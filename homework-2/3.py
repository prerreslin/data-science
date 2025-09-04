import numpy as np

matrix = np.array([[5, 2, 8],
                   [1, 7, 4],
                   [3, 6, 9]]
)

res = np.delete(matrix, 1, axis=0)
print(res)
