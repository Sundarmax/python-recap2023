
# multiple inheritance 
class A:
    def display(self):
        print('cLASS A method is called ')

class B(A):
    def display(self):
        print('Class B method is called')

class C(A):
    def display(self):
        print('Class C method is called')

class D(B,C):
    pass

obj = D()
obj.display()
print(D.__mro__)