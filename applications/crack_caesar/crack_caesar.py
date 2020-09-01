# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

'''
Read in the text
Count the freq of each non-punc character
Use the frequency count from our text to map to the letters that we know 
are the most - least freq in the english language
    - Creates a decoding table

After we have a decoding table we can decode each character in the text, ignoring punct.
'''

def freq_count(text):
    import string

    # Read in the text of the input file name
    with open(text) as file:
        text = file.read()

    # Freq count of each letter ignoring spaces and punct
    # Dictionary to count freq
    d = {}

    for c in text:
        # Ignore spaces
        if c.isspace():
            continue

        # Ignore punct.
        if c in string.punctuation:
            continue

        # If the letter is not in the dictionary, add it
        if c not in d:
            d[c] = 0
        
        # Increment count
        d[c] += 1
    
    # Now we have a frequency count
    # Pull out the letters sorted by freq

    # Put the dictionary into a list to sort
    items = list(d.items())

    # Sort the dictionary by freq
    items.sort(key= lambda e: (e[1]), reverse=True)

    # Store an array with the keys (letters sorted in most freq order)
    our_freq = [item[0] for item in items]
        
    # Map our count to the known freq of characters in the english language
    known_freq = [
        'E',
        'T',
        'A',
        'O',
        'H',
        'N',
        'R',
        'I',
        'S',
        'D',
        'L',
        'W',
        'U',
        'G',
        'F',
        'B',
        'M',
        'Y',
        'C',
        'P',
        'K',
        'V',
        'Q',
        'J',
        'X',
        'Z'
        ]

    # Create the decode table, the key should be our known character
        # The value is the correct character
    
    decode_table = {}

    # There are 28 items in our_freq but only 26 in the english alphabet
        # - don't map the last two (-, 1)
    for i in range(26):
        decode_table[our_freq[i]] = known_freq[i] 

    # Now we have a decode table to decode the input text

    # Empty string to pass in decoded characters
    message = ""

    # Go through each character
    for c in text:
        # If c is a key in our decode table, swap it with the value
        if c in decode_table.keys():
            message += decode_table[c]
        # Otherwise, just add it without decoding (should be only punct and spaces)
        else:
            message += c

    # Return decoded message
    return message

# Run the example
print(freq_count('ciphertext.txt'))
