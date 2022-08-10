import numpy as np
n , m = input().split();
li = [];
for i in range(int(n)):
    i = input().split();
    li.append(i);
arr = np.array(li,int);
print(np.transpose(arr))
print(arr.flatten())
