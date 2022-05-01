## Numbers ##
# Integer
print(2 + 10 * 10 + 3)
print((2 + 10) * (10 + 3))

a = 5
print(a)
a = a * 5
print(a)

# Float
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)



## Strings ##
print('Hello World!')
print("I'm a student")

my_string = 'Ironman'
print(my_string)
print(my_string[5])

# String Slicing
print(my_string[1:4]) 
print(my_string[3:])
print(my_string[::4])
print(my_string[:])

# String Basic Methods
my_string = 'hello world!'

my_string_upper = my_string.upper()
print(my_string_upper)
my_string_capitalize = my_string.capitalize()
print(my_string_capitalize)
my_string_split = my_string.split('l')
print(my_string_split)

# String formatting
my_string = 'Pet one: {}, Pet two: {}'.format('Cat', 'Dog')
print(my_string)
my_string = 'Pet one: {y}, Pet two: {x}'.format(x = 'Cat', y = 'Dog')
print(my_string)



## Lists ##
my_list = [1, 'Two', 3, 'Four']
print(my_list)
print(my_list[2])
print(my_list[-1])
print(len(my_list))

# Add item to the list
my_list.append(5)
print(my_list)

my_list = [1, 'Two', 3, 'Four']
my_list.append([5, 'Six', 7])
print(my_list)

my_list = [1, 'Two', 3, 'Four']
my_list.extend([5, 'Six', 7])
print(my_list)

# Change list item value
my_list[2] = 200
print(my_list)

# Remove item from list
my_list = [1, 'Two', 3, 'Four']
item = my_list.pop(2)
print(my_list)
print(item)

# Reverse the list
my_list = [1, 'Two', 3, 'Four']
my_list.reverse()
print(my_list)

# Sorting list
my_list = [1, 200, 3, 40]
my_list.sort()
print(my_list)

# Nested list (Get 4 and 5)
my_list = [[1, 2], [3, 4], [5, 6]]
print(my_list[1][1])
print(my_list[2][0])

# List Comprehension
my_list = [[1, 2, 3], [40, 50, 60], [700, 800, 900]]
first_col = [row[0] for row in my_list]
print(first_col)



## Dictionaries ##
car = {'brand': 'Lamborghini', 'name': 'Aventador', 'plate': 1234}
print(car['name'])

# Nested Dictionaries
car = {'brand': 'Lamborghini', 'name': 'Aventador', 'others': {'cars': ['Huracan', 'Urus']}}
print(car['others']['cars'][1])

# Reassign Dictionary Item
car = {'brand': 'Lamborghini', 'name': 'Aventador'}
car['name'] = 'Urus'
car['plate'] = 4567
print(car)



## Booleans ##
x = True
y = False
print('{} {}'.format(x, y))



## Tuples ## << Basically like a List but immutable
my_tuple = (1, 2, 3)
print(my_tuple[1])



## Sets ## << Unique element only
x = set()
x.add(1)
x.add(2)
x.add(2)
x.add(2)
x.add(0.1)
print(x)