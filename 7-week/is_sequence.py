# Write a Python function named is_sequence to check whether a given value is a sequence (let us limit to a list, a string, a range or a tuple for now) or not. For example for the values like 3.14 and 10 your function must return False as 3.14 and 10 are not sequences whereas for values like [], [1, 2], (2, 3), "code", range(4) and "" your function must return True as these values are sequences. Test your function for the items in the list, [3.14, 10, [], [1, 2], (2, 3),
# "code", range(4), ""] in your main program. Try doing this in a single line of code after your function docstring.

# Return True in is_sequence if the value is either a str, tuple, list, or range
# Iterate over each element in a_list
# If it is one of the 4 possible sequences, turn that sequence into a list and print each value separated by a comma
# If not, just print the element by itself

def is_sequence(value):
    """Checks whether a given value is a sequence or not"""
    return (type(value) == str or type(value) == tuple or type(value) == list or type(value) == range)


def print_content(a_list):
    """Prints the content of a_list one element at a time"""
    for el in a_list:
        if is_sequence(el):
            for x in list(el):
                print(x, end=", ")
            print()
        else:
            print(el)


def main():
    print([is_sequence(el)
          for el in [3.14, 10, [], [1, 2], (2, 3), "code", range(4), ""]])
    print_content([2, [2, 3, 4], "code",
                   ('a', 'b', 'c'), range(4, 1, -1), 10])


if __name__ == "__main__":
    main()
