import numpy as np

a = np.array([[3, 0, 3], [6, 1/4, 0], [1, 1/3, 1]])

b = np.array([1, 1, 1])

x = np.linalg.solve(a, b)\

a2 = 1 / x[0]
b2 = 1 /x[1]  
c2 = 1 / x[2] 

print(a2, b2, c2)