import numpy as np

n, m = map(int, input().split())

my_array = np.array([input().split() for i in range(n)], int)

minimum = np.min(my_array, axis = 1)

print(np.max(minimum))