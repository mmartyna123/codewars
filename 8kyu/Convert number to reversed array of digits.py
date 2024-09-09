# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# my solution:
def digitize(n):
    return list(map(int, str(n)))[::-1]