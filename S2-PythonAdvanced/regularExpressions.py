## Regular Expressions ##
import re

## Example of using RE
patterns = ['term1', 'term2']

text = 'This is a astring with term1, and not the other!'

for pattern in patterns:
    print('I\'m searching for: ' + pattern)

    if re.search(pattern, text):
        print('MATCH')
    else:
        print('NO MATCH')


## Using re.search(pattern, phrase)
match = re.search('term1', text)
print(match.start())    # term1 start on the 23th char

## Using re.split(pattern, phrase)
print(re.split('@', 'testing@gmail.com'))

## Using re.findall()
print(re.findall('match', 'Find a match phrase in the middle of the text'))

## Meta characters syntax
# Metacharacters:
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)

text_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
patterns = ['sd*', 'sd+', 'sd?', 's[sd]+']

# Find an s followed by 0 or more d
print(re.findall(patterns[0], text_phrase))

# Find an s followed by 1 or more d
print(re.findall(patterns[1], text_phrase))

# Find an s followed by 0 or 1 time d
print(re.findall(patterns[2], text_phrase))

# Find an s followed by n d
print(re.findall('sd{3}', text_phrase))
print(re.findall('sd{1,3}', text_phrase))

# Find an s followed 1 or more s or 1 or more d
print(re.findall(patterns[3], text_phrase))


text_phrase = 'This is a string! But it has punctuation. How can we remove it? Can this numbers 1242937 help?'

# Exclusion
patterns = ['[^!.?]+', '[a-z]+', '[A-Z]+']
print(re.findall(patterns[0], text_phrase))

# Find lowercase character
print(re.findall(patterns[1], text_phrase))

# Find uppercase character
print(re.findall(patterns[2], text_phrase))

# Find digits or numbers
print(re.findall(r'\d+', text_phrase))

# Find non-digit characters
print(re.findall(r'\D+', text_phrase))

# Find whitespace
print(re.findall(r'\s+', text_phrase))

# Find non-whitespace
print(re.findall(r'\S+', text_phrase))

# Find word characters
print(re.findall(r'\w+', text_phrase))

# Find non-word characters
print(re.findall(r'\W+', text_phrase))