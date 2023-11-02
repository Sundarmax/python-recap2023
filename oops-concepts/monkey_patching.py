class MonkeyPatch:
    def __init__(self, num):
        self.num = num

    def addition(self, other):
        return (self.num + other)
        
obj = MonkeyPatch(10)
print(obj.addition(20))

def subtraction(self, other):
    return (self.num - other)

MonkeyPatch.subtraction = subtraction

obj1 = MonkeyPatch(10)
print(obj1.subtraction(7))
