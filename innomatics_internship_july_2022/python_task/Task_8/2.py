# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial
n = 10
s = 0
p = 0.12

for i in range(0, 3):
    s = s + (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))
    
print('{:.3f}'.format(s)) 

s = 0

for i in range(2, 11):
    s = s + (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))
    
print('{:.3f}'.format(s)) 