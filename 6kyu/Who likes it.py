# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

# my solution:
def likes(names):
    if len(names) == 0:
        ppl = "no one likes"
    elif len(names) == 1:
        ppl = f"{names[0]} likes"
    elif len(names) <=3:
        ppl = f"{', '.join(names[:-1])} and {names[-1]} like"  
    else:
        ppl = f"{', '.join(names[0:2])} and {len(names)- 2} others like"
    return f"{ppl} this"