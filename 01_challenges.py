# Exercise 0
def create_multi_type_list():
    multi_type_list = ["I am a string", 42, True, [1, 2, 3]]
    return multi_type_list


multi_type_list = create_multi_type_list()

assert type(multi_type_list[0]) is FILL_ME_IN
assert type(multi_type_list[1]) is FILL_ME_IN
assert type(multi_type_list[2]) is FILL_ME_IN
assert type(multi_type_list[3]) is FILL_ME_IN


# Exercise 1
def list_mutation():
    letters = ["a", "b", "c"]
    letters.append("d")
    letters.append("g")
    return letters


letters = list_mutation()

assert letters == FILL_ME_IN

last_letter = letters.pop()

assert last_letter == FILL_ME_IN
assert letters == FILL_ME_IN


# Exercise 2
def nested_lists():
    rows = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
    ]
    return rows


rows = nested_lists()

assert rows[0] == FILL_ME_IN
assert rows[1] == FILL_ME_IN
assert rows[2] == FILL_ME_IN

first_row = rows[0]
assert first_row[0] == "a"
assert first_row[FILL_ME_IN] == "b"

assert rows[1][FILL_ME_IN] == "e"
assert rows[2][FILL_ME_IN] == "g"
assert rows[0][FILL_ME_IN] == "c"


# Exercise 3
def dictionary_keys():
    father = {
        "first_name": "Michael",
        "last_name": "Bluth",
        "age": 33,
    }
    return father


father = dictionary_keys()

key = "first_name"
assert father["last_name"] == FILL_ME_IN
assert father["age"] == FILL_ME_IN
assert father[key] == FILL_ME_IN


# Exercise 4
def removing_dict_keys():
    brother_in_law = {
        "name": "Tobias",
        "lastname": "Funke",
        "job": "therapist",
    }
    return brother_in_law


brother_in_law = removing_dict_keys()

assert brother_in_law["job"] == FILL_ME_IN

del brother_in_law["job"]
assert brother_in_law == FILL_ME_IN


# Exercise 5
def nested_dictionaries():
    bluth_family = {
        "father": {
            "name": "George",
        },
        "mother": {
            "name": "Lucille",
        },
        "sons": [{"name": "GOB"}, {"name": "Michael"}, {"name": "Buster"}],
        "daughters": [{"name": "Lindsay"}],
    }
    return bluth_family


bluth_family = nested_dictionaries()

assert bluth_family["father"]["name"] == FILL_ME_IN
assert bluth_family["mother"]["name"] == FILL_ME_IN
assert bluth_family["daughters"][FILL_ME_IN][FILL_ME_IN] == "Lindsay"
