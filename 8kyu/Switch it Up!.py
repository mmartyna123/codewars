# When provided with a number between 0-9, return it in words.

# Input :: 1

# Output :: "One".

# my solutions:
def switch_it_up0(number):
    numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return numbers[number]

def switch_it_up1(number):
    numbers = { 0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 
               6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
    return numbers[number]