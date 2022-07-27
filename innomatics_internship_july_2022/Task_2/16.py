# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
a = set(map(int, input().split()))
n2 = int(input())
for i in range(n2):
    command, n = input().split()
    b = set(map(int, input().split()))
    if command == "intersection_update":
        a.intersection_update(b)
    elif command == "update":
        a.update(b)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif command == "difference_update":
        a.difference_update(b)
print(str(sum(a)))