import numpy as np
n, m = map(int, input().split())

my_array = np.array([input().split() for i in range(n)], int)
s = np.sum(my_array, axis = 0)
print(np.prod(s))

