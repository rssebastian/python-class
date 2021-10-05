# Given a four digit positive integer number with nonzero digits, write a Python functions named reverse_ends_number to return the integer number created by putting the two end digits in reverse order. For example, for the given number, 4325, reverse_ends_number(4325) must return 54 because when we extract the digits 5 ans 4 and put them together we can form 54. You are not allowed to use math module or any string operations or any other Python library or module here.

# Please do the following:

# Please follow the UMPIRE to understand this problem (-5 points from Canvas total if missing or invalid)
# Write your algorithm as code comments
# Write your function:
# Write the function docstring (-2 points from Canvas total if missing or invalid)
# Comment your code where appropriate

# Plan: get first digit by taking a_number // 1000, the last digit by a_number % 10, and return last_digit*10 + first_digit
def reverse_ends_number(a_number):
    """Returns the integer number putting the two end digits in reverse order"""
    first_digit = a_number // 1000
    last_digit = a_number % 10
    return last_digit*10 + first_digit
