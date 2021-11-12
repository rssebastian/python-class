# A retail company track down daily sales of a certain product as a number of product sold per day. The company stores the daily sales of 4 weeks as elements of a 2 dimensional list in which each row is a 7 day week in which each element is a number of products sold per respective date and week. Given the unit price of the product and assuming the price is fixed during the 4 weeks, write a Python function named, get_average_revenue to return the average daily revenue during the 4 week period. For example, weekly sales for the 4 weeks [[16, 24, 12, 4, 14, 6, 20], [20, 22, 10, 0, 16, 26, 12], [28, 24, 8, 0, 20, 2, 4], [12, 2, 16, 14, 28, 8, 18]] and for unit price, of $1025.00 the average daily revenues is $14130.36. Try doing this in just a single line of code using a list comprehension. Test your function for above sales list in your main program.

# Create a list of the average number of sales for each week in sales
# Sum up the elements of that list, and divide by the number of weeks in sales
# Multiply that average number of sales per day by the unit price
def get_average_revenue(sales, unit_price):
    """Returns the average daily revenue of a 2-D list representing weekly sales"""
    return round(sum([sum(week)/len(week) for week in sales])/len(sales)*unit_price, 2)


def main():
    sales = [[16, 24, 12, 4, 14, 6, 20], [20, 22, 10, 0, 16, 26, 12],
             [28, 24, 8, 0, 20, 2, 4], [12, 2, 16, 14, 28, 8, 18]]
    unit_price = 1025.00
    print(get_average_revenue(sales, unit_price))


if __name__ == "__main__":
    main()
