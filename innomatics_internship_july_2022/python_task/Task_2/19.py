# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
n = int(input())
count = 0
for i in range (n):
    b = set(input().split())
    if a.issuperset(b):
        count += 1
print(count == n)