def binary_search(arr, x):

    low = 0

    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == x:

            return mid

        elif arr[mid] < x:

            low = mid + 1

        else:

            high = mid - 1

    return -1

arr = sorted(list(map(int, input("Enter the sorted array elements separated by space: ").split())))
x = int(input("Enter the element to search for: "))
result = binary_search(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element is not present in array")
