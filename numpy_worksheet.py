import numpy as np
import time
import sys

# 1. Show the diffrence beetwen the size of python operation confront to numpy operation

l = range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)

# result in terminal:
# 28000
# 8000

# 2. Show the diffrence beetwen the time python vs numpy

SIZE = 1000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x+y for x,y in zip(l1,l2))]
print("python list took: ", (time.time()-start)*1000)
# numpy array
start = time.time()
result = a1 + a2
print("numpy took: ", (time.time()-start)*1000)

# result in terminal:
# python list took:  0.0011920928955078125
# numpy took:  0.008344650268554688




