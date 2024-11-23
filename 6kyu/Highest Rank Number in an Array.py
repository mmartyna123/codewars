# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

# Note: no empty arrays will be given.

# my solution:
def highest_rank(arr):
    max_frequent = max(arr.count(i) for i in arr)
    most_frequent = [i for i in arr if arr.count(i)==max_frequent]
    return max(most_frequent)