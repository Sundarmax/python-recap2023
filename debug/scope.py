# list the scope .

x = 100 
def foo():
    x = 50
    print(x)
    print(locals())
    print(globals().get('x'))
foo()