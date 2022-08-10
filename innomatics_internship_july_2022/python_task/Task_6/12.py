import numpy as np

n, m = map(int, input().split())
array = np.array([input().split() for i in range(n)], int)
print(np.mean(array, axis=1))
print(np.var(array, axis=0))
print(round(np.std(array), 11))