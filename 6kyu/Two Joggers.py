# our job is to complete the function nbrOfLaps(x, y) that, given the length of the laps for Bob and Charles, finds the number of laps that each jogger has to complete before they meet each other again, at the same time, at the start.

# The function takes two arguments:

# The length of Bob's lap (larger than 0)
# The length of Charles' lap (larger than 0)

# The function should return an array (Tuple<int, int> in C#) containing exactly two numbers:

# The first number is the number of laps that Bob has to run
# The second number is the number of laps that Charles has to run

# my solution:
import math
def nbr_of_laps(x, y):
    return (math.lcm(x,y) // x, math.lcm(x,y) // y)
