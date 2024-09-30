# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# my solutions:
def array_diff0(a, b):
    res=[]
    for element in a:
        if element not in b:
            res.append(element)
    return res

def array_diff1(a, b):
    return [element for element in a if element not in b]