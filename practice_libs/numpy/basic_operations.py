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