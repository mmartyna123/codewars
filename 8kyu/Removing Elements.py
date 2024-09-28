# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# my solutions:
def remove_every_other0(my_list):
    new_list=[]
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(my_list[i])
    return new_list
        
def remove_every_other1(my_list):
    return my_list[::2]
