import random
import time
from Hybrid_sorting_algorithm import hybrid_sort  # Import your hybrid_sort function

def test_hybrid_sort():
    test_cases = [
        [],
        [1],
        [3, 2, 1],
        [10, 20, 30, 40],
        [40, 30, 20, 10],
        [5, 5, 5, 5],
    ]

    for test_case in test_cases:
        print("Original List:", test_case)
        sorted_case = sorted(test_case)  # Use Python's built-in sorting as a reference

        # Measure the time it takes for the hybrid_sort function
        start_time = time.time()
        hybrid_sort(test_case)
        end_time = time.time()

    
        print("Sorted List:", test_case)
        assert test_case == sorted_case, f"Failed for input: {test_case}"
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        print("=" * 30)



if __name__ == "__main__":
    print("Test Case 1")
    test_hybrid_sort()
    print("All tests passed.\n")
    already_sorted_data = list(range(1, 100))
    print("Original List:")
    print(already_sorted_data)
    start_time = time.time()
    hybrid_sort(already_sorted_data)
    print("Final List:")
    print(already_sorted_data)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("=" * 30)


    duplicated_values_data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]
    print("Original List:")
    print(duplicated_values_data)
    start_time = time.time()
    hybrid_sort(duplicated_values_data)
    print("Final List:")
    print(duplicated_values_data)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("=" * 30)

    partially_sorted_data = [1, 2, 3, 7, 6, 5, 4, 8, 9, 10]
    print("Original List:")
    print(partially_sorted_data)
    start_time = time.time()
    hybrid_sort(partially_sorted_data)
    print("Final List:")
    print(partially_sorted_data)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("=" * 30)      

    data_with_negative_values = [5, -3, 0, -10, 8, 2, -1, 7, 9, 4]
    print("Original List:")
    print(data_with_negative_values)
    start_time = time.time()
    hybrid_sort(data_with_negative_values)
    print("Final List:")
    print(data_with_negative_values)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("=" * 30)

    large_random_data = [random.randint(1, 1000000) for _ in range(10000)]
    print("Original List: length")
    print(len(large_random_data))
    start_time = time.time()
    hybrid_sort(large_random_data)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("=" * 30)
 
 
