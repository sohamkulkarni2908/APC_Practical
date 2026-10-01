import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
b = a.flatten()

print("Original array:")
print(a)
print("Flattened array:")
print(b)