import numpy as np
a = np.array([10, 25, 60, 45, 80, 30, 55, 90, 40, 70])
a[a > 50] = 0

print("Array:")
print(a)