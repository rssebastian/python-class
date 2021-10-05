# Given two phrases, phrases1 and phrases2, two denominator numbers, denominator1 and denominator2, and a test integer number, test_integer write a Python function named get_phrase_if_divisible to return phrases1 if the test_integer is divisible by denominator1 without a remainder or return phrases2 if the test_integer is divisible by denominator2 without a remainder or return phrases1+phrase2 (Concatenate the two phrases as shown and return) if the test_integer is divisible by both denominator1 and denominator2 without a remainder or return exactly "Impossible == I'm possible" if otherwise. The default value for the  denominator1 and denominator2 is 1. Arrange your input to the function like, get_phrase_if_divisible(phrases1, phrase2, test_integer, denominator1, denominator2). Below are some example calls,

# get_phrase_if_divisible("Hocus", "Pocus", 33, 3, 11) and get_phrase_if_divisible("Hocus", "Pocus", 33) return "HocusPocus" whereas the call get_phrase_if_divisible("Hocus", "Pocus", 33, 3, 10) returns "Impossible == I'm possible".

# Please do the following:

# Please follow the UMPIRE to understand this problem (-5 points from Canvas total if missing or invalid)
# Write your algorithm as code comments
# Write your function:
# Write the function docstring (-2 points from Canvas total if missing or invalid)
# Comment your code where appropriate

# Plan: Return phrases1+phrases2 if test_integer % denominator1 == 0 and test_integer % denominator2 == 0,
# Otherwise, return phrases1 if test_integer % denominator1 == 0
# Or return phrases1 if test_integer % denominator1 == 0
# If all of these checks fail, return "Impossible == I'm possible"

def get_phrase_if_divisible(phrase1, phrase2, test_integer, denominator1=1, denominator2=1):
    """Returns a phrase depending on the test_integer's divisibility by the given denominators"""
    if (test_integer % denominator1 == 0 and test_integer % denominator2 == 0):
        return phrase1 + phrases2
    elif (test_integer % denominator1 == 0):
        return phrase1
    elif (test_integer % denominator2 == 0):
        return phrase2
    else:
        return "Impossible == I'm possible"
