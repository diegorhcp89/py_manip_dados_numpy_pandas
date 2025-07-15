# aula 1 - indexação e fatiamento
import numpy as np

array_multi = np.array([[1, 2, 3, 4, 5, 6],[4, 5, 6, 7, 8, 9]])

print(array_multi[1][1])

print(array_multi[0][1:4])

print(array_multi[array_multi > 3])

print(array_multi[:1, 1:4])

print(array_multi[:, 1:4])

# aula 2 - operações matemáticas

print(array_multi + 2)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)

print(arr1 * arr2)

#broadcasting
print(array_multi + arr1[2])
