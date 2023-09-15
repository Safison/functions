# Exercise 1
# This function should take a list as an argument and return True if the list is empty, False otherwise.
def is_empty_list():
    pass


def test_is_empty_list():
    assert test_is_empty_list([]) == True
    assert test_is_empty_list(["a", "b", "c", "d"]) == False
    assert test_is_empty_list(["a"]) == False


# Exercise 2
# This function should take an dictionary representing a person and information about whether they like to code
# A person will take this form:
# {
#   "name": "Mitch",
#   "likesToCode": True
# }

# If the 'likesToCode' property is true, then you should return a string of the form
#   "My name is Mitch and I like to code."


# If the 'likesToCode' property is false, the string should look like
#   "My name is Mitch and I don't like to code."
def create_profile_description():
    pass


def test_create_profile_description():
    assert (
        create_profile_description({"name": "Mitch", "likesToCode": true})
        == "My name is Mitch and I like to code."
    )
    assert (
        create_profile_description({"name": "Lisa", "likesToCode": false})
        == "My name is Lisa and I don't like to code."
    )


# Exercise 3
# This function should take a string representing a traffic light colour as an argument
# It will be one of "red", "green" or "amber" in either uppercase or lowercase
# You should return a corresponding message


def read_traffic_light():
    pass


def test_read_traffic_light():
    assert read_traffic_light("green") == "GO!"
    assert read_traffic_light("GREEN") == "GO!"

    assert read_traffic_light("amber") == "GET READY..."
    assert read_traffic_light("AMBER") == "GET READY..."

    assert read_traffic_light("red") == "STOP!"
    assert read_traffic_light("RED") == "STOP!"


# Exercise 4
# This function should take any number of arguments and return the number of arguments passed into the function
def how_many_arguments():
    pass


def test_how_many_arguments():
    assert how_many_arguments("a", "b", "c") == 3
    assert how_many_arguments() == 0
    assert how_many_arguments(1, 2, 3, 4, 5) == 5
    assert how_many_arguments("the", "meaning", "of", "life", "is", 42) == 6


# Exercise 5
# This function should take a dictionary representing a coin machine and a string representing a coin as its arguments
# A coin machine object will take this form:
# {
#   "1p": 0,
#   "2p": 0,
#   "5p": 0,
#   "10p": 0
# }
# You should 'add the provided coin to the machine by altering the associated key and returning the updated coin machine
def update_coin_machine():
    pass


def test_update_coin_machine():
    assert update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p") == {
        "1p": 1,
        "2p": 0,
        "5p": 0,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p") == {
        "1p": 0,
        "2p": 1,
        "5p": 0,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p") == {
        "1p": 0,
        "2p": 4,
        "5p": 0,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p") == {
        "1p": 0,
        "2p": 3,
        "5p": 11,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p") == {
        "1p": 0,
        "2p": 3,
        "5p": 10,
        "10p": 1,
    }


# Exercise 6

# This function should take a list representing coordinates - an x position and a y position - and a string representing a direction
# It should return a new pair of coordinates, with the coords updated by moving either x or y 1 unit in a particular direction


# If direction is "up" it should move 1 unit up (+ 1 in the y direction)
# If the direction is "down" it should move 1 unit down (- 1 in the y direction)
# If the direction is "right" it should move 1 unit right (+ 1 in the x direction)
# If the direction is "left" it should move 1 unit left (- 1 in the x direction)
def update_position():
    pass


def test_update_position():
    assert test_update_position([10, 10], "up") == [10, 11]
    assert test_update_position([0, 0], "down") == [0, -1]
    assert test_update_position([3, 3], "left") == [2, 3]
    assert test_update_position([7, 50], "right") == [8, 50]


# Exercise 7
# This function should take any value as an argument, and return true if it is falsy, and false otherwise
def is_falsy(value):
    return bool(value) == False


def test_is_falsy():
    assert is_falsy(False) == True
    assert is_falsy("") == True
    assert is_falsy(0) == True
    assert is_falsy({}) == True
    assert is_falsy(None) == True
    assert is_falsy(True) == False


# Exercise 8
# This function should take a number representing a dice roll and a string representing a coin toss as its arguments
# A dice roll will be a number between 1 and 6
# A coin toss will be "H" or "T" representing heads or tails
# The game is considered to be won if the dice roll is 3 or higher AND the coin toss is "H"
# You should return True if the game has been won and False otherwise
def check_game():
    pass


def test_check_game():
    assert check_game(3, "H") == True
    assert check_game(4, "H") == True
    assert check_game(5, "H") == True
    assert check_game(6, "H") == True
    assert check_game(6, "T") == False


# Exercise 10
# In this function, a "coin collection" is represented by a list containing 4 other nested lists, each representing a slot in the collection in the following way:
#  1p   2p   5p   10p
# [[],  [],  [],  []] <-- coinCollection
# This should take two arguments, a coin collection list and a string representing a coin, and return an updated version of the given list
# with the coin added at the appropriate position
def add_coins():
    pass


def test_add_coins():
    assert addCoins([[], [], [], []], "1p") == [["1p"], [], [], []]
    assert addCoins([[], [], [], []], "2p") == [[], ["2p"], [], []]
    assert addCoins([[], ["2p"], [], []], "2p") == [[], ["2p", "2p"], [], []]
    assert addCoins([[], [], [], []], "5p") == [[], [], ["5p"], []]
    assert addCoins([["1p"], [], [], ["10p", "10p"]], "2p") == [
        ["1p"],
        ["2p"],
        [],
        ["10p", "10p"],
    ]
    assert addCoins([[], [], ["5p", "5p"], []], "5p") == [
        [],
        [],
        ["5p", "5p", "5p"],
        [],
    ]


#  Mark your progress on the Learn 2 Code platform before moving on to the next set of challenges!
