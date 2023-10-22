
# https://www.geeksforgeeks.org/class-method-vs-static-method-python/

class CALC:
    def __init__(self,access=None) -> None:
        self.user_access = "allowed"

    @staticmethod
    def get_max(x,y):
        return max(x,y)
    
    @classmethod
    def set_useraccess(cls,access=None):
        return cls("blocked")

# print(CALC.get_max(11,13))

# obj = CALC()
# print(obj.user_access)
# CALC.set_useraccess()
# print(obj.user_access)

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)
print(person1.age)
# print the result
print(Person.isAdult(22))
