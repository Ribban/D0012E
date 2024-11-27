import random

def maxKadane(arr):

    max_sum = int()
    curr_sum = 0

    for i in range(len(arr)):
        
        x = arr[i]

        if curr_sum + x > x:
            curr_sum += x
        
        else:
            curr_sum = x
        
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum

def maxRecursive(arr, start, end):

    if start == end:
        return arr[start], arr[start], arr[start], arr[start]
    
    mid = (start + end) // 2

    left = maxRecursive(arr, start, mid)
    right = maxRecursive(arr, mid + 1, end)

    max_sum = left[0]

    if right[0] > max_sum:
        max_sum = right[0]
    
    if left[2] + right[1] > max_sum:
        max_sum = left[2] + right[1]

    prefix = left[1]
    if right[1] + left[3] > prefix:
        prefix = right[1] + left[3]
    
    suffix = right[2]
    if left[2] + right[3] > suffix:
        suffix = left[2] + right[3]

    total = left[3] + right[3]

    return max_sum, prefix, suffix, total

def main():
    
    arr = [random.randint(-10, 10) for _ in range(8)]
    print("Random Array: ", arr)

    max_sum_kad = maxKadane(arr)
    print("Kadane: ", max_sum_kad)

    max_sum_rec = maxRecursive(arr, 0, len(arr) - 1)[0]
    print("Recursive: ", max_sum_rec)

    if max_sum_kad == max_sum_rec:
        print("Korrekt")
    else:
        print("Error")

main()