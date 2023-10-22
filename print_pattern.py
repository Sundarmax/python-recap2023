
def printSquare():
    for i in range(4):
        for j in range(4):
            print('',end="-")
        print()

def LeftPyramid():
    for i in range(4):
        for j in range(i+1):
            print('#',end=" ")
        print()

def makeTriangle():
    row = 6
    for i in range(row):
        # set starting point & add spaces
        for j in range(0,row-i-1):
            print('',end="-")
        for k in range(0,i+1):
            print('*',end=" ")
        print()
        
#printSquare()
#LeftPyramid()
makeTriangle()