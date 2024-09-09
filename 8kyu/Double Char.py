# Description:
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# my solution:
def double_char(s):
    ns=''
    for i in range(len(s)):
        ns+=(s[i])*2
        
    return ns
        