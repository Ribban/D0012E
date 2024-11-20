import random
import time

class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
class Stack:
    
    def __init__(self):                                                         # Initialize the stack with no elements
        self.content = None                                                       # Represents the top of stack

    def push(self, data):                                                       # Add a new element to the top of stack
        if isinstance(data, list):                                              # If data is a list
            self.content.extend(data)                                           # Add all elements in the list
        else:
            self.content.append(data)                                           # If data is a single element, add it to the stack

    def pop(self):                                                              # Remove and return the top element from stack
        return self.content.pop() if self.content else None                     # Remove and return the top of stack

    def isEmpty(self):                                                          # Check if the stack is empty
        return len(self.content) == 0


def sortStack(stack1):
    stack2 = Stack()                                                            # Initialize a temp stack (stack2) to temporarily hold elements for sorting

    while not stack1.isEmpty():                                                 # Loop until stack1 is empty
        temp = stack1.pop()                                                     # Pop the top element from stack1 and store it in a temp variable

        while stack2.content and stack2.content[-1] < temp:                    # Move elements from stack2 back to stack1 if they are smaller than temp
            stack1.push(stack2.pop())

        stack2.push(temp)                                                       # Push the temp element into stack2 at the correct position to keep sorted order

    stack1.push(stack2.content[::-1])

def main():
    stack1 = Stack()

    # Keeps track to not reuse numbers
#    unique = []                                                                 # List to keep track of generated numbers
#    while len(unique) < 100:
#        num = random.randint(1, 100)                                            # Generate a random number
#        if num not in unique:                                                   # Check if the number is unique
#            unique.append(num)                                                     # Add the number to the list
#            stack1.push(num)                                                    # Push the unique number onto the stack
    # Worstcase:
    worst = list(range(100, 0,-1))
    stack1.push(worst)

    # Does not care for reusing numbers
#    for _ in range(100):
#        stack1.push(random.randint(1, 100))

    print("Original Stack:")
    print(stack1.content)                                                       # Directly print the list representing the stack

    start_time = time.time()
    sortStack(stack1)
    end_time = time.time()

    print("Sorted Stack:")
    print(stack1.content)

    print(f"Run time: {end_time - start_time:.6f} seconds")                     # Prints time usage with up to 6 decimals
    

main()