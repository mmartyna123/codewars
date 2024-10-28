# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

# my solution:
def count(s):
    if not s:
        return {}
    character_count = {}
    for character in s:
        character_count[character] = character_count.get(character, 0) +1
    return character_count