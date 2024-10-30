' assignment 10 - ins'

def insertion_sort_with_swaps(arr):
    n = len(arr)
    swap_count = 0  # Initialize swap counter
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Swap happens here (shift larger element to right)
            swap_count += 1      # Increment the swap count
            j -= 1
            
        arr[j + 1] = key  # Insert the key in its correct position

    return swap_count, arr

# Input as space-separated string
input_string = input("Enter the numbers separated by spaces: ")

# Convert input string to a list of integers
arr = list(map(int, input_string.split()))

# Sort the array and get the number of swaps
swaps, sorted_arr = insertion_sort_with_swaps(arr)

# Output the results
print(f"Sorted array: {sorted_arr}")
print(f"Number of swaps: {swaps}")
