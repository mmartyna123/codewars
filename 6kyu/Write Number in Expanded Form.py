# Description:
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# my solution 
def expanded_form(num):
    ts=[]
    num=str(num)
    for i, digit in enumerate(num):
        if int(digit) != 0:
            an= int(digit) * 10**(len(num)-i-1)
            ts.append(str(an))
    return " + ".join(ts)