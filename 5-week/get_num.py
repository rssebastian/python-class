# Write a Python function named, get_sum to return the sum of n terms of the series sum given below:

# 12 + 22 + 32 + 42 + 52 + . ... + i2 +  ... + n2 .

# You must use a looping technique to solve this problem. Do not use the direct formula to solve this problem. Also, you may not use recursion here as we haven't learn it in this class.

# Please do the following:

# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (-5 points from Canvas total if missing or invalid)
# Write your function and write the function docstring (-2 points from Canvas total if missing or invalid)
# Comment your code where appropriate
# Test your function in your main program for n = 10 and verify it with the direct formula given by  n * (n + 1) * (2n + 1) / 6.

# Create accumulator to hold the sum of n terms
# iterate over a range of 1 to n
# add i^2 to the accumulator until we reach n

def get_sum(n):
    """return the sum of n terms of the series sum of 1 to n"""
    acc_sum = 0
    for i in range(1, n+1):
        acc_sum += i ** 2
    return acc_sum


def main():
    n = 10
    print(get_sum(n))
    print()
    direct_sum = n * (n + 1) * (2 * n + 1) / 6
    print(direct_sum == get_sum(n))


if __name__ == "__main__":
    main()
