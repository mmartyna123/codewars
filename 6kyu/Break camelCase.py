# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# my solutions:
def solution0(s):
    return ''.join(' ' + character if character.isupper() else character for character in s)

import re
def solution1(s):
    return re.sub(r'([A-Z])', r' \1', s)
