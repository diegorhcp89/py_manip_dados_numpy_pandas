# aula 1 - indexação e fatiamento
import numpy as np

array_multi = np.array([[1, 2, 3, 4, 5, 6],[4, 5, 6, 7, 8, 9]])

print(array_multi[1][1])

print(array_multi[0][1:4])

print(array_multi[array_multi > 3])

print(array_multi[:1, 1:4])

print(array_multi[:, 1:4])
