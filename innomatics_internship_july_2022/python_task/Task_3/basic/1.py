# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
z = complex(input())
print(abs(complex(z.real , z.imag)))
print(phase(complex(z.real, z.imag)))