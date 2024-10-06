# If we write out the digits of "60" as English words we get "sixzero"; the number of letters in "sixzero" is seven. The number of letters in "seven" is five. The number of letters in "five" is four. The number of letters in "four" is four: we have reached a stable equilibrium.

# Note: for integers larger than 9, write out the names of each digit in a single word (instead of the proper name of the number in English). For example, write 12 as "onetwo" (instead of twelve), and 999 as "nineninenine" (instead of nine hundred and ninety-nine).

# For any integer between 0 and 999, return an array showing the path from that integer to a stable equilibrium:

# Examples
# numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]
# numbersOfLetters(1) --> ["one", "three", "five", "four"]

# my solution:
def numbers_of_letters(n):
    digits_to_words = {
        0:'zero', 1:'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
        8:'eight', 9:'nine'
    }
    res = []
    def number_to_word(number):
        return ''.join(digits_to_words[int(digit)] for digit in str(number))
    word = number_to_word(n)
    while True:
        res.append(word)
        word_length = len(word)
        new_word = number_to_word(word_length)
        if new_word == word:
            break
        else:
            word = new_word
    return res
    