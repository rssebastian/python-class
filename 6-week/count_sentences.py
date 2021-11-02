# Given an English paragraph of text, write a Python function named, count_sentences to count number of sentences in the paragraph. In English usually exclamation (!), question mark (?) and the period(.) ends a sentence. You may assume that any English paragraph ends with a period. You are not allowed to use any string method or import any Python module.

# For example, given the paragraph, paragraph = "Python is very versatile! It provide more functionalities than many other languages. Did you know that Python is very close to English language? The latest version, version 3.10 is awesome."  Your call, count_sentences(paragraph) , must return 4.

# Please do the following:

# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (see assignment header for instructions)
# Write your function and write the function docstring
# Test your function in your main program for these great quotes by Helen Keller, "Security is mostly a superstition. It does not exist in nature, nor do the children of men as a whole experience it. Avoiding danger is no safer in the long run than outright exposure. Life is either a daring adventure, or nothing." and by Michael Faraday “The force of the temptation which urges us to seek for such evidence and appearances as are in favour of our desires, and to disregard those which oppose them, is wonderfully great. In this respect we are all, more or less, active promoters of error. In place of practising wholesome self-abnegation, we ever make the wish the father to the thought: we receive as friendly that which agrees with, we resist with dislike that which opposes us; whereas the very reverse is required by every dictate of common sense.”.

# Create counter to keep track of index as we loop through paragraph
# Create counter to keep track of the number of ., !, and ?
# Increment the second counter if the char at the first counter index matches and check if a " " follows or if it's the end of the string
# Return the second counter once we've looped through the whole paragraph

def count_sentences(paragraph):
    """Returns the number of sentences in a string paragraph"""
    i = 0
    num_sentences = 0
    while i < len(paragraph):
        if (paragraph[i] == "." or paragraph[i] == "?" or paragraph[i] == "!") and (i+1 == len(paragraph) or paragraph[i+1] == " "):
            num_sentences += 1
        i += 1
    return num_sentences


def main():
    paragraph = "Security is mostly a superstition. It does not exist in nature, nor do the children of men as a whole experience it. Avoiding danger is no safer in the long run than outright exposure. Life is either a daring adventure, or nothing."
    print(count_sentences(paragraph))
    paragraph = "The force of the temptation which urges us to seek for such evidence and appearances as are in favour of our desires, and to disregard those which oppose them, is wonderfully great. In this respect we are all, more or less, active promoters of error. In place of practising wholesome self-abnegation, we ever make the wish the father to the thought: we receive as friendly that which agrees with, we resist with dislike that which opposes us; whereas the very reverse is required by every dictate of common sense."
    print(count_sentences(paragraph))
    paragraph = "Python is very versatile! It provide more functionalities than many other languages. Did you know that Python is very close to English language? The latest version, version 3.10 is awesome."
    print(count_sentences(paragraph))


if __name__ == "__main__":
    main()
