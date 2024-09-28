# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.

# my solution:
def to_alternating_case0(string):
    result= ""
    for character in string:
        if character.islower():
            result+=character.upper()
        else:
            result+=character.lower()
    return result

def to_alternating_case1(string):
    return string.swapcase()

