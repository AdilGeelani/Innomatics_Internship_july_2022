import numpy as np
n,m,p=map(int,input().split())
li_1=[]
li_2 = []
for i in range(n):
    inp = input().split()
    li_1.append(inp)
for i in range(m):
    inp = input().split()
    li_2.append(inp)
array_1 = np.array(li_1, int)
array_2 = np.array(li_2, int)
print(np.concatenate((array_1, array_2)))