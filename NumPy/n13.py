import numpy as np
a = np.array([40, 10, 70, 20, 90, 30])

print("Original array:")
print(a)

print("Ascending order:")
print(np.sort(a))

print("Descending order:")
print(np.sort(a)[::-1])