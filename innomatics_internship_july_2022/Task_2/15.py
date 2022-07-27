# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = input().split()
b = int(input())
french = input().split()
e = set(eng)
f = set(french)
print(len(e.symmetric_difference(f)))