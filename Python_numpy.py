import numpy as np

# https://www.youtube.com/watch?v=QUT1VHiLmmI&t=11s
def numpy_basics():
    a = np.array([1,2,3],'int16')
    b = np.array([[1,2,4],[5,6,7]])
    print(a)
    # get dimension
    print(a.ndim)
    print(b.ndim)
    # get type
    print(a.dtype)
    # get size
    print(a.itemsize * a.size) # itemsize refers single item.
    print(a.nbytes)

def access_element():
    a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
    print(a.ndim)
    # Get specific element
    print(a[1,0])
    # Get specific row
    print(a[0,:])
    # Get specific col
    print(a[:,2])
    # Getting little more fancy
    print(a[0, 1:-1:2])

#numpy_basics()
access_element()
