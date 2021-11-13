# To search an item in a sorted list, you could use the in operator, but it would be slow because it searches through the entire list. So in the worse case in which the search key is at the very end of the list, we'd have to iterate the entire list to find the search key. We call this linear search as the search time grows linearly with the size of the list. Now imagine the length of your sorted list is 4194304 roughly 4.2 million, then our linear algorithm now has to iterate  4194304 times to find the search key in the worse case.

# Wouldn't it be great if we can reduce the worse case number of iteration to just 22 (222 = 4194304 so log2(4194304) = 22 ) in above list? Because the entities are in sorted order, we can speed things up with dividing the list by half in each iteration and searching only in the half of the list that is the key must be possible to find. We call this binary search algorithm. This documentation (Links to an external site.) clearly animate how binary search works. Please read it and play the animation. You will also find the algorithm there. This way solving problems in computer science is called divide and conquer paradigm.

# Given a sorted list of numbers, write a function named binary_search to search for a given key. If found, your function must return the respective index of search item. If not found, it must return -1. In the case of duplicates, you are not restricted to return the index of the first occurance. However, you are highly encouraged to return the index of the first occurrence. For example for the list, [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 30], your function must return 7 for search key 22, 0 for the search key 8 and -1 for search key 13. Use your function to search for 26 in above list in
# your main program.

# Initialize start, end, and mid pointers to track where we have checked
# Start is 0, end is last index of list, mid is the middle index, floored if the list has an even number of elements
# Use while loop to keep track if answer has been found
# If the element at the mid index is the key, end the loop and return the mid index
# If the element at the mid index is less than the key, move the end to the index before the mid and repeat the search
# If the element at the mid index is larger than the key, move the start to the index after the mid and repeat the search
# If the start and end point ever equal or if the end becomes smaller than the start, the search failed, loop is ended, and -1 is returned

def binary_search(sorted_list_of_numbers, key):
    start = 0
    end = len(sorted_list_of_numbers)-1
    mid = (start + end) // 2
    idx = 0
    found = False
    while not found:
        if sorted_list_of_numbers[mid] == key:
            idx = mid
            found = True
        elif start >= end:
            idx = -1
            found = True
        elif sorted_list_of_numbers[mid] > key:
            end = mid - 1
            mid = (start + end) // 2
        elif sorted_list_of_numbers[mid] < key:
            start = mid + 1
            mid = (start + end) // 2
    return idx


def main():
    print(binary_search([8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 30], 22))
    print(binary_search([8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 30], 8))
    print(binary_search([8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 30], 13))


if __name__ == "__main__":
    main()
