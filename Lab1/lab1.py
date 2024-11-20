import random
import time

class Node:
        def __init__(self, data):                                               # Initializes a node for the linked list
            self.data = data                                                    # Data stored in the node
            self.next = None                                                    # Pointer to the next node in the stack

class Stack:
    
    def __init__(self):                                                         # Initialize the stack with no elements
        self.content = None                                                     # Represents the top of stack

    def push(self, data):                                                       # Add a new element to the top of stack
        new_node = Node(data)                                                   # Create a new node with given data
        new_node.next = self.content                                            # Link the new node to the top of stack
        self.content = new_node                                                 # Update top of stack to the new node

    def pop(self):                                                              # Remove and return the top element from stack
        if self.isEmpty():                                                      # Check if stack is empty
            return None
        data = self.content.data                                                # Get data from top node
        self.content = self.content.next                                        # Update top of stack to next node
        return data                                                             # Return data of removed node

    def isEmpty(self):                                                          # Check if the stack is empty
        return self.content is None                                             # Stack is empty if top node is None
    
    def compare(self):                                                          # Returns a list of all elements in stack fro printing
        elements = []                                                           # List to store elements
        current = self.content                                                  # Start from top of stack
        while current:                                                          # Move through stack until the end
            elements.append(current.data)                                       # Append data of current node to list
            current = current.next                                              # Move to next node
        return elements                                                         # Returns the list

def sortStack(stack1):
    stack2 = Stack()                                                            # Initialize a temp stack (stack2) to temporarily hold elements for sorting

    while not stack1.isEmpty():                                                 # Loop until stack1 is empty
        temp = stack1.pop()                                                     # Pop the top element from stack1 and store it in a temp variable

        while not stack2.isEmpty() and stack2.content.data > temp:              # Move elements from stack2 back to stack1 if they are smaller than temp
            stack1.push(stack2.pop())

        stack2.push(temp)                                                       # Push the temp element into stack2 at the correct position to keep sorted order

    while not stack2.isEmpty():
        stack1.push(stack2.pop())

def main():
    stack1 = Stack()

    # Keeps track to not reuse numbers
#    unique = []                                                                 # List to keep track of generated numbers
#    while len(unique) < 100:
#        num = random.randint(1, 100)                                            # Generate a random number
#        if num not in unique:                                                   # Check if the number is unique
#            unique.append(num)                                                  # Add the number to the list
#            stack1.push(num)                                                    # Push the unique number onto the stack
    # Worstcase:
    for i in range(1, 100001):
        stack1.push(i)

    # Does not care for reusing numbers
#    for _ in range(100):
#        stack1.push(random.randint(1, 100))

    print("Original Stack:")
    print(stack1.compare())                                                      # Directly print the list representing the stack

    start_time = time.time()
    sortStack(stack1)
    end_time = time.time()

    print("Sorted Stack:")
    print(stack1.compare())

    print(f"Run time: {end_time - start_time:.6f} seconds")                      # Prints time usage with up to 6 decimals

main()