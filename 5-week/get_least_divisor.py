# Given a positive integer number grater than 2, write a Python function named get_least_divisor that uses a while loop to return the least integer number that divide the input number evenly without a remainder. For example given the number 30 your function must return 2 where as for 31 your function must return 31. More test cases are below. You are not allowed to use math module or any string operations or any other Python library or module here.

# Have loop run while i <= n
# Initialize i at 2
# If n % i == 0, return i
# If not, incrememnt i and run again
# if i == n, then return i

def get_least_divisor(n):
    """Finds the least common divisor of n besides 1"""
    i = 2
    while i < n:
        if n % i == 0:
            return i
        else:
            i += 1
            if i == n:
                return i


def main():
    a_number = 17
    print(get_least_divisor(a_number))
    a_number = 81
    print(get_least_divisor(a_number))
    a_number = 40
    print(get_least_divisor(a_number))
    a_number = 221
    print(get_least_divisor(a_number))


if __name__ == "__main__":
    main()
