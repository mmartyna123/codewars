# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

# my solutions:
def solve0(s):
    upper_count = sum(1 for character in s if character.isupper())
    lower_count = sum(1 for character in s if character.islower())
    return s.lower() if lower_count >= upper_count else s.upper()

def solve1(s):
    upper_count, lower_count = 0, 0
    for character in s:
        if character.isupper():
            upper_count += 1
        else:
            lower_count += 1
    return s.lower() if lower_count >= upper_count else s.upper()