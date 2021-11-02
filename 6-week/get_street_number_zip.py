# Given a postal address, write a Python function named get_street_number_zip to return the street number and the zip code as a pair (a tuple of two things), (street number, zip code). You can assume every street address has the format shown in the example below with street numbers of any number of digits. You must also thrive to minimize the number of loop iterations. You are not allowed to import any Python module. Assume all zip codes have only 5 digits. Note that the two return numbers are in integer type.

# For example,  your call, get_street_number_zip("415 Bell st, Houston, TX 77023") must return (415, 77023).

# Please do the following:

# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (see assignment header for instructions)
# Write your function and write the function docstring
# Test your function in your main program for the addresses, "415 Bell st, Houston, TX 77023" and  "8800 Stone st, Houston, TX 77023"

# The last 5 characters will be zipcode, store address[-5::1] as the zip_code
# The charcters prior to the first " " will be street number
# Loop through the string until the first " " and add each char to a street_number string
# return the tuple after each variable is cast to int (int(street_number), int(zip_code))

def get_street_number_zip(address):
    """Returns the street number and zip code as a tuple from an address string"""
    zip_code = address[-5::1]
    street_number = ""
    for idx, char in enumerate(address):
        street_number += char
        if address[idx + 1] == " ":
            break
    return (int(street_number), int(zip_code))


def main():
    print(get_street_number_zip("415 Bell st, Houston, TX 77023"))
    print(get_street_number_zip("8800 Stone st, Houston, TX 77023"))


if __name__ == "__main__":
    main()
