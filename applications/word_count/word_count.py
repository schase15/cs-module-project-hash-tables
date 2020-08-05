# Already did this with the histo.py example

# Only works on 3 out of 5 test
    # I think the test is wrong, In the second one, "Hello   hello", there are no special characters
    # so it should return a blank dictionary, not 'hello' : 2

    # For the last test, python already ignores \'s and the following letter so it 
    # Returns no special characters removed


def word_count(s):
    '''
    Take in string
    Strip any punctuation away
        If the input contains no ignored characters, return an empty dictionary
    Split on whitespaces
    Add to dictionary while counting
    '''

    charac_ignore = ' " : ; , . - + = / \ | [ ] } { ( ) * ^ &  '.split(' ')

    print(charac_ignore)

    ## Clean the punctuation out
    # Blank string to filter cleaned text into
    empty_string = ""

    # Count if special characters are removed, if this is equal to 0 at the end,
    # print out empty dictionary
    removed = 0

    # Filter out all of the punctuation
    for c in s:

        # Ignore punctuation
        if c in charac_ignore:
            # count if special characters are removed 
            removed += 1 
            continue

        # Make it all lower case
        c = c.lower()

        # Add it to the blank string
        empty_string += c

    # Empty dictionary to store word and the count
    d = {}  

    # If no special characaters are removed, return empty dictionary
    if removed == 0:
        print('No special characters removed')
        return d

    # Split the string into a list of individual words - split on whitespace
    arr = empty_string.split()

    # Iterate through the split words array, count the occurance of each word
    for word in arr:
        # If the word isn't in the dictionary, add it
        if word not in d:
            d[word] = 0
        
        # Increment the count
        d[word] += 1

    # Return the dictionary
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))