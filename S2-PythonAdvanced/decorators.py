## Decorators ##

g = 'This is a global variable!'

def global_func():
    # global g
    # g = 'Global'
    print(globals())
    print('globals()[\'g\']: {}'.format(globals()['g']))
    return g

def local_func():
    g = 'Local'
    print(locals())
    return g

print(global_func())
print(local_func())


print()
## Returning function
def hello(name='Bob'):
    print('THE HELLO() FUNCTION HAS BEEN RUN!')

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return 'THIS STRING IS INSIDE WELCOME()'

    # print(greet())
    # print(welcome())
    # print("End of hello()")

    if name == 'Bob':
        return greet
    else:
        return welcome

h = hello()
print(h())

def hi():
    return 'Hi Bob!'

def execute(func):
    print(func())

execute(hi)


## Decorator
def new_decorator(func):
    def wrap_func():
        print()
        print('CODE HERE BEFORE EXECUTING FUNC')
        func()
        print('FUNC() HAS BEEN CALLED')

    return wrap_func

def func_needs_decorator():
    print('THIS FUNCTION IS IN NEED OF DECORATOR!')

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

@new_decorator
def simple_way():
    print('THIS FUNCTION IS ALSO IN NEED OF DECORATOR!')

simple_way()