import random
import time

class BST:
    key = None
    left = None
    right = None
    size = 1

    def __init__(self, key):
        self.key = key

    def insert(self, key):
        current = self
        while True:
            if key < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = BST(key)
                    self.size += 1
                    break
            elif key > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = BST(key)
                    self.size += 1
                    break
            else:
                break

    def contain(self, key):
        current = self
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False


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


def main():
    INSERTIONS, LOOKUPS = 10000, 10000

    print("Input Type\tc\tInsert Time\tLookup Time")

    for input_type in ("Random     ", "Increasing"):
        for c in (None, 0.9, 0.8, 0.7, 0.6):
            tree_type = coolBST if c else BST
            tree = tree_type(-1, c) if c is not None else tree_type(-1)

            if input_type == "Random     ":
                values = [random.randint(0, INSERTIONS) for _ in range(INSERTIONS)]
            else:
                values = list(range(INSERTIONS))

            insert_start = time.time()
            for value in values:
                tree.insert(value)
            insert_time = (time.time() - insert_start) * 1000

            lookup_values = [random.randint(0, INSERTIONS) for _ in range(LOOKUPS)]
            lookup_start = time.time()
            for value in lookup_values:
                tree.contain(value)
            lookup_time = (time.time() - lookup_start) * 1000

            c_display = "N/A" if c is None else f"{c}"
            print(f"{input_type}\t{c_display}\t{insert_time:.5f}    \t{lookup_time:.5f}")

main()