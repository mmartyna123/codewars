# We want to generate a function that computes the series starting from 0 and ending until the given number.

# Example:
# Input:

# > 6
# Output:

# 0+1+2+3+4+5+6 = 21

# Input:

# > -15
# Output:

# -15<0

# Input:

# > 0
# Output:

# 0=0

# my solution:
def show_sequence(n):
    if n <0:
        return f'{n}<0'
    elif n == 0:
        return '0=0'
    else:
        series = '+'.join(map(str, range(n+1)))
        S = sum(range(n+1))
        return f'{series} = {S}'