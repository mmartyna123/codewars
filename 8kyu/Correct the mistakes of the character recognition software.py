# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

# my solutions:
def correct(s):
    res = ''
    for i in s:
        if i == '5':
            res += 'S'
        elif i == '0':
            res += 'O'
        elif i == '1':
            res += 'I'
        else:
            res += i
    return res

def correct2(s):
    return s.replace('5', 'S').replace('1', 'I').replace('0', 'O')