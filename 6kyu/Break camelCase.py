# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# my solution:
def solution(s):
    return ''.join(' ' + character if character.isupper() else character for character in s)