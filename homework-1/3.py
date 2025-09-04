import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:, 1])
print(matrix[1, :])
print(matrix.flatten())
