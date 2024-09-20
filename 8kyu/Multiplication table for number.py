# Your goal is to return multiplication table for number that is always an integer from 1 to 10.

# my solutions:
def multi_table0(number):
    result = []
    for i in range(1, 11):
        result.append(f'{i} * {number} = {i*number}')
    return '\n'.join(result)
    
def multi_table1(number):
    return '\n'.join(f'{i} * {number} = {i*number}' for i in range(1,11))