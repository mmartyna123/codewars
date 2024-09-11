# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# my solution:
def grow(arr):
    x=1
    for n  in range (len(arr)):
        x = x * arr[n]
    return x