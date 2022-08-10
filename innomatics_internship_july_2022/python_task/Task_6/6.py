# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
import re
pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for i in range(n):
    for j in re.findall(pattern,input()):
        print(j)