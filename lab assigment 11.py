import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition
print("Addition:\n", A + B)

# Multiplication
print("Multiplication:\n", np.dot(A, B))
