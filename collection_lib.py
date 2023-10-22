from collections import OrderedDict,defaultdict
from collections import ChainMap
from collections import namedtuple
import itertools as it

# order of the item is maintained
# even the items are added/removed in the future.
subject = OrderedDict()
subject['a'] = 'Eng'
subject['c'] = 'Math'

values = defaultdict(int)
# print(values['1']) # return 0

dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }

# merge two dict
res = ChainMap(dic1,dic2)
# for key,val in res.items():
#     print(key,val)

# itertools
numbers = [1,2,3]
letter = ['a','b','c']
combined = it.product(numbers,letter)
# for i in combined:
#     print(i)

# flattening the list
list_of_lists = [[1, 2], [3, 4]]
chain_obj = it.chain.from_iterable(list_of_lists)
# print(list(chain_obj))

# coroutine
def coroutine():
    while True:
        x = yield
        print(f"Received {x}")

# cor = coroutine()
# next(cor)
# cor.send(1)
# cor.send(2)
# clousure
def outer_func(x):
    def inner_func(y):
        return x * y
    return inner_func
closure = outer_func(5)
# print(closure(6))

# named tuple

subject =  namedtuple('person',['name','age','dob'])
subj = subject('SUNDAR','21','1995')
print(type(subj))