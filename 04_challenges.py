from test_api.checks import Check, SkipCheck

# Exercise 0
# Write a function, check_if_key_exists, that takes a dictionary and a key as
#  its arguments
# It should return True if the dictionary contains the provided key,
#  False otherwise


# Define function here...


Check(check_if_key_exists, "Test if key exists").when_called_with(
    {"name": "jonny", "age": 32}, "name"
).returns(True)

Check(check_if_key_exists, "Test if key exists").when_called_with(
    {"name": "jonny", "age": 32}, "age"
).returns(True)

Check(check_if_key_exists, "Test if key exists").when_called_with(
    {"name": "jonny", "age": 32}, "pets"
).returns(False)

# Exercise 1
# Write a function, create_dict, that takes a list consisting of two elements
#  representing a key / value pair as its argument
# It should return a dictionary with a single key based on the input

# Define function here...


SkipCheck(create_dict, "Create dictionary").when_called_with(
    ["name", "shaq"]
).returns({"name": "shaq"})

SkipCheck(create_dict, "Create dictionary").when_called_with(
    ["fruit", "apple"]
).returns({"fruit": "apple"})

SkipCheck(create_dict, "Create dictionary").when_called_with(
    ["language", "haskell"]
).returns({"language": "haskell"})


# Exercise 2
# Write a function, get_first_n_items, that takes two arguments, a list and
#  a number 'n'
# It should return a new list containing the first 'n' items of the given list

# Define function here...


SkipCheck(get_first_n_items, "Get first n items").when_called_with(
    ["a", "b", "c", "d"], 2
).returns(["a", "b"])

SkipCheck(get_first_n_items, "Get first n items").when_called_with(
    ["apple", "banana", "pear", "kiwi"], 0
).returns([])

SkipCheck(get_first_n_items, "Get first n items").when_called_with(
    ["apple", "banana", "pear", "kiwi"], 3
).returns(["apple", "banana", "pear"])


# Exercise 3
# Write a function, create_arrow, that takes a string representing a
#  direction ("left", "right", "up" or "down") as its argument
# It should return the corresponding arrow ("←", "→", "↑", "↓")
# You don't need to utilise an dictionary here, but think about how you
#  could do so

# Define function here...


SkipCheck(create_arrow, "Create arrow").when_called_with("left").returns("←")

SkipCheck(create_arrow, "Create arrow").when_called_with("right").returns("→")

SkipCheck(create_arrow, "Create arrow").when_called_with("up").returns("↑")

SkipCheck(create_arrow, "Create arrow").when_called_with("down").returns("↓")


# Exercise 4
# Write a function, move_item_to_end, that takes two arguments, a list and an
#  index value
# It should return a new list where the item that was previously at the
#  given index is now at the end of the list

# Define function here...


SkipCheck(move_item_to_end, "Move item to end").when_called_with(
    ["a", "b", "c"], 0
).returns(["b", "c", "a"])

SkipCheck(move_item_to_end, "Move item to end").when_called_with(
    ["a", "b", "c", "d"], 2
).returns(["a", "b", "d", "c"])

SkipCheck(move_item_to_end, "Move item to end").when_called_with(
    ["a", "b", "c", "d"], 1
).returns(["a", "c", "d", "b"])


# Exercise 5
# Write a function, update_user_age, that takes a dictionary representing a
#  user's account information
# A user object will look
# {
#       "admin": False,
#       "username": "xoxoAlexoxo",
#       "personal_details": {
#           "name": "Alex",
#           "age": 39,
#           "fav_food": "gooseberry fool"
#       },
# }
# The user's age should be increased by 1 to reflect their recent birthday
# NOTE: This function does NOT need to return anything!

# Define function here...


SkipCheck(update_user_age, "Update user age").when_called_with(
    {
        "admin": False,
        "username": "xoxoAlexoxo",
        "personal_details": {
            "name": "Alex",
            "age": 39,
            "fav_food": "gooseberry fool",
        },
    }
).mutates_input(
    {
        "admin": False,
        "username": "xoxoAlexoxo",
        "personal_details": {
            "name": "Alex",
            "age": 40,
            "fav_food": "gooseberry fool",
        },
    }
)

SkipCheck(update_user_age, "Update user age").when_called_with(
    {
        "admin": True,
        "username": "brum4life",
        "personal_details": {
            "name": "Poonam",
            "age": 19,
            "fav_food": "caviar",
        },
    }
).mutates_input(
    {
        "admin": True,
        "username": "brum4life",
        "personal_details": {
            "name": "Poonam",
            "age": 20,
            "fav_food": "caviar",
        },
    }
)


# Exercise 6
# Write a function, check_infinitive, that takes a string representing a
#  French word as an argument
# It should return True if it is an infinitive verb, and False otherwise
# A French infinitive verb is a word that ends with either "re", "ir" or "er"

# Define function here...


SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "manger"
).returns(True)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "faire"
).returns(True)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "aller"
).returns(True)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "finir"
).returns(True)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "rendre"
).returns(True)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "savoir"
).returns(True)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "suis"
).returns(False)

SkipCheck(check_infinitive, "Check infinitive").when_called_with("ai").returns(
    False
)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "ete"
).returns(False)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "sais"
).returns(False)

SkipCheck(check_infinitive, "Check infinitive").when_called_with(
    "allons"
).returns(False)


# Exercise 7
# Write a function, collect_plurals, that takes a list of strings as
#  an argument
# It should return a list containing all strings ending with an 's' from the
#  input (retaining the order)

# Define function here...


SkipCheck(collect_plurals, "Collect plurals").when_called_with(
    ["dogs", "cat", "apples", "kittens", "kiwi"]
).returns(["dogs", "apples", "kittens"])

SkipCheck(collect_plurals, "Collect plurals").when_called_with(
    ["abcs", "humans", "thoughts", "cloud", "computer", "cups"]
).returns(["abcs", "humans", "thoughts", "cups"])


# Exercise 8
# Write a function, make_all_admins, that takes a list of 'user' dictionaries
#  as an argument
# Each user will be an dictionary with key of 'name' and 'admin'
# The 'admin' key will have a boolean value
# You should return a list of user objects each with the 'admin' key set
#  to True

# Define function here...


SkipCheck(make_all_admins, "Make all admins").when_called_with(
    [
        {"name": "Barry", "admin": False},
        {"name": "Sandeep", "admin": True},
        {"name": "Kavita", "admin": False},
    ]
).returns(
    [
        {"name": "Barry", "admin": True},
        {"name": "Sandeep", "admin": True},
        {"name": "Kavita", "admin": True},
    ]
)
