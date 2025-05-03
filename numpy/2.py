import numpy as np

# Math x + (x - 120) + (x - 220) = 1328

a = np.array([[1, 1, 1], [1, -1, 0], [0, 1, -1]])
b = np.array([1328, 120, 100])

x = np.linalg.solve(a, b)
print(x)