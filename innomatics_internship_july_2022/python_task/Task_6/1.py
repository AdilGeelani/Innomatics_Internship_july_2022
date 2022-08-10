import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    result = numpy.array(arr, float)
    return(result[::-1])

arr = input().strip().split(' ')
result = arrays(arr)
print(result)