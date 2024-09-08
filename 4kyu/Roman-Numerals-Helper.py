# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

# 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
# 2008 is written as 2000=MM, 8=VIII; or MMVIII
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
#   86 -> "LXXXVI"
#    1 -> "I"

# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "LXXXVI"  ->   86
# "I"       ->    1

# my solution:
class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        M = ['','M', 'MM', 'MMM']
        C= ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X= ['', 'X', 'XX', 'XXX',  'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        
        thousands = M[val//1000]
        hundreds = C[(val%1000)//100]
        tens = X[(val%100)//10]
        ones = I[val%10]
        return thousands + hundreds + tens + ones

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_western={
            'I':1,  'V':5,
            'X':10, 'L':50,
            'C':100, 'D':500,
            'M':1000
        }
        
        western_num=0
        previous_num = 0
        for letter in roman_num:
            current_num = roman_western[letter]
            if current_num > previous_num:
                western_num += current_num - 2*previous_num
            else: western_num += current_num
            previous_num = current_num
        return western_num