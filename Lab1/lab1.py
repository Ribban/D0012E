import random
import time

class Stack:
    class Node:                                                                 # Inner class to represent a node in linked list
        def __init__(self, data):                                               # Initialize the node with the given data
            self.data = data                                                    # Store the data for this node
            self.next = None                                                    # Pointer to the next node which is initially None

    def __init__(self):                                                         # Initialize the stack with no elements
        self.top = None                                                         # Represents the top of stack

    def push(self, data):                                                       # Add a new element to the top of stack
        new_node = self.Node(data)                                              # Create a new node with the provided data
        new_node.next = self.top                                                # Point the new node to the current top of stack
        self.top = new_node                                                     # Update top to the new top of stack

    def pop(self):                                                              # Remove and return the top element from stack
        if self.isEmpty():
            return None
        top_data = self.top.data                                                # Save the data of top element
        self.top = self.top.next                                                # Move top pointer to the next node
        return top_data                                                         # Return data of the removed element

    def isEmpty(self):                                                          # Check if the stack is empty
        return self.top is None

    def peek(self):                                                             # Return top element of stack without removing it
        if self.isEmpty():
            return None
        return self.top.data                                                    # Return the data of the top element


def sortStack(stack1):
    stack2 = Stack()                                                            # Initialize a temp stack (stack2) to temporarily hold elements for sorting.
    
    while not stack1.isEmpty():                                                 # Loop until stack1 is empty
        temp = stack1.pop()                                                     # Pop the top element from stack1 and store it in a temp variable
        
        while not stack2.isEmpty() and stack2.peek() > temp:                    # Move elements from stack2 back to stack1 if they are larger than temp
            stack1.push(stack2.pop())
        
        stack2.push(temp)                                                       # Push the temp element into stack2 at the correct position to keep sorted order
    
    while not stack2.isEmpty():                                                 # After sorting, transfer all elements from stack2 back to stack1
        stack1.push(stack2.pop())


def printStack(stacker):
    numbers = []                                                                # Init an empty list to store the stack elements for printing
    current = stacker.top                                                       # Start from the top of the stack

    while current:                                                              # Move through the stack, adding each elements data to the list
        numbers.append(current.data)
        current = current.next
    
    print(numbers)

def main():
    stack1 = Stack()

    # Keeps track to not reuse numbers
    unique = set()                                                              # Set to keep track of generated numbers
    while len(unique) < 100:
        num = random.randint(1, 100)                                            # Generate a random number
        if num not in unique:                                                   # Check if the number is unique
            unique.add(num)                                                     # Add the number to the set
            stack1.push(num)                                                    # Push the unique number onto the stack
    
    # Does not care for reusing numbers
#    for _ in range(100):
#        stack1.push(random.randint(1, 100))

    print("Original Stack:")
    printStack(stack1)

    start_time = time.time()
    sortStack(stack1)
    end_time = time.time()

    print("Sorted Stack:")
    printStack(stack1)

    print(f"Run time: {end_time - start_time:.6f} seconds") # Prints time usage with up to 6 decimals

main()