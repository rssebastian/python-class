# Given a string phrase, and a number of rounds, write a Python function named rotate_clockwise to rotate the phrase clockwise with the given number of rounds. String clockwise rotation means removal of the characters from the front and adding them from the back one after the other as many number of rounds given. Note that the number of rounds can be any positive integer number greater than or equal to zero.

# For example the string "Python" is rotated clockwise two times (your call rotate_clockwise("Python", 2)) means the resulting string is "thonPy" and your call rotate_clockwise("code", 9)) must return "odec" and rotate_clockwise("code", 4) must return "code".

# Please do the following:

# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (see assignment header for instructions)
# Write your function and write the function docstring
# Test your function in your main program for the phrase "Python" for round of rotations, 3 and "Code" for round of rotations, 12

# Add edge case if str is null or if rotations == 0
# Rotate string rotation % len(str) times, in case the number of rotations exceeds str length
# Take a slice of the string at the index num == number of rotations until the end of the string
# Concatenate it with a slice of the beginning of the string until the index num (excluding)

def rotate_string(str, rotations):
    if rotations == 0 or str == "":
        return str
    rotations = rotations % len(str)
    return str[rotations::] + str[:rotations]


def main():
    print(rotate_string("Python", 3))
    print(rotate_string("Code", 12))


if __name__ == "__main__":
    main()
