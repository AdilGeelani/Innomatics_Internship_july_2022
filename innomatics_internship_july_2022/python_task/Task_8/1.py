# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial
n = 6
p = 1.09/2.09
s = 0

for i in range(3, 7):
    s = s + (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))


print('{:.3f}'.format(s))