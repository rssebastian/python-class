# 1. Given the diameter and the height, write a Python function named calculate_cylinder_volume to return (we solved very similar one in our last assignment but that time we didn't return a value. We printed it) the volume of the cylinder.
# The volume, v of a cylinder with diameter, d and height h is given by v=π*(d/2)^2*h. Do the following:
#   * Follow the UMPIRE process and write only the plan below (-5 points from Canvas total if missing or invalid)
#   * Write your function
#       * Write the docstring (-2 points from Canvas total if missing or invalid)
#   * In your main program, calculate the volume of a cylinder with the diameter and the height respectively 3 and 12 units. Convert your value to an integer and print it.
#
#   Understand - We are given the diameter and heigh of a cylinder, which are needed to calculate the volume of a cylinder, returning math.pi*(d/2)**2*h
#   Match - Using a given formula, calculate a value using provided inputs
#   Plan - Import the math module, Define the function properly, return the expected value
#   Implement - Written below
#   Review - Test if formula provides correct value on test cases
#   Evaluate - Nothing much to improve on, can probably omit the volume variable and return the expression for less lines
import math


def calculate_cylinder_volume(diameter, height):
    """Calculates the volume of a cylinder given the diameter and height"""
    volume = math.pi * (diameter/2) ** 2 * height
    return volume

# 2. Assume a soda can is a perfect cylinder. Write a Python function named count_soda_cans to return the number of soda cans of a given diameter and a given height that is required to be fully filled out of the given bulk volume amount of soda. Here you must use the function calculate_cylinder_volume you wrote above to calculate the volume of the soda can. Here is an example: assume the volume of a soda can calculated is 7.5 fluid ounce, and bulk  soda volume is 1000 ounce, you require 133 soda cans to fully fill them with soda. The left over amount is 2.5 soda ounce. Mathematically 1000 // 7.5 = 133.0. Do the following:
#   * Follow the UMPIRE process and write only the plan below (-5 points from Canvas total if missing or invalid)
#   * Write your function
#       * Write the docstring (-2 points from Canvas total if missing or invalid)
#       * Call calculate_cylinder_volume in your function (-5 points from Canvas total if missing)
#   * In your main program, calculate the required number of cans of diameter and the height respectively 3 and 12 units that can be fully filled by a bulk amount of soda volume of 1200 units. Convert your value to an integer and print it.
#   Understand - We are given the diameter and height of a cylinder, which are needed to calculate the volume of our soda cans
#                Then we need to see how many of cans we need to contain the amount of soda, which is also given as an argument
#   Match - Using a given formula, calculate a value using provided inputs
#   Plan - Use calculate_cylinder_volume to find the volume of our cans, divide the volume of soda by the volume of cans to find how many cans we need, round up since we cannot have fractions of cans
#   Implement - Written below
#   Review - Test if function provides correct value on test cases
#   Evaluate - Nothing much to improve on, can probably omit the volume variable and return the expression for less lines
#   CodeCheck does not take into account the need to round up after calculating the number cans needed. Wrapping expression in math.ceil() removed


def count_soda_cans(diameter, height, soda_volume):
    """Using calculate_cylinder_volume, calculates the number of cans needed to store the given soda_volume"""
    number_of_cans = math.ceil(
        soda_volume / calculate_cylinder_volume(diameter, height))
    return number_of_cans


# 3. Write a Python function named calculate_revenue to calculate total sale price of a given amount of product of a given unit price. There is discount per item sold. The default discount amount is $0.00 per item sold. Do the following:
#   * Follow the UMPIRE process and write only the plan below (-5 points from Canvas total if missing or invalid)
#   * Write your function
#       * Write the docstring (-2 points from Canvas total if missing or invalid)
#   * In your main program,calculate the revenues of selling 50 soda cans worth $1.20 each with no discount. Convert your value to an integer and print it
#   * In your main program, calculate the revenues of selling 500 soda cans worth $1.20 each with a discount of $0.10 per can. Convert your value to an integer and print it
#   Understand - Calculate the amount of money earned by taking the (unit_price - discount) * number_of_units_sold
#   Match - Using a given formula, calculate a value using provided inputs
#   Plan - Use the (unit_price - discount) as the price per can, multiply by number of can(s) sold to find the total earned
#   Implement - Written below
#   Review - Test if formula provides correct value on test cases
#   Evaluate - Nothing much to improve on, output can be float


def calculate_revenue(unit_price, number_of_units_sold, discount=0.0):
    """Calculates the amount earned after applying a discount on the unit_price, then multiplying by the number sold"""
    return (unit_price - discount) * number_of_units_sold
