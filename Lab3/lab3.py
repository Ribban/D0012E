class Node:
    def init(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

class BST:
    key = None
    left = None
    right = None
    size = 1

    def init(self, key):
        self.key = key


    def insert(self, key):
            insert_Bool = False
            if key < self.key:
                if self.left:
                    insert_Bool = self.left.insert(key)
                else:
                    self.left = BST(key)
                    insert_Bool = True
            elif key > self.key:
                if self.right:
                    insert_Bool = self.right.insert(key)
                else:
                    self.right = BST(key)
                    insert_Bool = True
            if insert_Bool:
                self.size += 1
            return insert_Bool

    def minValueNode(node):
        current = node
        while current.left:
            current = current.left
        return current

    # Deleting a node
     # Delete a node from the BST
    def deleteNode(self, key):
        if self is None:
            return self

        # Find the node to be deleted
        if key < self.key:
            if self.left:
                self.left = self.left.deleteNode(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.deleteNode(key)
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                return temp

            elif self.right is None:
                temp = self.left
                return temp

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(self.right)

            # Replace the key with the inorder successor's key
            self.key = temp.key

            # Delete the inorder successor
            self.right = self.right.deleteNode(temp.key)

        return self
    def contain(self, key):
        if key < self.key:
            return self.left and self.left.contain(key)
        elif key > self.key:
            return self.right and self.right.contain(key)
        else:
            return True

# Initialize the tree
root = BST(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

# Delete nodes
root = root.deleteNode(20)  # Delete a leaf node
root = root.deleteNode(30)  # Delete a node with one child
root = root.deleteNode(50)  # Delete a node with two children