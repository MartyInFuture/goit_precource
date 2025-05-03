import numpy as np

# (1, 12), (3, 54), (-1, 2)
# y = ax2 + bx + c

# 12 = a + b + c
# 54 = 9a + 3b + c
# 2 = a - b + c

a = np.array([[1, 1, 1], [9, 3, 1], [1, -1, 1]])

b = np.array([12, 54, 2])

x = np.linalg.solve(a, b)
print(x)