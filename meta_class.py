''''
The purpose of metaclasses isn’t to replace the class/object distinction with metaclass/class - 
it’s to change the behavior of class definitions (and thus their instances) in some way
'''

class MyMeta(type):
    def __new__(self,name,bases, atts):
        print(f'current attributes : {atts}')
        new_atts = {}
        for key,value in atts.items():
            if '__' in key:
                new_atts[key] = value
            else:
                new_atts[key.upper()] = value
        print(f'Modified attributes : {new_atts}')


class Sample(metaclass=MyMeta):
    x = 'bob'
    y = 24

    def say_hi(self):
        print('hii')
