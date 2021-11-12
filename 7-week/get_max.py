# Given a list of numbers, write a Python function named, get_max to return the largest number inside. Here you are not allowed to use, built-in methods except len(), any list method or import any Python module. For example, given the list, [2, 287, 34, 67, 899, 10], your function must return 899. Test your function for this list in your main program.

# Store the first element of the list as the potential maximum number
# Iterate over the list and check if the following element is greater than the current stored value
# If it is, replace the current stored value with the larger element. Do nothing if it's equal or smaller
# After iterating throught the list, return the stored value
def get_max(x):
    """Returns the largest number inside the list"""
    max_num = x[0]
    for el in x:
        if max_num < el:
            max_num = el
    return max_num


def main():
    print(get_max([2, 287, 34, 67, 899, 10]))


if __name__ == "__main__":
    main()
