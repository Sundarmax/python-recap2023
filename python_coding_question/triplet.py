
import math

N = 10

def find_triplet():
    '''
    TIME COMPLEXITY : O(N) ^2
    '''
    square_dict = {}
    rev_dict = {}
    for i in range(1,N+1):
        square_dict[i] =  i * i
        rev_dict[i*i] = i
    
    print(square_dict,rev_dict)

    result = []
    for ikey,ival in square_dict.items():
        for jkey,jval in square_dict.items():
            if ikey != jkey:
                calc_sum = square_dict[ikey] + square_dict[jkey]
                if calc_sum in rev_dict:
                    print(calc_sum)
                    get_sqrt = int(math.sqrt(calc_sum))
                    temp = [ikey,jkey,get_sqrt]
                    if sorted(temp) not in result:
                        result.append(sorted(temp))
    print(result)

def find_triplet2(a):
    '''
    TIME COMPLEXITY : O(N)^2
    IT USES THREE POINTER APPROACH.
    '''
    for i in range(len(a)):
        a[i] = a[i] * a[i]
    # sort an array
    a.sort()
    print(a)
    # use threee pointer to solve it
    for i in range(len(a)-1,-1,-1):
        j = 0 # start
        k = i-1 # prv to i
        while j < k: # since the array is sorted
            if a[j] + a[k] == a[i]:
                print(a[i],a[j],a[k])
                break
            else:
                if a[j] + a[k] < a[i]:
                    j = j +1
                else:
                    k = k -1    
    else:
        print('No triplet found')
#find_triplet()

arr2 = [3, 1, 4, 6, 5]
find_triplet2(arr2)