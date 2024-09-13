# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# my solution:
def tower_builder(n_floors):
    i=0
    l=[]
    width = 2 * n_floors - 1
    for i in range(n_floors):
        space = (width - (i*2 + 1)) // 2
        a = " " * space +  "*" * (i*2 + 1) + " " * space 
        l.append(a)
        
    return l
    