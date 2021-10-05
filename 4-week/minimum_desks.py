# A kindergarten classroom sits maximum 4 students at one desk. Given the number of kindergarten student enrolled, write a python function named calculate_minimum_desks to calculate the minimum number of desks required to sit all the students. For example, for a classroom with 27 students, the call calculate_minimum_desks(27) must return 7. You are not allowed to use string operations here.

# Please do the following:

# Please follow the UMPIRE to understand this problem (-5 points from Canvas total if missing or invalid).
# Write your algorithm as code comments
# Write your function:
# Write the function docstring (-2 points from Canvas total if missing or invalid)
# Comment your code where appropriate

import math
# Plan: if no_of_students / 4 has a non-zero remainder, add 1 to the floor division to ensure enough space, otherwise, return no_of_students/4


def calculate_minimum_desks(no_of_students):
    """Calculates the minimum number or desks needed to support the number of students"""
    if (no_of_students % 4 != 0):
        return no_of_students // 4 + 1
    else:
        return no_of_students % 4
