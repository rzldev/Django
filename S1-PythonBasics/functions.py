## Function ##
def greet(name = 'Bob'):
    print('Hello {}!'.format(name))

greet()
greet('John')


## Function that return value
def greet(name = 'Bob'):
    return 'Hello {}!'.format(name)

greet()
print(greet())

def addNum(num1, num2):
    return num1 + num2

result = addNum(2, 3)
print(result)
result = addNum('2', '3')
print(result)

# Using type to check if the parameter is integer
def addNum(num1, num2):
    if (type(num1) == int) and (type(num2) == int):
        return num1 + num2
    else:
        return 'Sorry, i need integers!'

result = addNum(2, 3)
print(result)
result = addNum('2', '3')
print(result)


## Lambda Expression
my_list = [x for x in range(10)]

# Function
def even_bool(num):
    return num % 2 == 0

evens = list(filter(even_bool, my_list))
print(evens)

# Lambda
odds = list(filter(lambda num: num % 2 == 1, my_list))
print(odds)


## Just some exercises
def arrayCheck(nums):
    if (type(nums) == list):
        for k, x in enumerate(nums):
            if k < len(nums) - 2 and x == 1 and nums[k + 1] == 2 and nums[k + 2] == 3: return True
        return False
        # return [1, 2, 3] in nums
    else:
        return 'I need a list!'

print(arrayCheck([1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 2, 4, 3, 1]))


def stringBits(chars):
    return ''.join([char if i % 2 == 0 else '' for i, char in enumerate(chars)])

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


def end_other(char1, char2):
    return char1.lower() == char2[len(char1)].lower() or char1[len(char2)].lower() == char2.lower()

print(end_other('Hiabc', 'abc'))
print(end_other('abC', 'HiaBc'))
print(end_other('fbs', 'abXabc'))


def doubleChar(chars):
    return ''.join(list(char * 2 for char in chars))

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))


def noTeensSum(a, b, c):
    return fixTeen(a) + fixTeen(b) + fixTeen(c)

def fixTeen(n):
    return 0 if n [13, 14, 17, 18, 19] else n

print(noTeensSum(1, 2, 3))
print(noTeensSum(2, 13, 1))
print(noTeensSum(2, 1, 14))


def countEvens(nums):
    return len(list(filter(lambda num: num % 2 == 0, nums)))

print(countEvens([2, 1, 2, 3, 4]))
print(countEvens([2, 2, 0]))
print(countEvens([1, 3, 5]))