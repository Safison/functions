from test_api.checks import Check, SkipCheck


# Challenge 0
# This function should return the product of two passed numbers.
def multiply(num_1, num_2):
    pass


Check(multiply, "return the product of two passed numbers").when_called_with(
    3, 5
).returns(15)
Check(multiply, "return the product of two passed numbers").when_called_with(
    17, 19
).returns(323)
Check(multiply, "return the product of two passed numbers").when_called_with(
    -180, 2
).returns(-360)


# Challenge 1
# This function should take a single argument and return its value
# rounded DOWN to the nearest integer.
def round_down():
    pass


SkipCheck(
    round_down, "return its value rounded DOWN to the nearest integer"
).when_called_with(100.1).returns(100)
SkipCheck(
    round_down, "return its value rounded DOWN to the nearest integer"
).when_called_with(25.5).returns(25)
SkipCheck(
    round_down, "return its value rounded DOWN to the nearest integer"
).when_called_with(121.999).returns(121)


# Challenge 2
# This function should take two arguments, m and n, and return m
# raised to the power of n.
def raise_to_power():
    pass


SkipCheck(
    raise_to_power, "return m raised to the power of n"
).when_called_with(10, 3).returns(1000)
SkipCheck(
    raise_to_power, "return m raised to the power of n"
).when_called_with(25, 2).returns(625)
SkipCheck(
    raise_to_power, "return m raised to the power of n"
).when_called_with(10, 0).returns(1)


# Challenge 3
# This function should take a number as an argument
# and return True if it is a multiple of 6, False otherwise.
def is_multiple_of_6():
    pass


SkipCheck(
    is_multiple_of_6, "return True if it is a multiple of 6, False otherwise"
).when_called_with(6).returns(True)
SkipCheck(
    is_multiple_of_6, "return True if it is a multiple of 6, False otherwise"
).when_called_with(10).returns(False)
SkipCheck(
    is_multiple_of_6, "return True if it is a multiple of 6, False otherwise"
).when_called_with(15).returns(False)
SkipCheck(
    is_multiple_of_6, "return True if it is a multiple of 6, False otherwise"
).when_called_with(36).returns(True)
SkipCheck(
    is_multiple_of_6, "return True if it is a multiple of 6, False otherwise"
).when_called_with(60).returns(True)
SkipCheck(
    is_multiple_of_6, "return True if it is a multiple of 6, False otherwise"
).when_called_with(61).returns(False)


# Challenge 4
# This function should take a string as an argument and return
# the same string with the first letter capitalised.


def capitalise_first_letter():
    pass


SkipCheck(
    capitalise_first_letter,
    "return the same string with the first letter capitalised",
).when_called_with("bang").returns("Bang")
SkipCheck(
    capitalise_first_letter,
    "return the same string with the first letter capitalised",
).when_called_with("apple").returns("Apple")
SkipCheck(
    capitalise_first_letter,
    "return the same string with the first letter capitalised",
).when_called_with("coding").returns("Coding")


# Challenge 5
# This function should take a integer as an argument representing a year,
# and return true if that year is in the 20th century and false otherwise.


def is_in_the_20th_century():
    pass


SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(1962).returns(True)
SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(1901).returns(True)
SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(1900).returns(False)
SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(1913).returns(True)
SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(1876).returns(False)
SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(2001).returns(False)
SkipCheck(
    is_in_the_20th_century,
    "return true if that year is in the 20th century and false otherwise",
).when_called_with(2000).returns(True)


# Challenge 6
# This function should take a string as an argument representing a file path
# and return True if it is an absolute path, and False otherwise.
# HINT: all absolute file paths start with a /


def is_absolute_path():
    pass


SkipCheck(
    is_absolute_path,
    "return True if it is an absolute path, and False otherwise",
).when_called_with("/Users/mitch").returns(True)
SkipCheck(
    is_absolute_path,
    "return True if it is an absolute path, and False otherwise",
).when_called_with(
    "/Users/mitch/northcoders/remote_course/remote_precourse_1"
).returns(
    True
)
SkipCheck(
    is_absolute_path,
    "return True if it is an absolute path, and False otherwise",
).when_called_with("../composers").returns(False)
SkipCheck(
    is_absolute_path,
    "return True if it is an absolute path, and False otherwise",
).when_called_with("./applications/my-awesome-app.js").returns(False)


# Challenge 7
# This function should take a string as an argument and
# return a string which describes the ASCII code of that character
# The returned string should be in the following format:
# "The ASCII code for <character> is <character-code>"


def get_char_code():
    pass


SkipCheck(
    get_char_code,
    "return a string which describes the ASCII code of that character",
).when_called_with("A").returns("The ASCII code for A is 65")
SkipCheck(
    get_char_code,
    "return a string which describes the ASCII code of that character",
).when_called_with("b").returns("The ASCII code for b is 98")
SkipCheck(
    get_char_code,
    "return a string which describes the ASCII code of that character",
).when_called_with("z").returns("The ASCII code for z is 122")
SkipCheck(
    get_char_code,
    "return a string which describes the ASCII code of that character",
).when_called_with("k").returns("The ASCII code for k is 107")
SkipCheck(
    get_char_code,
    "return a string which describes the ASCII code of that character",
).when_called_with("!").returns("The ASCII code for ! is 33")
SkipCheck(
    get_char_code,
    "return a string which describes the ASCII code of that character",
).when_called_with("M").returns("The ASCII code for M is 77")


# Challenge 8
# This function should take a length and a character as arguments
# and return a list of the given length populated with the given character.


def create_list():
    pass


SkipCheck(
    create_list,
    "return a list of the given length populated with the given character",
).when_called_with(3, "!").returns(["!", "!", "!"])
SkipCheck(
    create_list,
    "return a list of the given length populated with the given character",
).when_called_with(5, "a").returns(["a", "a", "a", "a", "a"])


# Challenge 9
# This function should take a integer representing a battery level
#  as a percentage.
# If the battery level is less than or equal to 5%, then you should return
#  a string stating:
#     "Warning - battery level low: <number-here>%, please charge your device"
# If the battery level is between 5 and 99% then it should return a
#  string stating:
#     "Battery level: <number-here>%"
# If the battery level is 100% then it should return a string stating:
#     "Fully charged :)"


def check_battery_level():
    pass


SkipCheck(check_battery_level, "returns fully charged").when_called_with(
    100
).returns("Fully charged :)")
SkipCheck(check_battery_level, "returns battery level").when_called_with(
    99
).returns("Battery level: 99%")
SkipCheck(check_battery_level, "returns battery level").when_called_with(
    80
).returns("Battery level: 80%")
SkipCheck(check_battery_level, "returns battery level").when_called_with(
    30
).returns("Battery level: 30%")
SkipCheck(check_battery_level, "returns battery level").when_called_with(
    10
).returns("Battery level: 10%")
SkipCheck(check_battery_level, "returns battery level").when_called_with(
    6
).returns("Battery level: 6%")
SkipCheck(check_battery_level, "returns battery level").when_called_with(
    5
).returns("Warning - battery level low: 5%, please charge your device")
SkipCheck(check_battery_level, "check_battery_level").when_called_with(
    4
).returns("Warning - battery level low: 4%, please charge your device")
SkipCheck(check_battery_level, "check_battery_level").when_called_with(
    3
).returns("Warning - battery level low: 3%, please charge your device")
SkipCheck(check_battery_level, "check_battery_level").when_called_with(
    1
).returns("Warning - battery level low: 1%, please charge your device")


# Challenge 10
# This function should take a list as an argument and return
# a list containing all string elements from the input (retaining the order)


def collect_strings():
    pass


SkipCheck(
    collect_strings,
    "return a list containing all string elements from the input",
).when_called_with(["a", "b", "c"]).returns(["a", "b", "c"])

SkipCheck(
    collect_strings,
    "return a list containing all string elements from the input",
).when_called_with(["a", 10, "b", 1000, "c"]).returns(["a", "b", "c"])
