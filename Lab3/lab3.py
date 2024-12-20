import random
import time
import plotly.graph_objects as go

class BST:                                      # Binary search tree implementation
    key = None                                  # Value stored in the current node
    left = None 
    right = None
    size = 1                                    # Size of the subtree rooted at this node

    def __init__(self, key):
        self.key = key                          # Initialize the root node with a key

    def insert(self, key):                      # Inserts a key into the BST, maintaining the BST
        current = self
        while True:
            if key < current.key:               # Go to the left subtree
                if current.left:
                    current = current.left
                else:                           # Create a new node if the left child is None
                    current.left = BST(key)
                    self.size += 1
                    break
            elif key > current.key:             # Go to the right subtree
                if current.right:
                    current = current.right
                else:                           # Create a new node if the right child is None
                    current.right = BST(key)
                    self.size += 1
                    break
            else:                               # Key already exists, no duplicates allowed
                break

    def contain(self, key):                     # Checks if a key exists in the BST
        current = self
        while current:
            if key < current.key:               # Search in the left subtree
                current = current.left
            elif key > current.key:             # Search in the right subtree
                current = current.right
            else:                               # Key found
                return True
        return False                            # Key not found

    def visualize(self):                        # Visualizes the BST as a graph
        def collect_edges_and_nodes(node, x, y, level, pos):
            if not node:
                return
            
            # Collect current node position and label
            nodes.append((x, y, str(node.key)))
            if node.left:
                edges.append(((x, y), (x - dx / (2 ** level), y - dy)))
                collect_edges_and_nodes(node.left, x - dx / (2 ** level), y - dy, level + 1, 'left')
            if node.right:
                edges.append(((x, y), (x + dx / (2 ** level), y - dy)))
                collect_edges_and_nodes(node.right, x + dx / (2 ** level), y - dy, level + 1, 'right')

        dx, dy = 1, 1  # Horizontal and vertical distance between levels
        edges = []     # List of edges (connections between nodes)
        nodes = []     # List of nodes with positions and labels

        collect_edges_and_nodes(self, 0, 0, 1, 'root')

        # Extract edge coordinates
        Xe, Ye = [], []
        for edge in edges:
            Xe += [edge[0][0], edge[1][0], None]
            Ye += [edge[0][1], edge[1][1], None]

        # Extract node coordinates and labels
        Xn = [node[0] for node in nodes]
        Yn = [node[1] for node in nodes]
        labels = [node[2] for node in nodes]

        # Create the Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe, y=Ye, mode='lines',
                                 line=dict(color='rgb(210,210,210)', width=1), hoverinfo='none'))
        fig.add_trace(go.Scatter(x=Xn, y=Yn, mode='markers', name='Nodes',
                                 marker=dict(symbol='circle-dot', size=18, color='#6175c1',
                                             line=dict(color='rgb(50,50,50)', width=1)),
                                 text=labels, hoverinfo='text', opacity=0.8))

        fig.update_layout(showlegend=False, xaxis=dict(showline=False, zeroline=False),
                          yaxis=dict(showline=False, zeroline=False),
                          margin=dict(l=40, r=40, b=85, t=100),
                          hovermode='closest')
        fig.show()


class coolBST(BST):                             # Extended BST with balancing capabilities based on a constraint (c)
    def __init__(self, key, c):
        super().__init__(key)                   # Initialize the base BST
        self.c = c                              # Set the constraint parameter (0.5 < c < 1)

    def check_c_constraint(self):               # Verifies if the c-constraint is satisfied for the current node
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        # Check if left or right subtree violates the c-constraint
        return left_size <= self.c * self.size and right_size <= self.c * self.size

    def in_order_traversal(self, node, keys):   # Performs an in-order traversal to collect keys in sorted order
        if node:
            self.in_order_traversal(node.left, keys)
            keys.append(node.key)
            self.in_order_traversal(node.right, keys)

    def build_balanced_bst(self, keys):         # Builds a balanced BST from a sorted list of keys
        if not keys:
            return None
        mid = len(keys) // 2
        root = coolBST(keys[mid], self.c)       # Create root with the middle key
        root.left = self.build_balanced_bst(keys[:mid])
        root.right = self.build_balanced_bst(keys[mid + 1:])
        root.update_size()
        return root

    def update_size(self):                      # Updates the size of the subtree
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        self.size = 1 + left_size + right_size

    def insert(self, key):                      # Inserts a key into the BST and balances if the c-constraint is violated
        super().insert(key)                     # Perform regular BST insertion
        if not self.check_c_constraint():       # If the constraint is violated
            keys = []
            self.in_order_traversal(self, keys) # Gather all keys in the subtree
            rebuilt_tree = self.build_balanced_bst(keys)   # Rebuild the subtree
            # Replace the current tree structure with the rebuilt one
            self.key = rebuilt_tree.key
            self.left = rebuilt_tree.left
            self.right = rebuilt_tree.right
            self.size = rebuilt_tree.size

def main():                                     # Main function to benchmark insertion and lookup times
    INSERTIONS, LOOKUPS = 100, 100          # Number of operations to perform

    print("Input Type\tc\tInsert Time\tLookup Time")

    for input_type in ("Random     ", "Increasing"): # Test both random and increasing input
        for c in (None, 0.9, 0.8, 0.7, 0.6, 0.51):         # Different balancing constraints
            tree_type = coolBST if c else BST        # Use coolBST only if a constraint is specified
            tree = tree_type(-1, c) if c is not None else tree_type(-1)

            if input_type == "Random     ":          # Generate input values
                values = [random.randint(0, INSERTIONS) for _ in range(INSERTIONS)]
            else:
                values = list(range(INSERTIONS))     # Sequential increasing values

            insert_start = time.time()
            for value in values:
                tree.insert(value)
            insert_time = (time.time() - insert_start) * 1000

            lookup_values = [random.randint(0, INSERTIONS) for _ in range(LOOKUPS)] # Generate random lookup values
            lookup_start = time.time()
            for value in lookup_values:
                tree.contain(value)
            lookup_time = (time.time() - lookup_start) * 1000

            # Display the results
            c_display = "None" if c is None else f"{c}"
            print(f"{input_type}\t{c_display}\t{insert_time:.5f}    \t{lookup_time:.5f}")
            tree.visualize()

main()
    
