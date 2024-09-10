# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.
# my solutions:
def sum_mix(arr):
    s=0
    for i in arr:
        s += int(i)
    return s

def sum_mix2(arr):
    return sum (int(i) for i in arr)