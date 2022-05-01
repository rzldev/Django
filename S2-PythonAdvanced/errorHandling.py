## Error Handling ##

# try -> A block that lets you test your code for errors.
# except -> A block that lets you handler the error.
# else -> A block that lets you execute code when there is no error.
# finally -> A block that lets you execute code regardless there is error or not.

## Example of error handling
try:
    print(my_string)    # will throw an error because my_string is never defined #
except NameError:
    print('ERROR: THERE IS SOMETHING WRONG WITH YOUR PYTHON VARIABLE')


## If you don't actually know what kin of error that you're going to handle,
#   you can empty the error type.
try:
    print(my_string)    # will throw an error because my_string is never defined #
except:
    print('ERROR: THERE IS SOMETHING WRONG WITH YOUR PYTHON VARIABLE')

## Using else statement to excute block of code id there is no error
try:
    my_string = [1, 2, 3]
    print(my_string)
except:
    print('ERROR: THERE IS SOMETHING WRONG WITH YOUR PYTHON VARIABLE')
else:
    print('SUCCESS: NO ERROR FOUND.')

## Using finally statement to execute block of code regardless there is an error or not.
try:
    print(list_of_my_string_that_never_defined)     # will throw an error because list_of_my_string_that_never_defined is never defined #
except:
    print('ERROR: THERE IS SOMETHING WRONG WITH YOUR PYTHON VARIABLE')
finally:
    print('WARNING: I DON\'T ACTUALLY KNOW IF THERE IS AN ERROR OR NOT')