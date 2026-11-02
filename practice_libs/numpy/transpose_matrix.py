import numpy as np

def transpose_matrix(matrix : np.ndarray) -> np.ndarray:
    transpose = np.empty((matrix.shape[1], matrix.shape[0]), dtype=matrix.dtype)
    i,j = matrix.shape
    for ele in range(i):
       transpose[ele] = matrix[:,ele] 
    return transpose 


a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", a)
a_t = transpose_matrix(a)
print("Transposed array:\n", a_t)

def column_matrix(matrix, col_index):
    if col_index < 0 or col_index >= matrix.shape[1]:
        raise IndexError("Column index out of bounds")
    return matrix[:, col_index]