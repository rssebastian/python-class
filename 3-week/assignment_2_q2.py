# Given an integer positive number with three digits, write a Python function named sum_of_digits to return the sum of all the digits. For example for the given number 123 the return value must be, 1 + 2 + 3 = 6. You must obtain this numerically; you are not allowed to use Python string operations and any module or external libraries. Do the following:

# Follow the UMPIRE process and write only the plan below (-5 points from Canvas total if missing or invalid)
# Write your function
# Write the docstring (-2 points from Canvas total if missing or invalid)
# In your main program, calculate and print the sum of digits of 234
# In your main program, calculate and print the sum of digits of 757

#   Understand - We are given an integer positive number with 3 digits and we need to return the sum of each of these digits
#   Match - Use mathematical logic to get the digits we want in an int
#   Plan - first_digit = digit // 100 % 10, second_digit = digit // 10 % 10, third_digit = digit % 10, return first_digit+second_digit_third_digit
#   Implement - Written below
#   Review - Test if function provides correct value on test cases
#   Evaluate - We can add a check to insure a_number is a valid input 0<1<1000

def sum_of_digits(a_number):
    """Calculates the sum of the digits in an integer positive number with 3 digits"""
    if (a_number <= 0 or a_number >= 1000):
        print("Unable to calculate")
        return
    first_digit = a_number // 100 % 10
    second_digit = a_number // 10 % 10
    third_digit = a_number % 10
    return first_digit + second_digit + third_digit
