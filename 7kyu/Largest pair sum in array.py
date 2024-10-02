# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)

# my solutions:
def largest_pair_sum0(numbers): 
    numbers = sorted(numbers)
    return numbers[-1]+numbers[-2]

def largest_pair_sum1(numbers): 
    largest = second_largest = float('-inf')
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return largest+second_largest