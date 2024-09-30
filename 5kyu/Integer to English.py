# For a given positive integer convert it into its English representation. All words are lower case and are separated with one space. No trailing spaces are allowed.

# To keep it simple, hyphens and the writing of the word 'and' both aren't enforced. (But if you are looking for some extra challenge, such an output will pass the tests.)

# Large number reference: http://en.wikipedia.org/wiki/Names_of_large_numbers (U.S., Canada and modern British)

# Input range: 1 -> 10**26
# Examples:

# int_to_english(1) == 'one'

# int_to_english(10) == 'ten'

# int_to_english(25161045656) == 'twenty five billion one hundred sixty one million forty five thousand six hundred fifty six'

# my solution:

def int_to_english(n):
    numbers = {
        0:'zero', 1:'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
        8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14: 'fourteen',
        15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
        30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
    }
    def two_digits(n):
        if n <= 20:
            return numbers[n]
        else:
            tens, ones = divmod(n,10)
            return numbers[tens*10] + ('' if ones==0 else ' '+ numbers[ones])
    def three_digits(n):
        hundreds, tens = divmod(n,100)
        if hundreds == 0:
            return two_digits(tens)
        else:
            return numbers[hundreds] + ' hundred' + ('' if tens==0 else ' ' + two_digits(tens))
        
    def large_numbers(n): 
        if n < 10**3 : 
            return three_digits(n)
        elif n < 10**6:
            thousands, hundreds = divmod(n, 1000)
            return three_digits(thousands) + ' thousand' +  ('' if hundreds == 0 else ' ' +  three_digits(hundreds))
        elif n < 10**9:
            millions, thousands = divmod(n, 10**6)
            return three_digits(millions) + ' million' + ('' if thousands == 0 else ' ' +  large_numbers(thousands))
        elif n < 10**12: 
            billions,  millions = divmod(n, 10**9)
            return three_digits(billions) + ' billion' + (''  if millions == 0 else ' ' +  large_numbers(millions))
        elif n < 10**15:
            trillions, billions = divmod(n, 10**12 )
            return three_digits(trillions) + ' trillion' +  (''  if  billions == 0 else ' ' + large_numbers(billions))
        elif n < 10**18:
            quadrillions, trillions = divmod(n, 10**15)
            return three_digits(quadrillions) + ' quadrillion' + ('' if  trillions == 0 else ' '  + large_numbers(trillions))
        elif n < 10**21:
            quintillions, quadrillions = divmod(n,  10**18)
            return three_digits(quintillions) + ' quintillion' + ('' if  quadrillions == 0 else ' ' + large_numbers(quadrillions))
        elif n < 10**24:
            sextillions, quintillions = divmod(n, 10**21)
            return three_digits(sextillions) +  ' sextillion' + ('' if quintillions == 0 else ' ' +  large_numbers(quintillions))
        else:  
            septillions, sextillions = divmod(n, 10**24 )
            return  three_digits(septillions) + ' septillion' + ('' if  sextillions == 0 else ' ' + large_numbers(sextillions))

    return large_numbers(n)