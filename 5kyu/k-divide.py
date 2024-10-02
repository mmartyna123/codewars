# You are given a positive integer N and an integer K > 1.

# For each integer from 1 to N, repeat the following operation:

# Divide the integer by K
# If the number is divisible, divide by K, and repeat
# Otherwise, end the operation.
# Let f(n) be the integer after the operation. For example, if n = 12 and K = 3, then f(12) = 4(12→4).

# Find the sum of all f(n) from 1 to N.

# Input
# You be given:
# N K
# Constraints
# The test cases are in the range

# 1≤N≤10**18
# 2≤K≤10**12

# Examples
# Let's try testing N=10 and K=4.

# f(1)=1
# f(2)=2
# f(3)=3
# f(4)=1
# f(5)=5
# f(6)=6
# f(7)=7
# f(8)=2
# f(9)=9
# f(10)=10
# So, 1+2+3+1+5+6+7+2+9+10=46

# my solution:
# they might need optimization in the future
def calculate_sum0(N, K):
    sum = 0      
    for number in range(1,N+1):
        while number % K ==0:
            quotient, remainder = divmod(number, K)
            number = quotient
        sum += number     
    return sum

def calculate_sum1(N, K):
    sum = 0     
    for number in range(1,N+1):
        while number % K ==0:
            number //= K
        sum += number     
    return sum

# The optimized solution:
def calculate_sum(N, K):
    sum = 0     
    while N > 0:
        sum += N * (N+1) //2
        N //= K
        sum -= K * N * (N+1) //2
    return sum
