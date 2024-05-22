from test_api.checks import Check, SkipCheck


# Exercise 0
# This function should take a list as an argument and return True if the list
#  is empty, False otherwise.
def is_empty_list(list_to_check):
    pass


Check(
    is_empty_list, "return True if the list is empty, False otherwise"
).when_called_with([]).returns(True)

Check(
    is_empty_list, "return True if the list is empty, False otherwise"
).when_called_with(["a", "b", "c", "d"]).returns(False)

Check(
    is_empty_list, "return True if the list is empty, False otherwise"
).when_called_with(["a"]).returns(False)


# Exercise 1
# This function should take an dictionary representing a person and information
#  about whether they like to code

# A person will take this form:
# {
#   "name": "Danika",
#   "likes_to_code": True
# }

# If the 'likes_to_code' key is true, then return a string of the form
#   "My name is Danika and I like to code."


# If the 'likes_to_code' key is false, the string should look like
#   "My name is Danika and I don't like to code."


def create_profile_description():
    pass


SkipCheck(
    create_profile_description,
    "return a string describing a person and their coding preferences",
).when_called_with({"name": "Danika", "likes_to_code": True}).returns(
    "My name is Danika and I like to code."
)

SkipCheck(
    create_profile_description,
    "return a string describing a person and their coding preferences",
).when_called_with({"name": "Alex", "likes_to_code": False}).returns(
    "My name is Alex and I don't like to code."
)


# Exercise 2
# This function should take a string representing a traffic light colour as
#  an argument

# It will be one of "red", "green" or "amber" in either uppercase or lowercase
# You should return a corresponding message


def read_traffic_light():
    pass


SkipCheck(
    read_traffic_light,
    "return a message based on the traffic light colour",
).when_called_with("green").returns("GO!")

SkipCheck(
    read_traffic_light,
    "return a message based on the traffic light colour",
).when_called_with("GREEN").returns("GO!")

SkipCheck(
    read_traffic_light,
    "return a message based on the traffic light colour",
).when_called_with("amber").returns("GET READY...")

SkipCheck(
    read_traffic_light,
    "return a message based on the traffic light colour",
).when_called_with("AMBER").returns("GET READY...")

SkipCheck(
    read_traffic_light,
    "return a message based on the traffic light colour",
).when_called_with("red").returns("STOP!")

SkipCheck(
    read_traffic_light,
    "return a message based on the traffic light colour",
).when_called_with("RED").returns("STOP!")


# Exercise 3
# This function should take any number of arguments and return the number of
#  arguments passed into the function
def how_many_arguments():
    pass


SkipCheck(
    how_many_arguments,
    "return the number of arguments passed into the function",
).when_called_with("a", "b", "c").returns(3)

SkipCheck(
    how_many_arguments,
    "return the number of arguments passed into the function",
).when_called_with().returns(0)

SkipCheck(
    how_many_arguments,
    "return the number of arguments passed into the function",
).when_called_with(1, 2, 3, 4, 5).returns(5)

SkipCheck(
    how_many_arguments,
    "return the number of arguments passed into the function",
).when_called_with("the", "meaning", "of", "life", "is", 42).returns(6)


# Exercise 4
# This function should take a dictionary representing a coin machine and a
#  string representing a coin as its arguments

# A coin machine object will take this form:
# {
#   "1p": 0,
#   "2p": 0,
#   "5p": 0,
#   "10p": 0
# }


# You should 'add the provided coin to the machine by altering the associated
#  key and returning the updated coin machine
def update_coin_machine():
    pass


SkipCheck(
    update_coin_machine,
    "return the updated coin machine",
).when_called_with({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p").returns(
    {"1p": 1, "2p": 0, "5p": 0, "10p": 0}
)

SkipCheck(
    update_coin_machine, "return the updated coin machine"
).when_called_with({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p").returns(
    {"1p": 0, "2p": 1, "5p": 0, "10p": 0}
)

SkipCheck(
    update_coin_machine, "return the updated coin machine"
).when_called_with({"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p").returns(
    {
        "1p": 0,
        "2p": 4,
        "5p": 0,
        "10p": 0,
    }
)

SkipCheck(
    update_coin_machine, "return the updated coin machine"
).when_called_with({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p").returns(
    {
        "1p": 0,
        "2p": 3,
        "5p": 11,
        "10p": 0,
    }
)

SkipCheck(
    update_coin_machine, "return the updated coin machine"
).when_called_with({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p").returns(
    {
        "1p": 0,
        "2p": 3,
        "5p": 10,
        "10p": 1,
    }
)


# Exercise 5

# This function should take a list representing coordinates - an x position and
#  a y position - and a string representing a direction.
# It should return a new pair of coordinates, with the coords updated by moving
#  either x or y 1 unit in a particular direction.


# If direction is "up" it should move 1 unit up (+ 1 in the y direction)
# If the direction is "down" it should move 1 unit down(- 1 in the y direction)
# If direction is "right" it should move 1 unit right (+1 in the x direction)
# If the direction is "left" it should move 1 unit left(- 1 in the x direction)
def update_position():
    pass


SkipCheck(
    update_position,
    "return the updated position",
).when_called_with(
    [10, 10], "up"
).returns([10, 11])

SkipCheck(
    update_position,
    "return the updated position",
).when_called_with(
    [0, 0], "down"
).returns([0, -1])

SkipCheck(
    update_position,
    "return the updated position",
).when_called_with(
    [3, 3], "left"
).returns([2, 3])

SkipCheck(
    update_position,
    "return the updated position",
).when_called_with(
    [7, 50], "right"
).returns([8, 50])


# Exercise 6
# This function should take any value as an argument, and return true if it is
#  falsy, and false otherwise
def is_falsy():
    pass


SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with(False).returns(True)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with(True).returns(False)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with("").returns(True)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with(0).returns(True)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with({}).returns(True)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with({"a": 1}).returns(False)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with([]).returns(True)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with([1, 2, 3]).returns(False)
SkipCheck(
    is_falsy, "return true if the argument is falsy, false otherwise"
).when_called_with(None).returns(True)


# Exercise 7
# This function should take a number representing a dice roll and a string
#  representing a coin toss as its arguments
# A dice roll will be a number between 1 and 6
# A coin toss will be "H" or "T" representing heads or tails
# The game is considered to be won if the dice roll is 3 or higher AND the
#  coin toss is "H"
# You should return True if the game has been won and False otherwise
def check_game():
    pass


SkipCheck(
    check_game, "return True if the game has been won, False otherwise"
).when_called_with(3, "H").returns(True)

SkipCheck(
    check_game, "return True if the game has been won, False otherwise"
).when_called_with(4, "H").returns(True)

SkipCheck(
    check_game, "return True if the game has been won, False otherwise"
).when_called_with(5, "H").returns(True)

SkipCheck(
    check_game, "return True if the game has been won, False otherwise"
).when_called_with(6, "H").returns(True)

SkipCheck(
    check_game, "return True if the game has been won, False otherwise"
).when_called_with(6, "T").returns(False)


# Exercise 8
# In this function, a "coin collection" is represented by a list containing 4
#  other nested lists, each representing a slot in the collection in the
#  following way:
#        1p   2p   5p   10p
#       [[],  [],  [],  []] <-- coinCollection
# This should take two arguments, a coin collection list and a
#   string representing a coin, and return an updated version of the given
#   list with the coin added at the appropriate position
def add_coins():
    pass


SkipCheck(
    add_coins, "return an updated version of the given list with the coin"
).when_called_with([[], [], [], []], "1p").returns([["1p"], [], [], []])
SkipCheck(
    add_coins, "return an updated version of the given list with the coin"
).when_called_with([[], [], [], []], "2p").returns([[], ["2p"], [], []])
SkipCheck(
    add_coins, "return an updated version of the given list with the coin"
).when_called_with([[], ["2p"], [], []], "2p").returns(
    [[], ["2p", "2p"], [], []]
)
SkipCheck(
    add_coins, "return an updated version of the given list with the coin"
).when_called_with([[], [], [], []], "5p").returns([[], [], ["5p"], []])
SkipCheck(
    add_coins, "return an updated version of the given list with the coin"
).when_called_with([["1p"], [], [], ["10p", "10p"]], "2p").returns(
    [["1p"], ["2p"], [], ["10p", "10p"]]
)
SkipCheck(
    add_coins, "return an updated version of the given list with the coin"
).when_called_with([[], [], ["5p", "5p"], []], "5p").returns(
    [[], [], ["5p", "5p", "5p"], []]
)


# Mark your progress on the Learn 2 Code platform before moving on to the
#  next set of challenges!
