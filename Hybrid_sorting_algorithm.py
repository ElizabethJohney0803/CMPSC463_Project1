def insertion_sort(arr, low, high):
    # Iterate through the elements in the range [low, high]
    for i in range(low + 1, high + 1):
        # Store the current element in 'key'
        key = arr[i]
        # Initialize 'j' to the previous element's index
        j = i - 1
        # Compare 'key' with elements to the left until you find the correct position
        while j >= low and key < arr[j]:
            # If 'key' is smaller than the element at 'j', move 'arr[j]' one position to the right
            arr[j + 1] = arr[j]
            j -= 1
        # Place 'key' in its correct position in the sorted subarray
        arr[j + 1] = key


def quicksort(arr, low, high, threshold):
    # Check if there are elements to be sorted in the subarray
    if low < high:
        # If the subarray size is less than or equal to the threshold, use insertion sort
        if high - low <= threshold:
            insertion_sort(arr, low, high)
        else:
            # Find the pivot index by partitioning the array
            pivot_index = partition(arr, low, high)
            # Recursively sort the left subarray (elements less than the pivot)
            quicksort(arr, low, pivot_index - 1, threshold)
            # Recursively sort the right subarray (elements greater than the pivot)
            quicksort(arr, pivot_index + 1, high, threshold)


def partition(arr, low, high):
    # Improved pivot selection: choose the median of three elements
    mid = (low + high) // 2
    
    # Reorder 'low', 'mid', and 'high' so that 'low' is the median
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # 'pivot' is now the median of 'low', 'mid', and 'high'
    pivot = arr[mid]
    
    # Initialize 'left' and 'right' pointers
    left = low + 1
    right = high

    done = False
    
    # Start the partitioning process
    while not done:
        # Find an element on the left that is greater than 'pivot'
        while left <= right and arr[left] <= pivot:
            left += 1
        # Find an element on the right that is smaller than 'pivot'
        while arr[right] >= pivot and right >= left:
            right -= 1
        # If 'right' is less than 'left', the partitioning is complete
        if right < left:
            done = True
        else:
            # Swap the elements at 'left' and 'right' to maintain the order
            arr[left], arr[right] = arr[right], arr[left]
    
    # Swap the pivot element into its correct position in the sorted array
    arr[mid], arr[right] = arr[right], arr[mid]
    
    # Return the index of the pivot element in its sorted position
    return right


def hybrid_sort(arr, threshold=10):
    # Call the quicksort function on the entire array with the specified threshold
    quicksort(arr, 0, len(arr) - 1, threshold)


if __name__ == "__main__":
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    hybrid_sort(unsorted_array)
    print("Sorted array:", unsorted_array)
