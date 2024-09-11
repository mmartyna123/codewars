# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# my solution:
def reverse_words(text):
    text = text.split(' ')
    nt=[]
    for i in text:
        i = i[::-1]
        nt.append(i)
    return ' '.join(nt)