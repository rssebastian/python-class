# Solutions to practice exam 1 coding question.
# Disclaimer: By writing my full name here, I here by declare and guarantee
# that this is my own original work.
# Your Fullname: Ryan Sebastian
#
# Please don't alter the function names. You are responsible for picking
# proper variables, parameters, arguments  and return values and writing
# docstrings and comments.

# Question #: 17
# Algorithm: Write your algorithm below
# Subtract 32 from input, multiply that by 5, divide that by 9, then add 273.15

# IMPLEMENT:
# Please do not change the name. However you are responsible for use of proper parameters and return values if necessary
def convert_fahrenheit_to_kelvin(fahrenheit_t):
    """Takes in a temperature in Fahrenheit units and converts it to Kelvin units"""
    return (fahrenheit_t-32) * 5 / 9 + 273.15


# Question #: 18
# Algorithm: Write your algorithm below
# if side1+side2 >= side3, side1+side3 >= side2, side2+side3 >= side1, then return True
# if any of these comparisons fail, the function should return False

# IMPLEMENT:
# Please do not change the name. However you are responsible for use of proper parameters and return values if necessary
def is_triangle_possible(side1, side2, side3):
    """Takes in 3 sides and checks if by triangle equality if the 3 sides create a valid triangle"""
    return side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1


# Question #: 19
# IMPLEMENT:
def print_numbers(number):
    """Prints multiple lines of numbers in decreasing length"""
    for i in range(1, number+1):
        for j in range(1, number+2-i):
            print(j, end=" ")
        print()


# Question #: 20
# Algorithm: Write your algorithm below
# default value of accumulator pi will be 3, if n=1, return pi
# use iterator to keep track of which term we are on
# if i = 1, return 3
# denominator will always equal (((i-1)*2) * ((i-1)*2+1) * ((i-1)*2+2))
# if i is even, add to accumulator, else, subtract it from the accumulator
# return accumulator


# IMPLEMENT:
def estimate_pi(n):  # Please do not change the name. However you are # responsible for use of proper parameters and return values if necessary
    """Estimates the value of pi given an n number of terms"""
    pi = 3
    if (n == 1):
        return pi
    elif (n <= 0):
        return ValueError
    else:
        for i in range(2, n+1):
            if (i % 2 == 0):
                pi += 4/(((i-1)*2) * ((i-1)*2+1) * ((i-1)*2+2))
            else:
                pi -= 4/(((i-1)*2) * ((i-1)*2+1) * ((i-1)*2+2))
        return pi


def main():
    print("Disclaimer: By writing my full name at the top, I here by declare "
          "and guarantee that this is my own original work. Please write "
          "your name before submit your code.")  # Please do
    # not delete this line. I
    print("Testing Q17:")
    fahrenheit_t = 98.4
    print("Kelvin temp. is: ", convert_fahrenheit_to_kelvin(fahrenheit_t), "\n")  #
    # Please make sure to place correct arguments
    print("End testing Q17. \n")

    print("Testing Q18:")
    side1 = 10
    side2 = 20
    side3 = 15
    print("This triangle is possible:",
          is_triangle_possible(side1, side2, side3), "\n")
    side1 = 4
    side2 = 4
    side3 = 10
    print("This triangle is possible:",
          is_triangle_possible(side1, side2, side3), "\n")
    # Please make sure to place correct arguments
    print("End testing Q18. \n")

    print("Testing Q19:")
    print(print_numbers(20), "\n")  # Please make sure place correct parameters
    print("End testing Q19. \n")

    print("Testing Q20:")
    print("Pi is for number of terms 5 ,",  estimate_pi(5), "\n")  # Please
    # make sure to place correct arguments

    print("Pi is for number of terms 20 ,",  estimate_pi(20), "\n")  # Please
    # make sure to place correct arguments
    print("End testing Q20. \n")


if __name__ == "__main__":
    main()
