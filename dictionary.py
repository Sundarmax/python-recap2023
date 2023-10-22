import copy

# Get list of keys
dic = {"a":1,"b":2}
print(dic.keys())

# unpacking
*x, = dic.keys()
print(x)

# can use iterables also.
y = [*dic.keys()]
print(y)

dic = {"a":1,"b":1}
# copy using copy operator
dic2 = dic.copy()
print(id(dic), id(dic2))

# copy using equal operator
dic3 = dic
# drawbacks of using '=' operator.
print(id(dic3),id(dic))

# dict with tuple as a key
tuple_ = (1,2,3)
dic4 = {tuple_ : "one,two,three"}
print(dic4)
# dict with list a key
list_ = [1,2,3 ]
# dic4[list_] = 4 # throws type error.
# print(dic4)
# dict with tuple having list as key
tuple_list = (1,2,['3'])
# dic4 = {tuple_list : "one,two,three"}
# print(dic4)