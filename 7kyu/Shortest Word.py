# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# my solution:
def find_short(s):
    return min(len(i) for i in  s.split(" "))