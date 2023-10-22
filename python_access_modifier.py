
class Test:
    varPublic = 65
    _varProtected = 75
    __varPrivate = 85

    def public_method(self):
        print("public method is called")
    
    def _protected_method(self):
        print("Hey This is protected method")

    def __private_method(self):
        print("Hey This is private method")

obj = Test()
obj.public_method()
obj._protected_method()
# obj.__private_method() # This throws attribute error 
print(dir(obj))
obj._Test__private_method() # name mangling
# source : https://bhartidig.medium.com/access-modifiers-in-python-public-private-protected-fe5f923bd914
