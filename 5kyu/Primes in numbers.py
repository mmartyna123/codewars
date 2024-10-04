# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

# my solution:
def prime_factors(n):
    factors = {}
    current_divisor = 2
    res = ''
    while n > 1:
        while n % current_divisor == 0:
            if current_divisor in factors:
                factors[current_divisor] += 1
            else:
                factors[current_divisor] = 1
            n //= current_divisor
        current_divisor += 1
    for divisor in sorted(factors):
        exponent = factors[divisor]
        if exponent == 1:
            res += f'({divisor})'
        else:
            res += f'({divisor}**{exponent})'
    return res