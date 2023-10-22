


def findPair(arr,target_sum):
    '''
    Brute force approach
    '''
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if target_sum == arr[i] + arr[j]:
                print(arr[i],arr[j],end=",")


def findPair2(arr,target_sum):
    '''
    Hashing approach
    '''
    hash_map = {}
    for i in range(len(arr)):
        temp = target_sum - arr[i]
        if temp in hash_map:
            print('Element exist')
            print(arr[i],arr[hash_map[temp]])
        hash_map[arr[i]] = i

A = [0, -1, 2, -3, 1]
x = -2
# findPair(A,x)

arr2 = [1,4,45,6,10,8]
#x = 16
#findPair2(arr2,x)
findPair2(A,x)