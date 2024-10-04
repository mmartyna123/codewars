# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

# my solution:
def encrypt_this(text):
    ans = []
    for word in text.split():
        if len(word) == 1:
            ans.append(str(ord(word[0])))
        elif len(word) == 2:
            ans.append(str(ord(word[0])) + word[1])
        else:
            ans.append(str(ord(word[0])) + word[-1] + word[2:-1] + word[1])
    return ' '.join(ans)
        