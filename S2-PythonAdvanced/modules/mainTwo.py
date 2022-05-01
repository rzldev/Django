def func():
    print('func() in mainTwo.py file')

print('TOP LEVEL mainTwo.py')

if __name__ == '__main__':
    print('mainTwo.py is being run directly')
else:
    print('mainTwo.py has been imported')