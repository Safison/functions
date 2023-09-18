# This function should take a string as its argument and return True if each character appears only once and False otherwise
def contains_no_repeats(str):
    pass


def test_contains_no_repeats():
    # contains_no_repeats() returns True for an empty string
    assert contains_no_repeats("") == True

    # contains_no_repeats() returns False for a single repeated character
    assert contains_no_repeats("oo") == False
    assert contains_no_repeats("zzz") == False

    # contains_no_repeats() returns True when each character appears only once
    assert contains_no_repeats("dog") == True
    assert contains_no_repeats("cat") == True
    assert contains_no_repeats("abcde") == True

    # contains_no_repeats() returns False if any characters are repeated
    assert contains_no_repeats("dooog") == False
    assert contains_no_repeats("iHaveRepeats") == False
    assert contains_no_repeats("anat") == False
    assert contains_no_repeats("abcdea") == False


# ---------------------------------------------------------------------------


# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which are named with letters from a to m.
# The colours used by the printer are recorded in a string.

# For example a "good" control string would be aaabbbbhaijjjm meaning:
# that the printer used colour 'a' three times , colour 'b' four times , colour 'h' one time and so on.

# Sometimes there are problems and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# Write a function named count_printer_errors which given a string will return the error rate of the printer.

# You should return a string representing a fraction whose numerator is the number of errors and the denominator the length of the control string.

# Example:
# control = "aaabbbbhaijjjm"
# count_printer_errors(control) should return "0/14"

# control = "aaaxbbbbyyhwawiwjjjwwm"
# count_printer_errors(control) should return "8/22"


def count_printer_errors():
    pass


def test_count_printer_errors():
    # countPrinterErrors() should return zero for an empty control string
    assert count_printer_errors("") == "0/0"

    # count_printer_errors() should return correct control string length
    assert count_printer_errors("aaa") == "0/3"

    # count_printer_errors() should correctly count errors in control string
    assert count_printer_errors("aaz") == "1/3"
    assert count_printer_errors("aaaxbbbbyyhwawiwjjjwwm") == "8/22"


# ---------------------------------------------------------------------------

# If we list all the whole numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the limit passed in as an argument.
# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once! */


def find_total_of_multiples(limit):
    pass


def test_find_total_of_multiples():
    # find_total_of_multiples() return zero for negative numbers
    assert find_total_of_multiples(-1) == 0

    # find_total_of_multiples() returns first multiple of 3
    assert find_total_of_multiples(4) == 3

    # find_total_of_multiples() returns sum of multiples of 3 or 5  below limit

    assert find_total_of_multiples(6) == 8
    assert find_total_of_multiples(10) == 23


# ---------------------------------------------------------------------------

# Ordinal suffixes are the letters we put after a number:
# E.g. "nd" is an ordinal suffix as we'd write 2nd and "st" is an ordinal suffix as we'd write 1st etc

# This function should take a number as an argument and should return the corresponding ordinal suffix

# See here for more details: https://www.grammarly.com/blog/how-to-write-ordinal-numbers-correctly/


def get_ordinal_suffix(num):
    pass


def test_get_ordinal_suffix():
    # getOrdinalSuffix() returns 'st' when given 1
    assert getOrdinalSuffix(1) == "st"

    # getOrdinalSuffix() returns 'nd' when given 2
    assert getOrdinalSuffix(2) == "nd"

    # getOrdinalSuffix() returns 'rd' when given 3
    assert getOrdinalSuffix(3) == "rd"

    # getOrdinalSuffix() returns 'th' given any single digit number above 3
    assert getOrdinalSuffix(4) == "th"
    assert getOrdinalSuffix(7) == "th"
    assert getOrdinalSuffix(9) == "th"

    # getOrdinalSuffix() returns 'th' given any value between 10 and 20 inclusive
    assert getOrdinalSuffix(10) == "th"
    assert getOrdinalSuffix(11) == "th"
    assert getOrdinalSuffix(15) == "th"
    assert getOrdinalSuffix(19) == "th"
    assert getOrdinalSuffix(20) == "th"

    # getOrdinalSuffix() returns 'st' for numbers above 20 ending in 1
    assert getOrdinalSuffix(21) == "st"
    assert getOrdinalSuffix(41) == "st"

    # getOrdinalSuffix() returns 'nd' for numbers above 20 ending in 2
    assert getOrdinalSuffix(22) == "nd"
    assert getOrdinalSuffix(32) == "nd"

    # getOrdinalSuffix() returns 'rd' for numbers above 20 ending in 3
    assert getOrdinalSuffix(23) == "rd"
    assert getOrdinalSuffix(63) == "rd"

    # getOrdinalSuffix() returns 'th' for any other numbers
    assert getOrdinalSuffix(27) == "th"
    assert getOrdinalSuffix(98) == "th"
