# Write a Python function named reverse to return the reversed word of a given word. You are not allowed to use string slicing or any string method or import any Python module here.

# For example  reverse("Python") returns "nohtyP" and reverse("madam") returns "madam".

# Please do the following:

# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (see assignment header for instructions)
# Write your function and write the function docstring
# Test your function in your main program for the two phrases, "madam" and "detartrated".

# Loop through each char of the str, starting index from the right to left
# Starting from the char at len(str)-1, add the char at that index to the previous char
# Return the reversed string

def reverse(str):
    """Loops through the str at each index from right to left and creates a reversed string"""
    new_str = ""
    for i in range(len(str)-1, -1, -1):
        new_str += str[i]
    return new_str


def main():
    print(reverse("madam"))
    print(reverse("detartrated"))


if __name__ == "__main__":
    main()
