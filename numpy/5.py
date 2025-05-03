import numpy as np

def get_polynom(coords):
  n = len(coords) - 1

  A = []
  B = []

  for x, y in coords:
    row = [x ** i for i in range(n + 1)]
    A.append(row)
    B.append(y) 

  A = np.array(A)
  B = np.array(B)

  coeffs = np.linalg.solve(A, B)

  return coeffs

coeffs = get_polynom([(1, 12), (3, 54), (-1, 2)])
print(coeffs)