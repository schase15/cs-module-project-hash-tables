'''
Plan:
    Put each word into a dictionary
    Don't add duplicates
    Return the keys into a list
    Return a string of the keys separated by spaces 
'''

def no_dups(s):
    # Split input text into words
    words = s.split()

    # Put each word into a dict
    d = {}

    for word in words:
        d[word] = 0

    word_list = list(d.keys())

    # Put in proper output format
        # joins each item in the list with a space in between
    string_result = " ".join(word_list)

    return string_result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
