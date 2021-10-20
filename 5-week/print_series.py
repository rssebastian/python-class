# Given three numbers, start, stop and step (start < stop, step < stop), write a Python function named, print_series to print the sequence of numbers from start to stop both inclusive in steps as a comma separated series of numbers. Make the default stop value to 1. For example for the start = 3, stop = 26 and step = 2, your call,  print_series(3, 26, 2) must print 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,  whereas your call print_series(3, 26) must print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,  .
# Please note the separation by single commas and a spaces all the way to the end. You must use a looping technique here.

# Please do the following:

# Please write your Canvas full name and LMS ID as code comments in CodeCheck
# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (-5 points from Canvas total if missing or invalid)
# Write your function and write the function docstring (-2 points from Canvas total if missing or invalid)
# Comment your code where appropriate
# Test your function in your main program for start = 4, stop = 45 and step = 7.

# Use start, stop, and step values to create a range
# turn range into a list with list()
# iterate over each value of the list and print each number

def print_series(start, stop, step=1):
    """Function that creates a range from start to stop (inclusive) and prints each value"""
    series = list(range(start, stop+1, step))
    for num in series:
        print(num, end=", ")


def main():
    start = 1
    stop = 26
    step = 2
    print_series(start, stop, step)
    print()
    print_series(start, stop)
    start = 4
    stop = 45
    step = 7
    print_series(start, stop, step)


if __name__ == "__main__":
    main()
