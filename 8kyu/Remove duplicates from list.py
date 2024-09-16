# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.

# Examples:

# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

# my solution:
def distinct(seq):
    result = []
    [result.append(el) for el in seq if el not in result]
    return result