# Your task is to write a function which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

# Examples

# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)

# my solutions:
def sequence_sum0(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step)) if begin_number <= end_number else 0

def sequence_sum1(begin_number, end_number, step):
    if begin_number > end_number and step > 0 or begin_number < end_number and step < 0:
        return 0
    n = (end_number - begin_number) // step + 1
    last_number = begin_number + (n-1)*step
    return n*(begin_number + last_number) //2