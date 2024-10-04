# We all know about Roman Numerals, and if not, here's a nice introduction kata. And if you were anything like me, you 'knew' that the numerals were not used for zeroes or fractions; but not so!

# I learned something new today: the Romans did use fractions and there was even a glyph used to indicate zero.

# So in this kata, we will be implementing Roman numerals and fractions.

# Although the Romans used base 10 for their counting of units, they used base 12 for their fractions. The system used dots to represent twelfths, and an S to represent a half like so:

# 1/12 = .
# 2/12 = :
# 3/12 = :.
# 4/12 = ::
# 5/12 = :.:
# 6/12 = S
# 7/12 = S.
# 8/12 = S:
# 9/12 = S:.
# 10/12 = S::
# 11/12 = S:.:
# 12/12 = I (as usual)
# Further, zero was represented by N

# Kata
# Complete the method that takes two parameters: an integer component in the range 0 to 5000 inclusive, and an optional fractional component in the range 0 to 11 inclusive.

# You must return a string with the encoded value. Any input values outside the ranges given above should return "NaR" (i.e. "Not a Roman" :-)

# Examples
# roman_fractions(-12)     #=> "NaR"
# roman_fractions(0, -1)   #=> "NaR"
# roman_fractions(0, 12)   #=> "NaR"
# roman_fractions(0)       #=> "N"
# roman_fractions(0, 3)    #=> ":."
# roman_fractions(1)       #=> "I"
# roman_fractions(1, 0)    #=> "I"
# roman_fractions(1, 5)    #=> "I:.:"
# roman_fractions(1, 9)    #=> "IS:."
# roman_fractions(1632, 2) #=> "MDCXXXII:"
# roman_fractions(5000)    #=> "MMMMM"
# roman_fractions(5001)    #=> "NaR"

# my solution:
def roman_fractions(integer, fraction=None):
        M = ['','M', 'MM', 'MMM', 'MMMM', 'MMMMM']
        C= ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X= ['', 'X', 'XX', 'XXX',  'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        fr = ['','.', ':', ':.', '::', ':.:', 'S', 'S.', 'S:', 'S:.', 'S::', 'S:.:']
        
        if not (0 <= integer <= 5000) or (fraction is not None and not (0 <= fraction <= 11)):
            return 'NaR'
        if integer == 0 and (fraction is None or fraction == 0):
            return 'N'
        if fraction is None:
            fraction = 0
        
        thousands = M[integer//1000]
        hundreds = C[(integer%1000)//100]
        tens = X[(integer%100)//10]
        ones = I[integer%10]
        frac = fr[fraction]
        return thousands + hundreds + tens + ones + frac
    
        