# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
n = 100
mean = 500
std = 80
space = 0.95
z = 1.96

print('{:.2f}'.format(abs(mean - (std / sqrt(n)) * z)))
print('{:.2f}'.format(abs(mean + (std / sqrt(n)) * z)))

