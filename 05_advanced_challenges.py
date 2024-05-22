from test_api.checks import Check, SkipCheck

# If we list all the whole numbers below 10 that are multiples of 3 or 5, we
#  get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3
#  or 5 below the limit passed in as an argument.
# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once!


def find_total_of_multiples(limit):
    pass


Check(
    find_total_of_multiples, "return zero for negative numbers"
).when_called_with(-1).returns(0)

Check(find_total_of_multiples, "returns first multiple of 3").when_called_with(
    4
).returns(3)

Check(
    find_total_of_multiples, "returns sum of multiples of 3 or 5  below limit"
).when_called_with(6).returns(8)
Check(
    find_total_of_multiples, "returns sum of multiples of 3 or 5  below limit"
).when_called_with(10).returns(23)


# ---------------------------------------------------------------------------

# In a factory a printer prints labels for boxes. For one kind of boxes the
#  printer has to use colors which are named with letters from a to m.
# The colours used by the printer are recorded in a string.

# For example a "good" control string would be aaabbbbhaijjjm meaning that
#  the printer used:
# - colour 'a' three times
# - colour 'b' four times
# - colour 'h' one time
# and so on.

# Sometimes there are problems and a "bad" control string is produced
#  e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# Write a function named count_printer_errors which given a string will
#  return the error rate of the printer.

# You should return a string representing a fraction whose numerator is the
#  number of errors and the denominator the length of the control string.

# Example:
# control = "aaabbbbhaijjjm"
# count_printer_errors(control) should return "0/14"

# control = "aaaxbbbbyyhwawiwjjjwwm"
# count_printer_errors(control) should return "8/22"


def count_printer_errors():
    pass


SkipCheck(
    count_printer_errors, "return zero for an empty control string"
).when_called_with("").returns("0/0")

SkipCheck(
    count_printer_errors, "return correct control string length"
).when_called_with("aaa").returns("0/3")

SkipCheck(
    count_printer_errors, "correctly count errors in control string"
).when_called_with("aaz").returns("1/3")

SkipCheck(
    count_printer_errors, "correctly count errors in control string"
).when_called_with("aaaxbbbbyyhwawiwjjjwwm").returns("8/22")


# ---------------------------------------------------------------------------
# Ordinal suffixes are the letters we put after a number:
# E.g. "nd" is an ordinal suffix as we'd write 2nd and "st" is an ordinal
#  suffix as we'd write 1st etc

# This function should take a number as an argument and should return the
#  corresponding ordinal suffix

# See here for more details:
#  https://www.grammarly.com/blog/how-to-write-ordinal-numbers-correctly/


def get_ordinal_suffix(num):
    pass


SkipCheck(get_ordinal_suffix, "return 'st' when given 1").when_called_with(
    1
).returns("st")

SkipCheck(get_ordinal_suffix, "return 'nd' when given 2").when_called_with(
    2
).returns("nd")

SkipCheck(get_ordinal_suffix, "return 'rd' when given 3").when_called_with(
    3
).returns("rd")

SkipCheck(
    get_ordinal_suffix, "return 'th' given any single digit number above 3"
).when_called_with(4).returns("th")

SkipCheck(
    get_ordinal_suffix, "return 'th' given any single digit number above 3"
).when_called_with(7).returns("th")

SkipCheck(
    get_ordinal_suffix, "return 'th' given any single digit number above 3"
).when_called_with(9).returns("th")

SkipCheck(
    get_ordinal_suffix,
    "return 'th' given any value between 10 and 20 inclusive",
).when_called_with(10).returns("th")

SkipCheck(
    get_ordinal_suffix,
    "return 'th' given any value between 10 and 20 inclusive",
).when_called_with(11).returns("th")

SkipCheck(
    get_ordinal_suffix,
    "return 'th' given any value between 10 and 20 inclusive",
).when_called_with(15).returns("th")

SkipCheck(
    get_ordinal_suffix,
    "return 'th' given any value between 10 and 20 inclusive",
).when_called_with(19).returns("th")

SkipCheck(
    get_ordinal_suffix,
    "return 'th' given any value between 10 and 20 inclusive",
).when_called_with(20).returns("th")

SkipCheck(
    get_ordinal_suffix, "return 'st' given any value above 20 ending in 1"
).when_called_with(21).returns("st")

SkipCheck(
    get_ordinal_suffix, "return 'st' given any value above 20 ending in 1"
).when_called_with(41).returns("st")

SkipCheck(
    get_ordinal_suffix, "return 'nd' given any value above 20 ending in 2"
).when_called_with(22).returns("nd")

SkipCheck(
    get_ordinal_suffix, "return 'nd' given any value above 20 ending in 2"
).when_called_with(32).returns("nd")

SkipCheck(
    get_ordinal_suffix, "return 'rd' given any value above 20 ending in 3"
).when_called_with(23).returns("rd")

SkipCheck(
    get_ordinal_suffix, "return 'rd' given any value above 20 ending in 3"
).when_called_with(63).returns("rd")

SkipCheck(
    get_ordinal_suffix, "return 'th' given any other numbers"
).when_called_with(27).returns("th")

SkipCheck(
    get_ordinal_suffix, "return 'th' given any other numbers"
).when_called_with(98).returns("th")


# ---------------------------------------------------------------------------


# This function should take a string as its argument and
# return True if each character appears only once and False otherwise
def contains_no_repeats(str):
    pass


SkipCheck(
    contains_no_repeats, "return True for an empty string"
).when_called_with("").returns(True)

SkipCheck(
    contains_no_repeats, "return False for a single repeated character"
).when_called_with("oo").returns(False)

SkipCheck(
    contains_no_repeats, "return False for a single repeated character"
).when_called_with("zzz").returns(False)


SkipCheck(
    contains_no_repeats, "return True when each character appears only once"
).when_called_with("dog").returns(True)

SkipCheck(
    contains_no_repeats, "return True when each character appears only once"
).when_called_with("cat").returns(True)

SkipCheck(
    contains_no_repeats, "return True when each character appears only once"
).when_called_with("abcde").returns(True)

SkipCheck(
    contains_no_repeats, "return False if any characters are repeated"
).when_called_with("dooog").returns(False)

SkipCheck(
    contains_no_repeats, "return False if any characters are repeated"
).when_called_with("iHaveRepeats").returns(False)

SkipCheck(
    contains_no_repeats, "return False if any characters are repeated"
).when_called_with("anat").returns(False)

SkipCheck(
    contains_no_repeats, "return False if any characters are repeated"
).when_called_with("abcdea").returns(False)


# ---------------------------------------------------------------------------

# When users are signing up for our service we ask them pick a username.
# Each person's username must be unique and we will write a function to check
#  if their usernames have already been taken or not

# This function should take a list of existing usernames and any number of
#  additional usernames to check
# It should return True if all the new usernames are available, and False if
#  any of them already exist


def check_usernames_available(usernames, *names):
    pass


SkipCheck(
    check_usernames_available, "return True for a single available username"
).when_called_with(["Roy", "Moss"], "Jen").returns(True)

SkipCheck(
    check_usernames_available,
    "return False for a single username that is taken",
).when_called_with(["Roy", "Moss"], "Moss").returns(False)

SkipCheck(
    check_usernames_available,
    "return True for multiple usernames that are available",
).when_called_with(["Roy", "Moss"], "Jen", "Douglas").returns(True)

SkipCheck(
    check_usernames_available,
    "return False for multiple usernames that are available",
).when_called_with(["Roy", "Moss"], "Roy", "Moss").returns(False)

SkipCheck(
    check_usernames_available,
    "return False if a single username is not available",
).when_called_with(["Roy", "Moss"], "Jen", "Moss").returns(False)

SkipCheck(
    check_usernames_available, "return True if no new usernames are passed"
).when_called_with(["Roy", "Moss"]).returns(True)
