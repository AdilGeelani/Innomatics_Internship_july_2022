#    Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf
mean = 70
std = 10
x1 = 80
x2 = 60
x3 = 60
def cdf(mean, std, x):
    return  0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print('{:.2f}'.format(abs(1-(cdf(mean, std, x1)))*100))
print('{:.2f}'.format(abs(1-(cdf(mean, std, x2)))*100))
print('{:.2f}'.format(abs(cdf(mean, std, x2))*100))
