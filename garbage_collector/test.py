import sys
import gc
x = [1,2,3]

print(sys.getrefcount(x))
 
y = x

print(sys.getrefcount(x))

# gc.collect() # manually clean up unused objects.

# print(sys.getrefcount(x))