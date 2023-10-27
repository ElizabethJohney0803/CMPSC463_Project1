## Hybrid Sorting Algorithm Report

### Introduction
The hybrid sorting algorithm is designed to efficiently sort an array of elements by combining two sorting methods: quicksort and insertion sort. The choice between these two sorting methods depends on the size of the subarray being sorted. When the subarray size is smaller than a specified threshold, insertion sort is used due to its better performance for small arrays. For larger subarrays, quicksort is employed, a highly efficient comparison-based sorting algorithm.

### Components of the Algorithm

#### 1. `insertion_sort` Function
The `insertion_sort` function is a straightforward sorting method that is used for small subarrays. It works as follows:
- It iterates through the elements in the specified range `[low, high]`.
- For each element, it is temporarily stored in a variable called 'key.'
- The algorithm then compares the 'key' with the elements to its left until it finds the correct position.
- Elements greater than 'key' are shifted one position to the right to make space for 'key.'
- The final step is to place 'key' in its correct sorted position within the subarray.

#### 2. `quicksort` Function
The `quicksort` function is a recursive sorting algorithm that is used for larger subarrays. It incorporates the following steps:
- It checks if there are elements to be sorted within the given subarray (specified by `low` and `high`).
- If the subarray size is less than or equal to a specified threshold, it uses the `insertion_sort` function for efficiency.
- If the subarray size exceeds the threshold, it proceeds with quicksort.
- Quicksort works by partitioning the array and recursively sorting the left and right subarrays. The pivot selection is optimized by choosing the median of three elements for better performance.

#### 3. `partition` Function
The `partition` function is used by the `quicksort` function to rearrange the elements around a pivot element. It includes the following steps:
- It calculates the median index 'mid' of the subarray.
- It reorders the elements at 'low,' 'mid,' and 'high' so that 'low' contains the median value among the three.
- The pivot element is set to the value at index 'mid.'
- Left and right pointers, 'left' and 'right,' are initialized to the start and end of the subarray.
- A while loop is used to compare and swap elements to ensure elements less than the pivot are on the left, and elements greater than the pivot are on the right.
- Once the pointers meet, the partitioning process is complete, and the pivot is swapped to its correct sorted position.
- The function returns the index of the pivot in its sorted position.

#### 4. `hybrid_sort` Function
The `hybrid_sort` function serves as the main entry point for the hybrid sorting algorithm. It allows specifying a threshold value for the switch between insertion sort and quicksort. The function calls the `quicksort` function on the entire array with the specified threshold.

### Advantages of the Hybrid Sorting Algorithm
- The hybrid approach takes advantage of both quicksort's efficiency for larger subarrays and insertion sort's simplicity and performance for small subarrays.
- The threshold value can be adjusted to optimize the algorithm's performance based on the specific use case.
- The use of the median-of-three pivot selection in the `partition` function improves the performance of quicksort.

### Conclusion
The hybrid sorting algorithm combines the strengths of quicksort and insertion sort to efficiently sort an array of elements. It adapts to the size of the subarray being sorted, utilizing insertion sort for small subarrays and quicksort for larger ones. This adaptive approach enhances sorting performance in a variety of scenarios, making it a valuable sorting algorithm.
