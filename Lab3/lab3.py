class Node:
     def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

class BST:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

    def update_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


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
                self.update_size()
            return insert_Bool

    def minValueNode(self):
        current = self
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
        
class coolBST(BST):        
    def __init__(self, key, c):
        super().__init__(key)
        self.c = c  # Set the constraint parameter (0.5 < c < 1)

    def check_c_constraint(self):
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        # Check if left or right subtree violates the c-constraint
        return left_size <= self.c * self.size and right_size <= self.c * self.size

    def in_order_traversal(self, node, keys):
        if node:
            self.in_order_traversal(node.left, keys)
            keys.append(node.key)
            self.in_order_traversal(node.right, keys)

    def build_balanced_bst(self, keys):
        if not keys:
            return None
        mid = len(keys) // 2
        root = coolBST(keys[mid], self.c)
        root.left = self.build_balanced_bst(keys[:mid])
        root.right = self.build_balanced_bst(keys[mid + 1:])
        root.update_size()
        return root

    def insert(self, key):
        super().insert(key)  # Perform regular BST insertion
        if not self.check_c_constraint():  # If the constraint is violated
            keys = []
            self.in_order_traversal(self, keys)  # Gather all keys in the subtree
            rebuilt_tree = self.build_balanced_bst(keys)  # Rebuild the subtree
            # Replace the current tree structure with the rebuilt one
            self.key = rebuilt_tree.key
            self.left = rebuilt_tree.left
            self.right = rebuilt_tree.right
            self.size = rebuilt_tree.size

# Standard BST
standard_bst = BST(100)
standard_bst.insert(30)
standard_bst.insert(70)
standard_bst.insert(20)
standard_bst.insert(40)
standard_bst.insert(60)
standard_bst.insert(80)

print("Standard BST:")
print(f"Root key: {standard_bst.key}, Size: {standard_bst.size}")

# Constrained BST with c = 0.7
constrained_bst = coolBST(100, 0.7)
constrained_bst.insert(30)
constrained_bst.insert(70)
constrained_bst.insert(20)
constrained_bst.insert(40)
constrained_bst.insert(60)
constrained_bst.insert(80)

print("\nConstrained BST:")
print(f"Root key: {constrained_bst.key}, Size: {constrained_bst.size}")