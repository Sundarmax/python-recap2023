# nonlocal variable
def outer_func():
    x =10
    def inner_func():
        nonlocal x
        x = x +1
        print(x)
    inner_func()
