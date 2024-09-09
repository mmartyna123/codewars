# Write a function that checks if a given string (case insensitive) is a palindrome.

# my solutions:
def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def is_palindrome2(s):
    for i in range (int(len(s)/2)):
        if s[i].lower() != s[len(s)-i -1].lower():
            return False
    return True
