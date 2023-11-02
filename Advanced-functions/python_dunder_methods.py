from typing import Any

class lengthcheck:

    def __len__(self):
        return 1

obj = lengthcheck()
# print(len(obj))

class Person:
    '''
    On a high level, __str__ is used for creating output for end user while __repr__ is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable.
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Person: {}, Age: {}".format(self.name, self.age)
    
    def __repr__(self):
        print('inside repr')
        return " Person: {}, Age: {}".format(self.name, self.age)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('Call method is called')

person = Person('Sundar','26')
person
print(person) # if we don't use str method then the result will be like this : <__main__.Person object at 0x7f027b0df860>
person()