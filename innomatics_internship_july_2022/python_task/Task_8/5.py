# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf, sqrt

x = 9800
n = 49
mean = 205
std = 15

mean_sum = n * mean
std_sum = sqrt(n) * std

def cdf(mean, std, x):
    return  0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print('{:.4f}'.format(abs(cdf(mean_sum, std_sum, x))))