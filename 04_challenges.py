import pytest


# Exercise 0
# Write a function, check_if_key_exists, that takes a dictionary and a key as
#  its arguments
# It should return True if the dictionary contains the provided key,
#  False otherwise


def test_check_if_key_exists():
    assert check_if_key_exists({"name": "jonny", "age": 32}, "name") == True
    assert check_if_key_exists({"name": "jonny", "age": 32}, "age") == True
    assert check_if_key_exists({"name": "jonny", "age": 32}, "pets") == False


# Exercise 1
# Write a function, create_dict, that takes a list consisting of two elements
#  representing a key / value pair as its argument
# It should return a dictionary with a single key based on the input


@pytest.mark.skip()
def test_create_dict():
    assert create_dict(["name", "shaq"]) == {"name": "shaq"}
    assert create_dict(["fruit", "apple"]) == {"fruit": "apple"}
    assert create_dict(["language", "haskell"]) == {"language": "haskell"}


# Exercise 2
# Write a function, get_first_n_items, that takes two arguments, a list and
#  a number 'n'
# It should return a new list containing the first 'n' items of the given list


@pytest.mark.skip()
def test_get_first_n_items():
    assert get_first_n_items(["a", "b", "c", "d"], 2) == ["a", "b"]
    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 0) == []
    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 3) == [
        "apple",
        "banana",
        "pear",
    ]


# Exercise 3
# Write a function, create_arrow, that takes a string representing a
#  direction ("left", "right", "up" or "down") as its argument
# It should return the corresponding arrow ("←", "→", "↑", "↓")
# You don't need to utilise an dictionary here, but think about how you
#  could do so


@pytest.mark.skip()
def test_create_arrow():
    assert create_arrow("left") == "←"
    assert create_arrow("right") == "→"
    assert create_arrow("up") == "↑"
    assert create_arrow("down") == "↓"


# Exercise 4
# Write a function, move_item_to_end, that takes two arguments, a list and an
#  index value
# It should return a new list where the item that was previously at the
#  given index is now at the end of the list


@pytest.mark.skip()
def test_move_item_to_end():
    assert move_item_to_end(["a", "b", "c"], 0) == ["b", "c", "a"]
    assert move_item_to_end(["a", "b", "c", "d"], 2) == ["a", "b", "d", "c"]
    assert move_item_to_end(["a", "b", "c", "d"], 1) == ["a", "c", "d", "b"]


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


@pytest.mark.skip()
def test_update_user_age():
    user1 = {
        "admin": False,
        "username": "xoxoAlexoxo",
        "personal_details": {
            "name": "Alex",
            "age": 39,
            "fav_food": "gooseberry fool",
        },
    }
    update_user_age(user1)
    assert user1 == {
        "admin": False,
        "username": "xoxoAlexoxo",
        "personal_details": {
            "name": "Alex",
            "age": 40,
            "fav_food": "gooseberry fool",
        },
    }

    user2 = {
        "admin": True,
        "username": "brum4life",
        "personal_details": {
            "name": "Poonam",
            "age": 19,
            "fav_food": "caviar",
        },
    }
    update_user_age(user2)
    assert user2 == {
        "admin": True,
        "username": "brum4life",
        "personal_details": {
            "name": "Poonam",
            "age": 20,
            "fav_food": "caviar",
        },
    }


# Exercise 6
# Write a function, check_infinitive, that takes a string representing a
#  French word as an argument
# It should return True if it is an infinitive verb, and False otherwise
# A French infinitive verb is a word that ends with either "re", "ir" or "er"


@pytest.mark.skip()
def test_check_infinitive():
    assert check_infinitive("manger") == True
    assert check_infinitive("faire") == True
    assert check_infinitive("aller") == True
    assert check_infinitive("finir") == True
    assert check_infinitive("rendre") == True
    assert check_infinitive("savoir") == True

    assert check_infinitive("suis") == False
    assert check_infinitive("ai") == False
    assert check_infinitive("ete") == False
    assert check_infinitive("sais") == False
    assert check_infinitive("allons") == False


# Exercise 7
# Write a function, collect_plurals, that takes a list of strings as
#  an argument
# It should return a list containing all strings ending with an 's' from the
#  input (retaining the order)


@pytest.mark.skip()
def test_collect_plurals():
    assert collect_plurals(["dogs", "cat", "apples", "kittens", "kiwi"]) == [
        "dogs",
        "apples",
        "kittens",
    ]

    assert collect_plurals(
        ["abcs", "humans", "thoughts", "cloud", "computer", "cups"]
    ) == ["abcs", "humans", "thoughts", "cups"]


# Exercise 8
# Write a function, make_all_admins, that takes a list of 'user' dictionaries
#  as an argument
# Each user will be an dictionary with key of 'name' and 'admin'
# The 'admin' key will have a boolean value
# You should return a list of user objects each with the 'admin' key set
#  to True


@pytest.mark.skip()
def test_make_all_admins():
    users = [
        {"name": "Barry", "admin": False},
        {"name": "Sandeep", "admin": True},
        {"name": "Kavita", "admin": False},
    ]
    assert make_all_admins(users) == [
        {"name": "Barry", "admin": True},
        {"name": "Sandeep", "admin": True},
        {"name": "Kavita", "admin": True},
    ]
