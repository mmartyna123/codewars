
# Description:
# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

# Write a function that computes the nth smallest Hamming number.

# Specifically:

# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in the Example test fixture.

# Your code should be able to compute the first 5 000 ( LC: 400, Clojure: 2 000, Haskell: 12 691, NASM, C, D, C++, Go and Rust: 13 282 ) Hamming numbers without timing out.


# MY SOLUTION:
def hamming(n):
    hamming_numbers=[1] * n
    x, y, z = 2, 3, 5
    i = j = k = 0
    for el in range(1, n):
        hamming_numbers[el]= min(x,y,z)
        if hamming_numbers[el] == x:
            i +=1
            x = hamming_numbers[i] * 2
            
        if hamming_numbers[el] == y:
            j +=1
            y = hamming_numbers[j] * 3
            
        if hamming_numbers[el] == z:
            k+= 1
            z = hamming_numbers[k] * 5
            
    return hamming_numbers[-1]