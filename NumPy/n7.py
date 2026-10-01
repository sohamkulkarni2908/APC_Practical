import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
c = np.matmul(a, b)

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Result:")
print(c)