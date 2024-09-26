# The task is simple to explain: simply sum all the numbers from the first parameter being the beginning to the second parameter being the upper limit (possibly included), going in steps expressed by the third parameter:

# sequence_sum(2, 2, 2) # 2
# sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
# sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
# sequence_sum(1, 5, 3) # 5 (= 1 + 4)
# If it is an impossible sequence (with the beginning being larger the end and a positive step or the other way around), just return 0. See the provided test cases for further examples :)

# my solution:
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number and step > 0 or begin_number < end_number and step < 0:
        return 0
    n = (end_number - begin_number) // step + 1
    last_number = begin_number + (n-1)*step
    return n*(begin_number + last_number) //2