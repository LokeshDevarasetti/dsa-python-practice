import numpy as np

# 1D array operations
a = np.array([5,10,15,20])
b = np.arange(4)
print("Array b:", b)

c= a - b
print("Array c (a-b):", c)

b_square = b**2
print("Array d (b^2):", b_square)

sin_array = np.sin(a)
print("Sine of array a:", sin_array)

print("Max of array a:", np.max(a))
print("Min of array a:", np.min(a))
print("boolean array (a<15):", a<15)

# 2D array operations
A = np.array([[12,6,3],[5,17,2],[1,2,14]])
B = np.array([[5,2,3],[6,5,4],[7,8,9]])
B_float = B.astype(np.float64)  # convert B to float type
print('B converted to float type \n', B_float)
print("Array A:\n", A)

print("Sum of all elements in A:", np.sum(A))
print('matrix multiplication with a number(scalar) 5: 5A \n', 5*A)
print('matrix addition A + B \n', A + B)
print('matrix subtraction A - B \n', A - B)
print('matrix multiplication A * B \n', A * B)  # element-wise multiplication
print('matrix division A / B \n', A / B)        # element-wise division

# matrix product (dot product) is A @ B or np.dot(A, B)

# recommended to define the matrix as np.array and  use @ operator for matrix product
# np.dot() is slower than @ operator
print('matrix product A @ B \n', A @ B) 
print('matrix product np.dot(A, B) \n', np.dot(A, B))

B += 2*A
print('After B += 2*A, B is \n', B)

# example of upcasting
# when operating on two arrays of different data types, NumPy will upcast the smaller type
A_float = A + B_float
print('After A + B_float, A_float is \n', A_float)
print('A_float data type:', A_float.dtype)

C_complex = A + 2j*B
print('After A + 2j*B, C_complex is \n', C_complex)
print('C_complex data type:', C_complex.dtype)

print('sum of each column \n',A.sum(axis=0))     # sum of each column

print('sum of each row \n',A.sum(axis=1))        # sum of each row
print('mean of each column \n',A.mean(axis=0))   # mean of each column
print('mean of each row \n',A.mean(axis=1))      # mean of each row
print('cummulative sum of each column \n',A.cumsum(axis=0))  # cumulative sum of each column
print('cummulative sum of each row \n',A.cumsum(axis=1))     # cumulative sum of each row

# 3D array operations
A_3D = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]],[[5,5,5],[6,6,6]]])
print('3D array A_3D \n', A_3D)
print('shape of A_3D:', A_3D.shape)
print('sum of each "depth" \n',A_3D.sum(axis=0))     # sum of each "depth"
print('sum of each row \n',A_3D.sum(axis=1))        # sum of each row
print('sum of each column \n',A_3D.sum(axis=2))      # sum of each column

# Universal functions (ufuncs) are functions that operate element-wise on arrays.
print('Square root of each element in A \n', np.sqrt(A))
print('Exponential (e^x) of each element in A \n', np.exp(A))
print('Natural logarithm (ln) of each element in A \n', np.log(A))
print('Base-10 logarithm (log10) of each element in A \n', np.log10(A))

# indexing and slicing
# 1D array
p = np.arange(10)**2
print('Array p:', p)
print('p[2]:', p[2])      # third element
print('p[2:5]:', p[2:5])  # elements from index 2 to 4
p[0:5] = 1000  # set first five elements to 1000
print('After setting first five elements to 1000, p:', p)
p[:6:2] = 80 # from start to position 6, exclusive, set every 2nd element to 80
print('After setting every 2nd element to 80 up to index 6, p:', p)
print('Last element p[-1]:', p[-1])  # last element
print('Last three elements p[-3:]:', p[-3:])  # last three elements
p[::-1]  # reversed array
print('Reversed array p:', p)
for i in p:
    print(i**(1/2))  # square root of each element

# 2D array
def fun(x, y):
    return 10 * x + 2*y
q = np.fromfunction(fun, (5, 4), dtype=int)
print('Array q:\n', q)
print('q[2,3]:', q[2,3])    # element at 3rd row, 4th column
print('q[1:3,0:3]: ', q[1:3,0:3])  # sub-array from 2nd to 3rd row, 1st to 3rd column

# 3D array
r = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print('3D array r:\n', r)
print('shape of r:', r.shape)
print('r[1, ...]: \n', r[1, ...])  # all elements from 2nd 2D array

# iterating
print('Iterating over each element in r:')
for row in r:
    print(row)

print('Iterating over each element in r using nditer:')
for x in np.nditer(r):
    print(x)

print('iterating using flat. r.flat is an iterator that iterates over all elements of the array:')
for x in r.flat:
    print(x)
print('q[1:3,0:3]: ', q[:,1])