'''
Print out a histogram made from hashtags to represent the freq. of each word in a string
Count each word
Print histogram by multiplying # by the count
'''

# Function takes in a file name
def word_hist(txt):
    # Characters to ignore
    charac_ignore = ' " : ; , . - + = / \ | [ ] } { ( ) * ^ &  '.split(' ')

    # Read in the text of the input file name
    with open(txt) as file:
        text = file.read()

    ## Clean the punctuation out
    # Blank string to filter cleaned text into
    s = ""

    # Count if special characters are removed, if this is equal to 0 at the end, print out nothing
    removed = 0

    # Filter out all of the punctuation
    for c in text:

        # Ignore punctuation
        if c in charac_ignore:
            # count if special characters are removed 
            removed += 1 
            continue

        # Make it all lower case
        c = c.lower()

        # Add it to the blank string
        s += c
    
    # If no special characaters are removed, return nothing
    if removed == 0:
        print('No special characters removed')
        return None

    # Split the string into a list of individual words - split on whitespace
    arr = s.split()
    
    # Put the word and the count into a dictionary
    d = {}

    # Iterate through the split words array, count the occurance of each word
    for word in arr:
        # If the word isn't in the dictionary, add it
        if word not in d:
            d[word] = 0
        
        # Increment the count
        d[word] += 1

    # Put the dictionary into a list to sort
    items = list(d.items())

    # Sort the dictionary, first by count and then by alphabet
    items.sort(key= lambda e: (-e[1], e[0]))

    ### Print the output in the desired way
    # Space between word and first hashtag needs to be two spaces longer than the longest word
    longest_word = max([len(x) for x in arr])
    width = longest_word + 2

    # For each tuple, print key and count in length hashtags
    for item in items:
        print(f"{item[0].ljust(width)}" + '#' * item[1])

# Histogram of robin.txt file
word_hist('robin.txt')
