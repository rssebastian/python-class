# Given a set of x coordinates as a list, write a Python function named get_y that returns  the list of corresponding y coordinates list according to the quadratic formula, y=x2+2x+3 using list comprehension. For example, given x = [1, 2, 3], your function must return = [(12 + 2*1 + 3), (22 + 2*2 + 3), (32, 2*3 + 3)] = [6, 11, 18]. Test your function for the list, [-1, 3, 5] in your main program.
# Given a word, a_word, write a Python function named get_ord_list to return the list of corresponding ordinal values,  (ord()) of each character  using list comprehension. For example, given the word "programming" your function must return [112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]. Test your function for the phrase "Python code" in your main program.
# Given a list of both numbers and strings, write a Python function named multiply_list to return a list of multiplications or the repetitions of the values of the list by a given number using list comprehension. For example, given the [2, 4, "A", "N"] and the multiplier, 3, your function must return [6, 12, "AAA", "NNN"]. Test your function for the list, ['a', 'b', 1, 2, "to"] to multiply values by 2 in your main program.
# Given a list, write Python function named get_even_indexed_list to return a list of all elements that has an even index  using list comprehension. For example, given the list [5, 3, 2, 8, "code", 'a', 20], your function must return [5, 2, 'code', 20]. Test your function for the list, [4, 7, 8, 1, "p", "q"] in your main program.
# Given a paragraph of text, write a python function named extract_numbers to return a list of numbers (must be numbers ie not in string format) in the phrase. For example, given the paragraph, "Steph Curry recorded 50 points and 10 assists for the first time in his career, overtaking Wilt Chamberlain as the oldest player in NBA history to do so, as the Golden State Warriors continued their blistering start to the season with a 127 to 113 victory over the Atlanta Hawks on Monday." your function must return [50.0, 10.0, 127.0, 113.0]. Test your function for above paragraph in your main program.

def get_y(x):
    return [el ** 2 + 2 * el + 3 for el in x]


def get_ord_list(phrase):
    return [ord(a_word) for a_word in phrase]


def multiply_list(a_list, multiplier):
    return [el * multiplier for el in a_list]


def get_even_indexed_list(a_list):
    return [el for el in a_list if a_list.index(el) % 2 == 0]


def extract_numbers(paragraph):
    return [float(el) for el in paragraph.split() if str.isnumeric(el)]


def main():
    print(get_y([-1, 3, 5]))
    print(get_ord_list("Python code"))
    print(multiply_list(['a', 'b', 1, 2, "to"], 2))
    print(get_even_indexed_list([4, 7, 8, 1, "p", "q"]))
    paragraph = "Steph Curry recorded 50 points and 10 assists for the first time in his career, overtaking Wilt Chamberlain as the oldest player in NBA history to do so, as the Golden State Warriors continued their blistering start to the season with a 127 to 113 victory over the Atlanta Hawks on Monday."
    print(extract_numbers(paragraph))


if __name__ == "__main__":
    main()
