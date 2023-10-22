class square:

    def __init__(self, side) -> None:
        self.side = side
    
    def square_area(self):
        return self.side * self.side

class cube(square):
    def __init__(self, side) -> None:
        super().__init__(side)

    def area(self):
        return super().square_area() * 6

#obj = cube(4)
#print(obj.area())

class Parent:
    def __init__(self):
        print("This is the parent class")
        
class Parent1:
    def __init__(self):
        print("This is the parent1 class")
        
class Child(Parent1, Parent):
    def __init__(self):
        ##Calling constructor of the Parent 1 class
       super(Parent1, self).__init__()

ob = Child()
