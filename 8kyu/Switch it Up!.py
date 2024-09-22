# When provided with a number between 0-9, return it in words.

# Input :: 1

# Output :: "One".

# my solution:
def switch_it_up(number):
    numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return numbers[number]