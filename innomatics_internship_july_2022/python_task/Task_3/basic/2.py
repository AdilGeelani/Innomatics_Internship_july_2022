# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 * bc**2)
mc = ac/2
bca =  math.atan(ab/bc)
# the property of right angle triange(median to hypotenuses divide it into 2 isoceles triangles soe am = bm = cm ) therefore angle acb = mbc
print(str(int(round(math.degrees(bca)))) + u"\N{DEGREE SIGN}")