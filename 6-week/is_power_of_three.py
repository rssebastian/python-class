# Given a positive integer number (<= 318 = 387420489), write a Python function named is_power_of_three to return whether the number is an integer power of 3 or not. Try doing this using a single line of code without using a loop or math module.

# For example,  your call,  is_power_of_three(81) must return True because 34 = 81.

# Please do the following:

# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (see assignment header for instructions)
# Write your function and write the function docstring
# Test your function in your main program for the numbers 27, 177147 and 4782976

# Check if the number is divisible by 3 first
# Then check if the last digit is 3, 9, 7, or 1
# Each power of 3 will have their last digits cycle between these 4
# If both conditions pass, return True, and False if not
def is_power_of_three(n):
    """Returns if n is a power of 3"""
    return True if (n % 3 == 0) and (n % 10 == 3 or n % 10 == 9 or n % 10 == 7 or n % 10 == 1) else False


def main():
    print(is_power_of_three(27))
    print(is_power_of_three(177147))
    print(is_power_of_three(4782976))
    print(is_power_of_three(3))
    print(is_power_of_three(9))
    print(is_power_of_three(27))
    print(is_power_of_three(81))
    print(is_power_of_three(243))
    print(is_power_of_three(24))
    print(is_power_of_three(33))
    print(is_power_of_three(60))


if __name__ == "__main__":
    main()
