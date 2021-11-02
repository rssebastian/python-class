# Solutions to Exam 1 coding question.
# Disclaimer: By writing my full name here, I here by declare and guarantee
# that this is my own original work.
# Your Fullname: Ryan Sebastian

# Please don't alter the function names.
# You are responsible for picking proper variables, parameters and return
# values and writing docstrings and comments.

# Question #: 17
# IMPLEMENT:


def prg_question_1(kelvin_t):
    """Converts an input of Kelvin temperature units to Fahrenheit units"""
    fahrenheit_t = (kelvin_t - 273.15) * 9 / 5 + 32
    return fahrenheit_t


# Question #: 18
# ================================UMPIRE========================================
# Understand: Given the condition the coefficients of a quadratic equation must satisfy to have real roots, (b ** 2 - 4 * a * c), check if a, b, and c are greater than or equal to zero.
# Question: Use given formula to see if arguments return the expected value


# PLAN:
# Algorithm: Write your algorithm below
# Set up parameters a, b, and c
# Return the boolean value of (b ** 2 - 4 * a * c) >= 0

# IMPLEMENT:
def prg_question_2(a, b, c):
    return (b ** 2 - 4 * a * c) >= 0

# Question #: 19
# ================================UMPIRE========================================
# Understand: Plug in the appropriate values for "your code goes here" in order to print number rows of number sequences from number to 1
# Question: Use correct values for the range function to print the desired ranges from 1 to number


# PLAN:
# Algorithm: Write your algorithm below
# Replace the first "your code goes here" with number + 1, since there will be number rows
# The second "your code goes here" should have a start of number+1-i since it decreases each iteration of i, end of 0, and step of -1

# IMPLEMENT:
def prg_question_3(number):
    """Prints multiple sequences of numbers in decreasing number of terms"""
    for i in range(1, number+1):  # prints the rows
        for j in range(number+1-i, 0, -1):  # prints each number in a row
            print(j, end=" ")
        print()


prg_question_3(9)  # Prints above numbers set


# Question #: 20
# ================================UMPIRE========================================
# Understand: Use the formula for pi as a series expansion to determine the estimated value of pi given n number of terms
# Question: Use given formula to see if arguments return the expected value

# PLAN:
# Algorithm: Write your algorithm below
# import math module
# Create accumulator to store the summation series
# Create a loop to iterate n times and for each iteration, add to the accumulator 1/i**2
# Return the square root of (6 * accumulator)


# IMPLEMENT:

import math
def prg_question_4(n):
    acc = 0
    for i in range(1, n):
        acc += 1 / i ** 2
    return math.sqrt(6 * acc)


def main():
    print("Disclaimer: By writing my full name at the top, I here by declare "
          "and guarantee that this is my own original work.")  # Please do
    # not delete this line.
    print("Testing Q17:")
    # Test 1
    print("Answer to Q17 test 1 is:", prg_question_1(300), "\n")  # Please
    # make sure to place correct parameters
    print("End testing Q17. \n")

    print("Testing Q18:")
    # Test 1
    print("Answer to Q18 test 1 is:", prg_question_2(1, 5, 6), "\n")  # Please
    # make sure place correct parameters
    # Test 2
    print("Answer to Q18 test 2 is:", prg_question_2(1, 1, 1), "\n")  # Please
    # make sure place correct parameters
    print("End testing Q18. \n")

    print("Testing Q19:")
    prg_question_3(20)  # Please make sure to place correct parameters
    print("End testing Q19. \n")

    print("Testing Q20:")
    # Test 1
    print("Answer to Q20 test 1 is:",  prg_question_4(5), "\n")  # Please
    # make sure to place correct parameters
    # Test 2
    print("Answer to Q20 test 2 is:",  prg_question_4(20), "\n")  # Please
    # make sure to place correct parameters
    print("End testing Q20. \n")


if __name__ == "__main__":
    main()
