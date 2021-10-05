# Given the year number, write a Python function named is_leap_year,  to return True if the year is a leap year or False otherwise. Make the current year, 2021 as the default year.

# For example your calls, is_leap_year(1600) must return True, is_leap_year(1900) must return False , is_leap_year(2012) must return True and is_leap_year()  must return False.  The rules for a leap year in Gregorian calendar are as follows:

# a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
# a year is always a leap year if its number is exactly divisible by 400
# Please do the following:

# Please follow the UMPIRE to understand this problem (-5 points from Canvas total if missing or invalid)
# Write your algorithm as code comments
# Write your function:
# Write the function docstring (-2 points from Canvas total if missing or invalid)
# Comment your code where appropriate

# Plan: Take the year input, return True if year % 400 == 0, otherwise, check if year % 4 == 0, and if year % 100 !=0. Return True if both of the conditions pass or False if either fail

def is_leap_year(year=2021):
    """Returns True or False if the inputted year is a leap year given the Gregorian calendar conditions"""
    if (year % 400 == 0):
        return True
    if (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
