# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    pattern = re.compile(r'^[789]\d{9}$')
    numbers = input()
    if re.match(pattern, numbers):
        print('YES')
    else:
        print('NO')