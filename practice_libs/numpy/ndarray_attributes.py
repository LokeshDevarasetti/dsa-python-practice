import numpy as np
import numpy.random as rg

# sample array of 3 dimensions. shape will be (3, 5)
a = np.arange(15).reshape(3, 5)
print(a)
print("Array shape:", a.shape)
print("Array dimension",a.ndim)
print("Array data type:", a.dtype)
print("Array item size:", a.itemsize, "bytes")
print("Array total size:", a.nbytes, "bytes")
print("Array size:", a.size)

# sample array of 1 dimension. shape will be (3,)
# output : [1. 2. 3.]
b=np.array([1, 2, 3], dtype=np.float64)
print('Aray b')
print(b)
print("Array shape:", b.shape)
print("Array dimension",b.ndim)
print("Array data type:", b.dtype)
print("Array item size:", b.itemsize, "bytes")
print("Array total size:", b.nbytes, "bytes")
print("Array size:", b.size)

# sample array of 2 dimensions with the same elements as in array b. shape will be (3,1)
c = np.array([[1], [2], [3]], dtype=np.int32)
print('Aray c')
print(c)
print("Array shape:", c.shape)
print("Array dimension",c.ndim)
print("Array data type:", c.dtype)
print("Array item size:", c.itemsize, "bytes")
print("Array total size:", c.nbytes, "bytes")
print("Array size:", c.size)

# exaple of a 0 dimension array
d = np.array(42)
print('Aray d')
print(d)
print("Array shape:", d.shape)
print("Array dimension",d.ndim)
print("Array data type:", d.dtype)
print("Array item size:", d.itemsize, "bytes")
print("Array total size:", d.nbytes, "bytes")
print("Array size:", d.size)

# example of an empty array
# creates an array without initializing the entries
e = np.empty((2,3)) # uninitialized values
print('Aray e')
print(e)
print("Array shape:", e.shape)
print("Array dimension",e.ndim)
print("Array data type:", e.dtype)
print("Array item size:", e.itemsize, "bytes")
print("Array total size:", e.nbytes, "bytes")
print("Array size:", e.size)

# exmple to convert 1D array b to 2D array
# output : 
# [[1.]
#  [2.]
#  [3.]]
b_reshaped = b.reshape((3, 1))
print('Reshaped array b to 2D')
print(b_reshaped)
print("Array shape:", b_reshaped.shape)
print("Array dimension",b_reshaped.ndim)
print("Array data type:", b_reshaped.dtype)
print("Array item size:", b_reshaped.itemsize, "bytes")
print("Array total size:", b_reshaped.nbytes, "bytes")
print("Array size:", b_reshaped.size)


print('rg.random((2, 2)) \n', rg.random((2, 4,2, 5)))  # random values in a 2x2 array
