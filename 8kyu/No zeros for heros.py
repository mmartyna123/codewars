# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# m solution:
def no_boring_zeros(n):
    return n if n==0 else int(str(n).rstrip('0'))