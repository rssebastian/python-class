# Multiplication between two integer positive numbers can be interpreted as a summation problem. For example 3 * 7 = 21 can be written as 7 + 7 + 7 = 21. You must follow the least number of iterations. This means you must figure the smallest of the two numbers. In other words, in above example, 3 + 3+ 3+ 3+3+ 3+ 3 = 21 is not a valid solution. Use of direct multiplication here will result zero points for this question.

# Store the num1 in bigger_num if num1 >= num_2, or num2 if num2 is bigger
# Initialize accumulator to equal bigger_num
# Store num1 or num2 in smaller_num, whichever didn't get used yet
# iterate over range(smaller_num - 1)
# each iteration, add bigger_num to the accumulator
# return accumulator

def get_product_via_sum(num1, num2):
    """Finds the product of two numbers by adding num1 to itself num2 times, or the other way around"""
    bigger_num = num1 if (num1 >= num2) else num2
    smaller_num = num1 if (bigger_num != num1) else num2
    acc_sum = 0
    for i in range(smaller_num):
        acc_sum += bigger_num
    return acc_sum


def main():
    number_1 = 3
    number_2 = 5
    print(get_product_via_sum(number_1, number_2))
    number_1 = 5
    number_2 = 11
    print(get_product_via_sum(number_1, number_2))


if ___name__ == "__main__":
    main()
