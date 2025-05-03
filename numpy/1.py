import numpy as np

# Math x + y + z = 50000
# 0.5x + 0.7y + 0z = 2250 | * 100
# 0.5x + 0y + 0.6z = 1400 | * 100

a = np.array([[1, 1, 1], [5, 7, 0], [5, 0, 6]])
b = np.array([50000, 225000, 140000])

x = np.linalg.solve(a, b)
print(x)