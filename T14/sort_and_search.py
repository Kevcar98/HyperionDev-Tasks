
def insertion_sort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

#Binary Search was chosen as it has a time complexity of O(log n) where n is the number of lements in the arrayay:
def binary_search(array, target):

    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Linear Search was chosen as it has a time complexity of O(n) and it is a relatively small arrayay:
# It is chosen whn the dataset is small or unsorted, or when simplicity is prioritized over efficiency like in small databases
def linear_search(array, target):

    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def sort_and_search(array, target, algorithm='binary'):

    if algorithm == 'binary':
        sorted_array = insertion_sort(array)
        return binary_search(sorted_array, target)
    elif algorithm == 'linear':
        return linear_search(array, target)
    else:
        raise ValueError("Invalid search algorithm specified. Choose 'binary' or 'linear'.")

# Example usage
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9

# Using binary search
result_binary = sort_and_search(numbers, target, algorithm='binary')
print("Using binary search:")
if result_binary != -1:
    print(f"Found {target} at index {result_binary}.")
else:
    print(f"{target} not found in the array.")

# Using linear search
result_linear = sort_and_search(numbers, target, algorithm='linear')
print("\nUsing linear search:")
if result_linear != -1:
    print(f"Found {target} at index {result_linear}.")
else:
    print(f"{target} not found in the array.")
