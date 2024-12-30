def linear_search(arr, x):
     for i in range(len(arr)):
       if arr[i] == x:
         return i
         return -1

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
x = int(input("Enter the element to search for: "))
result = linear_search(arr, x)
if result != -1:
  print(f"Element {x} is present at index {result}")
else:
  print("Element is not present in array")
