# Your goal is to return multiplication table for number that is always an integer from 1 to 10.

# my solution:
def multi_table(number):
    result = []
    for i in range(1, 11):
        result.append(f'{i} * {number} = {i*number}')
    return '\n'.join(result)
    