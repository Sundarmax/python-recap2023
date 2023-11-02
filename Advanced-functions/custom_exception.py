class InvalidAgeException(Exception):
    pass

try:
    a = input("Enter your age : ")
    if int(a) < 18:
        raise InvalidAgeException
    else:
        print("Eligibile to vote")
except InvalidAgeException:
    print("Not eligible to vote")

# Try and except
try:
    # a = [1]
    # b = a[2]
    # c = {}
    # d = c['d']
    temp = 'a' + 2
except IndexError:
    print('Index error is raised')
except KeyError:
    print('Key error is raised')
except NameError:
    print('Variable is not defined')
except TypeError:
    print('Type error is raised')

class Error(Exception):
    pass
class ValueSmallError(Error):
    pass
# custom exception
try:
    #n = int(input('Enter a num : '))
    n = 4
    if n < 20:
        raise ValueSmallError
except ValueSmallError:
    print('Value is too smaller')
