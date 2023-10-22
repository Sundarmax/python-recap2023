# lambda func
# This function can have any number of arguments but only one expression, which is evaluated and returned.

from functools import reduce
def add(x,y):
    return x + y

def python_lambda():
    # lambda input argument : expression
    a = lambda x,y : x + y
    string =  lambda str_var : str_var.lower()
    # lambda func
    print(a(2,3))
    print(string('WELCOME'))
    # normal func
    print(add(4,5))

def lambda_with_comprehension():
    number = [lambda arg=x : arg + 2 for x in range(5)]
    print(number)
    for n in number:
        print(n())

def lambda_with_if_esle():
    Max = lambda a,b : a if a>b else b
    print(Max(6,5))

def python_map_functions():
    # map (func, iterables)
    # returns map object
    veg_list = ["Banaana","Mango","Apple"]
    result  = map(lambda x:x.lower(), veg_list)
    print(list(result))
    def lambda_with_two_iterables():
        non_veg_list = ["chicken","MUTTON","FISH"]
        result = map(lambda x,y: str(x)+str(y),veg_list,non_veg_list)
        print(list(result))

    lambda_with_two_iterables()

def python_function_reduce():
    a = [2,4,6]
    b = [1,3,5]
    result_sum = reduce((lambda x,y:x + y),a)
    print(result_sum)


def python_function_filter():
    # filter (func with condition ,iterables)
    li = [5,7,22,33,44,55,6,0]
    result = list(filter(lambda x : (x//11 !=0),li))
    print(result)

# python_lambda()
#lambda_with_comprehension()
# lambda_with_if_esle()
# python_map_functions()
#python_function_reduce()
#python_function_filter()