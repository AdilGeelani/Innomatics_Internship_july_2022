# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf
mean = 20
std = 2
x1 = 19.5
x2 = 20
x3 = 22
def cdf(mean, std, x):
    return  0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print('{:.3f}'.format(abs(cdf(mean, std, x1))))
print('{:.3f}'.format(abs(cdf(mean, std, x2) - cdf(mean, std, x3))))