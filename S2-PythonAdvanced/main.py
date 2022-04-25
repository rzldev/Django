## __name__ == '__main__' ##

from modules import mainTwo as mt

print('TOP LEVEL main.py')

mt.func()

if __name__ == '__main__':
    print('main.py being run directly')
else:
    print('main.py is being imported')