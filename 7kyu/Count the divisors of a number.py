# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000, but fixed tests go higher.

# my solutions:
# first approach
def divisors(n):
    count = 0
    for i in range (1, n+1):
        if n % i == 0:
            count += 1
    return count
# second approach def divisors(n):
def divisors(n):
    return sum( n % i == 0 for i in range(1, n+1))