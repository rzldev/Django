## Scopes ##

# LEGB
# L: Local -> Names assigned in any way within a function (def or lambda),
#   and not decalred global in that function.
# E: Enclosing -> Name in the local scope of any and all enclosing functions
#   (def and lambda), from inner to outer.
# G: Global (module) -> Names assigned at the top-level of a module file,
#   or declared global in a def within the file.
# B: Built-in (Python) -> Names preassigned in the builtin names module: open, range, SyntaxError, ....

x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
my_func()
print(x)

## Local
lambda x: x ** 2
# The x is a local variable


## Global
name = 'This is a global name!'

def greet():
    ## Enclosing
    name = 'Sammy'

    def hello():
        print('Hello {}!'.format(name))

    hello()

greet()
print(name)


## Reassign global variable inside function
i = 100

def func():
    global i
    i = -1

print('Before function call, i is {}'.format(i))
func()
print('After function call, i is {}'.format(i))