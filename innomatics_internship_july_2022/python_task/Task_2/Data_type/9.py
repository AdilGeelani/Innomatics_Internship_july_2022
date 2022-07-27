# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(input().split())
n = int(input())
b = set(input().split())
inter = a.intersection(b)
u = a.union(b)

print ('\n'.join(sorted(u.difference(inter), key=int)))
