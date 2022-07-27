# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    n1 = int(input())
    a = set(input().split())
    n2 = int(input())
    b = set(input().split())
    a.difference_update(b)
    if len(a) == 0:
        print(True)
    else:
        print(False)