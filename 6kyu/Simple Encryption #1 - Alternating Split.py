# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.


# my solution:
def decrypt(encrypted_text, n):
    if not encrypted_text or n<=0:
        return encrypted_text
    length = len(encrypted_text)
    for iteration in range(n):
        half_len = length//2
        even_characters = encrypted_text[half_len:]
        odd_characters = encrypted_text[:half_len]
        encrypted_text = ''.join(even_characters[i:i+1] + odd_characters[i:i+1] for i in range(half_len))
        if len(even_characters) > len(odd_characters):
            encrypted_text += even_characters[half_len:]
    return encrypted_text


def encrypt(text, n):
    if not text or n<=0:
        return text
    for iteration in range(n):
        even_characters = text[0::2]
        odd_characters = text[1::2]
        text = odd_characters + even_characters
    return text
