# Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

# For example:

# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# # should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

# my solution:
def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if type(original) == type(other) == list:
        if len(original) != len(other):
            return False
        
        for el1, el2 in zip(original,other):
            if type(el1) == type(el2) == list:
                if not same_structure_as(el1,el2):
                    return False
            elif type(el1) == list or type(el2) == list :
                return False
    return True