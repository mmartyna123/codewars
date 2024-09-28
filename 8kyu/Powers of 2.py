# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

# my solution:
def powers_of_two(n):
    list_of_powers = []
    for i in range(n+1):
        list_of_powers.append(2**i)
    return list_of_powers