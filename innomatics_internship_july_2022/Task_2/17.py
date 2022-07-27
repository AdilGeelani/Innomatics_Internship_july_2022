# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
li = input().split()
a = set()
b = set()
for i in li:
    if i in a:
        b.add(i)
    else:
        a.add(i)

diff = a.difference(b)
print(list(diff)[0])
