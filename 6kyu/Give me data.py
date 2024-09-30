# In this kata, your task is to write a function which will determine whether the user has or does not have the permission to download certain data.

# Data: movies, games, books.
# Info about user's permissions is stored in a database with the following form: "movies_allow", "games_deny" ..

# When user wants to download a game and the db contains "games_deny", your function should return False.

# The user can also have everything allowed or denied: "*_allow", "*_deny".

# You can also have everything denied and some data allowed: "*_deny", "movies_allow".

# Count on incorrectness of permissions: user can have same data allowed and denied e.g.: "books_allow", "books_deny" - which results in "books_deny".

# hint: specific data has a higher priority than "*", so watch out for cases like: "*_allow", "books_deny" - in this case, the user can download everything apart from books.

# Example:

# { "books_allow", "movies_deny" }, "movies"  =>  False
# { "books_allow", "movies_deny" }, "books"  =>  True
# { "*_allow", "books_allow", "movies_deny" }, "games"  =>  True
# { "*_allow", "*_deny" }, "movies"  =>  False

# my solutions:
def has_permission0(user_info, accessing_data):
    res = False
    if '*_allow' in user_info:
        res = True
    if '*_deny' in user_info:
        res = False
    if f'{accessing_data}_allow' in user_info:
        res = True
    if f'{accessing_data}_deny' in user_info:
        res = False
    return res

def has_permission1(user_info, accessing_data):
    if f'{accessing_data}_deny' in user_info:
        return False
    if f'{accessing_data}_allow' in user_info:
        return True
    if '*_deny' in user_info:
        return False
    if '*_allow' in user_info:
        return  True
    return False