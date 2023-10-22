# abstraction -- > Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only how to use the application
# encapsulation -- >Getter ,setter [Prevent accidential modification of data ,obj values can only changed by object methods]
# inheritance -- >child class inherits the properties of parent class use super() method
# polymorphism -- >meaning having many form In programming, polymorphism means the same function name is used for different types. 

from abc import ABC,abstractmethod
class Account:
    # example for data encapsulation
    def __init__(self,id,name,pwd) -> None:
        self.id = id
        self.name = name
        self.__pwd = pwd

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self, pwd):
        # we can only modify private var by public methods only in the same  class.
        self.__pwd = pwd
obj = Account(11,'sundar','temp%')
print(obj.get_pwd())

# print(obj.__pwd) which raise attribute error.
class A:
    pass
class B(A):
    pass
a = A()

#print(issubclass(B,A),issubclass(A,B))
#print(isinstance(a,A))

class Bird:
    # example of polymorphism
    # Method overriding
    def __init__(self,name) -> None:
        self.name = name
    
    def flight(self):
        print('Some birds cannot fly')

class Sparrow(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def flight(self):
        # overriden method from the base class
        super().flight()
        print(self.name, ' can fly .. ')

# obj = Sparrow('pigeon')
# obj.flight()

# Amenity becomes our abstract base class (ABC)

class Amenity(ABC): 
    def turn_on(self):
        pass
# We extend our ABC to three new child classes
class Electricity(Amenity):    
    def turn_on(self):
        print("You flipped the light switch!")

obj = Electricity()
obj.turn_on()