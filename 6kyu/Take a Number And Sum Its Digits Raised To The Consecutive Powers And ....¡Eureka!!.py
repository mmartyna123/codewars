# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 
# 89=8**1+9 ** 2
# The next number in having this property is 135:

# See this property again: 
# 135
# =
# 1
# 1
# +
# 3
# 2
# +
# 5
# 3
# 135=1 ** 1+3 **2+5 **3
 
# Task
# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

# my solution:
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    eureka = []
    for number in range(a,b+1):
        sum_of_powered = sum(int(digit) ** (i+1) for i, digit in enumerate(str(number)))
        if sum_of_powered == number:
            eureka.append(number)
    return eureka