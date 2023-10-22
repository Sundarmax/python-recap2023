#  https://www.scaler.com/topics/call-by-value-and-call-by-reference-in-python/

# When Immutable objects such as whole numbers, strings, etc are passed as arguments to the function call, the it can be considered as Call by Value.

def myFunc(a):
    'Example for call by value with immutable object'
    print("Value received in 'a' =", a)
    a+=2
    print("Value of 'a' changes to :",a)

a = 11
myFunc(a)
print("Value of a outside the function", a)

# When Mutable objects such as list, dict, set, etc., are passed as arguments to the function call, it can be called Call by reference in Python. When the values are modified within the function, the change also gets reflected outside the function.

def myFunc2(listA):
    'Example or call by reference with mutable object'
    listA.append(4)
    print("List values inside the function : ", listA)

listA  = [1,2,3]
# myFunc2(listA)
# print("List values outisde the function : ", listA)

# call by reference example - > 2

def myFunc3(listB):
    'Call by reference with different scenario'
    listB.append(4)
    listB = [6,7,8]
    print("object-id inside the function {}".format(id(listB)))
    print("List values inside the function : ", listB)

listB = [1,2,3]
print("object-id outside the function {}".format(id(listB)))
myFunc3(listB)

print("List values outside the function : ", listB)