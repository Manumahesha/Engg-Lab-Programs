import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print("Array a:",a)
print("Array b:",b)
print("Sum of arrays a&b:", np.add(a,b))
print("Difference of arrays a&b:", np.subtract(a,b))
print("Product of arrays a&b:", np.multiply(a,b))
print("Sqare root of arrays a&b:", np.sqrt(a))
print("Exponential of arrays a&b:", np.exp(a))
print("Minimum Value of arrays a:", np.min(a))
print("Maximum Value of array a:", np.max(a))
print("Standard diviation of array b:", np.std(b))
print("Sum of all elements in array a:", np.sum(a))
c=np.array([[1,2],[3,4],[5,6]])
print("Array.c")
print(c)
print("Reshaped array c(2 rows,3 coloumn):")
print(np.reshape(c,(2,3)))
d=np.array([[1,2,3],[4,5,6]])
print("Array.d:")
print(d)
print ("transposed array d:")
print(np.transpose(d))

//output
Array a: [1 2 3 4 5]
Array b: [ 6  7  8  9 10]
Sum of arrays a&b: [ 7  9 11 13 15]
Difference of arrays a&b: [-5 -5 -5 -5 -5]
Product of arrays a&b: [ 6 14 24 36 50]
Sqare root of arrays a&b: [1.         1.41421356 1.73205081 2.         2.23606798]
Exponential of arrays a&b: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
Minimum Value of arrays a: 1
Maximum Value of array a: 5
Standard diviation of array b: 1.4142135623730951
Sum of all elements in array a: 15
Array.c
[[1 2]
 [3 4]
 [5 6]]
Reshaped array c(2 rows,3 coloumn):
[[1 2 3]
 [4 5 6]]
Array.d:
[[1 2 3]
 [4 5 6]]
transposed array d:
[[1 4]
 [2 5]
 [3 6]]
