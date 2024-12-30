integer_array = [10, 20, 30, 40, 50]
print("Array items:", integer_array)
index = int(input("Enter an index (0 to 4) to access an element: "))

if 0 <= index < len(integer_array):
    element = integer_array[index]
    print(f"Element at index {index} is: {element}")
else:
    print("Invalid index. Please enter an index between 0 and 4.")
