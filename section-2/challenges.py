import pytest


# Challenge 0
# This function should return the product of two passed numbers.
def multiply():
    pass


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(17, 19) == 323
    assert multiply(-180, 2) == -360


# Challenge 1
# This function should take a single argument and return its value rounded
# DOWN to the nearest integer.
def round_down():
    pass


@pytest.mark.skip()
def test_round_down():
    assert round_down(100.1) == 100
    assert round_down(25.5) == 25
    assert round_down(121.999) == 121


# Challenge 2
# This function should take two arguments, m and n, and return m raised to the
# power of n.
def raise_to_power():
    pass


@pytest.mark.skip()
def test_raise_to_power():
    assert raise_to_power(10, 3) == 1000
    assert raise_to_power(25, 2) == 625
    assert raise_to_power(10, 0) == 1


# Challenge 3
# This function should take a number as an argument
# and return True if it is a multiple of 6, False otherwise.
def is_multiple_of_6():
    pass


@pytest.mark.skip()
def test_is_multiple_of_6():
    assert is_multiple_of_6(6) == True
    assert is_multiple_of_6(10) == False
    assert is_multiple_of_6(15) == False
    assert is_multiple_of_6(36) == True
    assert is_multiple_of_6(60) == True
    assert is_multiple_of_6(61) == False


# Challenge 4
# This function should take a string as an argument and return
# the same string with the first letter capitalised.


def capitalise_first_letter():
    pass


@pytest.mark.skip()
def test_capitalise_first_letter():
    assert capitalise_first_letter("bang") == "Bang"
    assert capitalise_first_letter("apple") == "Apple"
    assert capitalise_first_letter("coding") == "Coding"


# Challenge 5
# This function should take a integer as an argument representing a year,
# and return true if that year is in the 20th century and false otherwise.


def is_in_the_20th_century(year: int):
    pass


@pytest.mark.skip()
def test_is_in_the_20th_century():
    assert is_in_the_20th_century(1962) == True
    assert is_in_the_20th_century(1901) == True
    assert is_in_the_20th_century(1900) == False
    assert is_in_the_20th_century(1913) == True
    assert is_in_the_20th_century(1876) == False
    assert is_in_the_20th_century(2001) == False
    assert is_in_the_20th_century(2000) == True


# Challenge 6
# This function should take a string as an argument representing a file path
# and return True if it is an absolute path, and False otherwise.
# HINT: all absolute file paths start with a /


def is_absolute_path():
    pass


@pytest.mark.skip()
def test_is_absolute_path():
    assert is_absolute_path("/Users/mitch") == True
    assert (
        is_absolute_path(
            "/Users/mitch/northcoders/remote_course/remote_precourse_1")
        == True
    )
    assert is_absolute_path("../composers") == False
    assert is_absolute_path("./applications/my-awesome-app.js") == False


# Challenge 7
# This function should take a string as an argument and return a string
# which describes the ASCII code of that character
# The returned string should be in the following format:
# "The ASCII code for <character> is <character-code>"


def get_char_code():
    pass


@pytest.mark.skip()
def test_get_char_code():
    assert get_char_code("A") == "The ASCII code for A is 65"
    assert get_char_code("b") == "The ASCII code for b is 98"
    assert get_char_code("z") == "The ASCII code for z is 122"
    assert get_char_code("k") == "The ASCII code for k is 107"
    assert get_char_code("!") == "The ASCII code for ! is 33"
    assert get_char_code("M") == "The ASCII code for M is 77"


# Challenge 8
# This function should take a length and a character as arguments
# and return a list of the given length populated with the given character.


def create_list():
    pass


@pytest.mark.skip()
def test_create_list():
    assert create_list(3, "!") == ["!", "!", "!"]
    assert create_list(5, "a") == ["a", "a", "a", "a", "a"]


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


@pytest.mark.skip()
def test_check_battery_level():
    assert check_battery_level(100) == "Fully charged :)"

    assert check_battery_level(99) == "Battery level: 99%"
    assert check_battery_level(80) == "Battery level: 80%"
    assert check_battery_level(30) == "Battery level: 30%"
    assert check_battery_level(10) == "Battery level: 10%"
    assert check_battery_level(6) == "Battery level: 6%"

    assert (
        check_battery_level(5)
        == "Warning - battery level low: 5%, please charge your device"
    )
    assert (
        check_battery_level(4)
        == "Warning - battery level low: 4%, please charge your device"
    )
    assert (
        check_battery_level(3)
        == "Warning - battery level low: 3%, please charge your device"
    )
    assert (
        check_battery_level(1)
        == "Warning - battery level low: 1%, please charge your device"
    )


# Challenge 10
# This function should take a list as an argument and return an list containing
# all string elements from the input (retaining the order)


def collect_strings():
    pass


@pytest.mark.skip()
def test_collect_strings():
    assert collect_strings(["a", "b", "c"]) == ["a", "b", "c"]
    assert collect_strings(["a", 10, "b", 1000, "c"]) == ["a", "b", "c"]
