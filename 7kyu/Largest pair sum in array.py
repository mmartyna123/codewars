# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)

# my solution:
def largest_pair_sum(numbers): 
    numbers = sorted(numbers)
    return numbers[-1]+numbers[-2]