import random
from tokenize import Number

match = {'finish': 0, 'match': 1, 'close': 2, 'none': 3}

def startGame():
    code = list(random.randint(1, 9) for _ in range(3))

    status = match['none']
    
    while (status != match['finish']):
        numbers = input('Enter 3 digits number: ')

        ## Cheat
        if (int(numbers) == 000): print('{} {}'.format(code, [int(num) for num in numbers]))

        if (len(numbers) == 3 and type(numbers) == str):
            status =  matching(code, [int(num) for num in numbers])
            print(statusText(status))
        else:
            print('Invalid input!')

def matching(code, input):
    status = match['none']

    if code == input: return match['finish']

    for i in range(3):
        if input[i] in code: 
            status = match['close']
        if input[i] == code[i]: 
            status = match['match']
            break

    return status

def statusText(status):
    if status == match['finish']:
        return 'The answer is correct!!!'
    if status == match['match']:
        return 'Something match!!!'
    if status == match['close']:
        return 'Close! Don\'t give up!'
    if status == match['none']:
        return 'Sorry, nothing close.'

if __name__ == '__main__':
    startGame()