# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

# my solution:
def sum_pairs(ints, s):
    seen = set()
    for number in ints:
        looking_for = s - number
        if looking_for in seen:
            return [looking_for, number]
        seen.add(number)
    return None
        