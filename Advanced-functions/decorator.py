
def decorator_func(func):
    def wrapper_func():
        print("wrapper func worked")
        return func()
    print('Decorator func worked')
    return wrapper_func

def show():
    print('Show worked')

# dec_show = decorator_func(show)
# dec_show()

# alternative implementation
@decorator_func
def display():
    print('Display worked')
# display()

# we want addTwoNumber func should calculate the sum of the square of two numbers instead of sum of two number.
# Here is the simple decorator to change the behaviour of the existing function

def decorator(func):
    def square_two_number(x,y):
        return func(x**2,y**2)
    return square_two_number

@decorator
def sumOfTwoNumber(x,y):
    return x + y

print(sumOfTwoNumber(4,5))



