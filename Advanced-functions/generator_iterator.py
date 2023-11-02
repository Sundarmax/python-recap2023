# generator
def generate_number():
    for i in range(1,5):
        yield i

obj = generate_number()
print(next(obj))
print(next(obj))
print(next(obj))

# iterator
iter_list = iter([1,2,3])
print(next(iter_list))
print(next(iter_list))