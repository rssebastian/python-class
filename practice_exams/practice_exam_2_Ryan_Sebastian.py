# Solutions to practice exam 2 coding questions.
# Disclaimer: By writing my full name here, I here by declare and guarantee
# that this is my own original work.
# Your Fullname: <please write your full name here>
#
# Please don't alter the function names. You are responsible for picking
# proper variables, parameters, arguments  and return values and writing
# docstrings and comments.

# Question #: 16
# Algorithm: Write your algorithm below
# Create a new list using list comprehension and the expression el ** power

# IMPLEMENT:
def get_powers(a_list, power):  # Please do not change the name. However
    # you are responsible for use of proper parameters and return values if
    # necessary
    """Returns a list of each element in a_list raised by the power given"""
    return [el ** power for el in a_list]


# Question #: 17
# Algorithm: Write your algorithm below
# Create a list of numbers to iterate over
# Create the first list by making a list out of the range from 1 to len(str)
# Create the second list by making a list out of the range from -1 to len(str) * -1
# Concatenate both lists and this will represent the end index we need to slice to
# Print the slice of the string from [:idx]


# IMPLEMENT:
def print_pattern(str):  # Please do not change the name. However you are
    # responsible for use of proper parameters and return values if necessary
    """Prints pyramid pattern of str using only 1 for loop and string slicing operation"""
    list1 = list(range(1,len(str) + 1))
    list2 = list(range(-1,len(str) * -1, -1))
    idxList = list1 + list2
    for idx in idxList:
        print(str[:idx])


# Question #: 18
# Set up 3 parameters: unit_price, num_units, discount
# Set the parameter of discount to ""
# Calculate base price before any discount
# If discount is not "", check if discount == "3m", "2m", "1m"
# Apply the appropriate discount in an if-elif-else clause and return new price
# Otherwise, return base price

# IMPLEMENT:
def calculate_price(unit_price, num_units, discount=""):
    # Please do not change the name. However you are
    # responsible for use of proper parameters and return values if necessary
    """Calculates the total price of a product with possible discount"""
    base_price = unit_price * num_units
    if discount:
        if discount == "3m":
            return base_price * 0.95
        elif discount == "2m":
            return base_price * 0.90
        elif discount == "1m":
            return base_price * 0.85
    return base_price


# Question #: 19
# Algorithm: Write your algorithm below
# Set whichever list has the smaller length to short list, and the other to long_list
# Return list comprehension of the short list if the element is also present in long_list


# IMPLEMENT:
def get_intersection(list1, list2):  # Please do not change the name. However you are
    # responsible for use of proper parameters and return values if necessary
    """Returns the intersection of two lists"""
    if len(list1)<=len(list2):
        short_list = list1
        long_list = list2
    else:
        short_list = list2
        long_list = list1
    return [el for el in short_list if el in long_list]

# Question #: 20
# Algorithm: Write your algorithm below
# Calculate the average of the elements in the list by accumulating each element and dividing by the length
# Create a single element list of the average
# Concatenate it with a slice of the original list

# IMPLEMENT:
def get_average_priority_list(a_list):  # Please do not change the name. However
    # you are responsible for use of proper parameters and return values if
    # necessary
    """Returns the priority list with the average of the list as the first element"""
    sum = 0
    for num in a_list:
        sum += num
    average = sum / len(a_list)
    return [average] + a_list[:]


def main():
    print("Disclaimer: By writing my full name at the top, I here by declare "
          "and guarantee that this is my own original work. Please write "
          "your name before submit your code.")  # Please do
    # not delete this line. I
    print("Testing Q16:")
    print("The powers are: ", get_powers([2, 7, 8, 1, 6], 4), "\n")  #
    # Please make sure to place correct arguments
    print("End testing Q16. \n")

    print("Testing Q17:")
    print_pattern("programming")
    # Please make sure to place correct arguments
    print("\nEnd testing Q17. \n")

    print("Testing Q18:")
    print("Price for one time purchase: ", calculate_price(1.00, 10),
          "\n")  # Please make sure place correct parameters
    print("Price for once a moth subscription: ", calculate_price(1.00, 10, "1m"),
          "\n")  # Please make sure place correct parameters
    print("End testing Q18. \n")

    print("Testing Q19:")
    list1 = ['a', "code", 1, 46, 50, [1, 2, 3]]
    list2 = ['b', "code", 46, [1, 2]]
    print("The intersection is: ,", get_intersection(list1, list2), "\n")  # Please
    # make sure to place correct arguments
    print("End testing Q19. \n")

    print("Testing Q20:")
    print("The average priority list is ,", get_average_priority_list([15, 24, 25, 75, 34, 67, 65, 89, 98, 88, 68]),
          "\n")  # Please make sure to place correct arguments
    print("End testing Q20. \n")


if __name__ == "__main__":
    main()
