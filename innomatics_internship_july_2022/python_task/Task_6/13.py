import numpy as np
n= int(input())
array_a = np.array([input().split() for i in range(n)], int)
array_b = np.array([input().split() for i in range(n)], int)
print (np.dot(array_a, array_b))
