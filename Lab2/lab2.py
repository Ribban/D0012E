import random

def maxKadane(arr):                                                 # Kadanes Algorithm that finds the maximum subarray sum

    max_sum = int()                                                 # Initialize the maximum sum to a small value
    curr_sum = 0                                                    # Store the sum of the current subarray

    for i in range(len(arr)):                                       # Loop through each element in the array
        
        x = arr[i]                                                  # Current element

        if curr_sum + x > x:                                        # If adding the current element to the existing sum is greater
            curr_sum += x
        
        else:                                                       # Otherwise start a new starting at the current element
            curr_sum = x
        
        if curr_sum > max_sum:                                      # Update the maximum sum if the current subarray sum is larger
            max_sum = curr_sum

    return max_sum                                                  # Return the maximum sum found


def maxRecursive(arr, start, end):                                  # Divide-and-conquer approach to find the maximum subarray sum

    if start == end:                                                # Base case
        return arr[start], arr[start], arr[start], arr[start]
    
    mid = (start + end) // 2                                        # Find the midpoint of the array

    left = maxRecursive(arr, start, mid)                            # Recursively solve for the left half of the array
    right = maxRecursive(arr, mid + 1, end)                         # Recursively solve for the right half of the array

    max_sum = left[0]                                               # Start with the maximum sum from the left half

    # Update max_sum to be the largest of: left half, right half or the sum of the suffix or left and prefix of the right
    if right[0] > max_sum:
        max_sum = right[0]
    if left[2] + right[1] > max_sum:
        max_sum = left[2] + right[1]

    prefix = left[1]                                                # Compute the prefix sum for the combined array
    if right[1] + left[3] > prefix:
        prefix = right[1] + left[3]
    
    suffix = right[2]                                               # Compute the suffix sum for the combined array
    if left[2] + right[3] > suffix:
        suffix = left[2] + right[3]

    total = left[3] + right[3]                                      # Compute the total sum of the combined array

    return max_sum, prefix, suffix, total                           # Return the results: maximum subarray sum, prefix sum, suffix sum, and total sum


def main():
    
    arr = [random.randint(-10, 10) for _ in range(8)]               # Generate a random array of integers between -10 and 10, with 8 elements
    print("Random Array: ", arr)

    max_sum_kad = maxKadane(arr)
    print("Kadane: ", max_sum_kad)

    max_sum_rec = maxRecursive(arr, 0, len(arr) - 1)[0]
    print("Recursive: ", max_sum_rec)

    if max_sum_kad == max_sum_rec:                                  # Compare the results of both algorithms to ensure correctness
        print("Korrekt")
    else:
        print("Error")

main()