# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf, sqrt

x = 250
n = 100
mean = 2.4
std = 2

mean_sum = n * mean
std_sum = sqrt(n) * std

def cdf(mean, std, x):
    return  0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print('{:.4f}'.format(abs(cdf(mean_sum, std_sum, x))))