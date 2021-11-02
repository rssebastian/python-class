# Given a web url, write a Python function named is_secure_site to return whether the url is secure or not. According to the internet protocol, a secure web address starts with https whereas non-secure web address starts with http. Based on your check, your function must return only a boolean value.

# For example https://peralta.instructure.com/ is a secure web page and you must return True whereas http://pythontutor.com/ (Links to an external site.) is not and you must return False. You are not allowed to use any string method or import any Python module.

# Please do the following:

# Please write your Canvas full name and LMS ID as code comments in CodeCheck
# Please follow the UMPIRE technique to understand this problem and write your algorithm as code comments (see assignment header for instructions)
# Write your function and write the function docstring
# Test your function in your main program for above two websites.

# Get the first 5 characters of the URL by getting a slice of the string [:5]
# Return True if they match https, False if not
def is_secure_site(url):
    """Returns True if the first 5 characters of the url are https, False if not"""
    if url[:5] == 'https':
        return True
    else:
        return False


def main():
    print(is_secure_site("https://peralta.instructure.com/"))
    print(is_secure_site("http://pythontutor.com/"))


if __name__ == "__main__":
    main()
