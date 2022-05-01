## Control Flow ##
print('1 < 2 is {}'.format(1 < 2))
print('1 > 2 is {}'.format(1 > 2))
print('1 >= 1 is {}'.format(1 >= 1))
print('1 <= 4 is {}'.format(1 <= 4))
print('1 == 1 is {}'.format(1 == 1))
print('1 == \'1\' is {}'.format(1 == '1'))
print('\'hi\' == \'bye\' is {}'.format('hi' == 'bye'))
print('1 != 2 is {}'.format(1 != 2))
print('(1 > 2) and (2 < 3) is {}'.format((1 > 2) and (2 < 3)))
print('(1 > 2) or (2 < 3) is {}'.format((1 > 2) or (2 < 3)))
print('(1 == 2) or (2 == 3) or (4 == 4) is {}'.format((1 == 2) or (2 == 3) or (4 == 4)))
print('\'x\' in [1, 2, 3 is {}]'.format('x' in [1, 2, 3]))


## Using if statement
if (1 < 2):
    print('1 is less than 2!')

# Nested if statement
if (1 < 2):
    print('1 is less than 2!')

    if (-1 < 2):
        print('-1 is also less than 2!')


## Using if else statement
name = 'Bob'
if (name == 'Bob'):
    print('Hello Bob!')
else:
    print('Sorry i don\'t know you')


## Using elif statement
name = 'Bob'
if (name == 'John'):
    print('Hello John!')
elif (name == 'Bob'):
    print('How are you Bob?')
else:
    print('Sorry i don\'t know you')


## Using for loops statement
my_seq = [x for x in range(20)]
for item in my_seq:
    if item % 5 == 0: print(item)

my_dictionary = {'name': 'Bob', 'age': 24}
for k in my_dictionary:
    print('{}: {}'.format(k, my_dictionary[k]))

tuple_list = [(1, 2), (3, 4), (5, 6)]
for (tup1, tup2) in tuple_list:
    print('{} {}'.format(tup2, tup1))


## Using while loops statement
i = 1
while i < 5:
    print(i + 20)
    i += 1


## Using range statement
print(list(range(5)))
print(list(range(2, 4)))


## List comprehension
input = [1, 2, 3, 4]
output = []

for num in input:
    output.append(num ** 2)

print(output)

print([x ** 2 for x in input])