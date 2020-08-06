'''
Plan:
    Dictionary:
        Split the text into separate words, keep capitals and punct.
        Add each unique word as a key with an empty list as a value
            For each word, add the next word to the value array for that key
    Pick words:
        When putting the words into the dictionary populate start and stop word lists
            If the first character of the word is a Capital add to start words
            If the first character is a " and then a Capital, 
                (so second character is a capital) ass to start words
            If the word ends with a .?! or second to last is .?!, add to stop words

        Start with blank string
        1. Start with a random word from the Start words list
        2. Randomly choose a word from the list that can follow that first word
        3. Continue choosing a random word from the next list as long as it does not belong to the stop list

        Use recursive function to build the sentence, passing on the next word to the next call

    Print the built message using 
        for word in message_list:
            print(word, end=" ")
'''

import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# Split the words
word_list = words.split()

# Create the dictionary and lists
d = {}
start_words = []
stop_words = []

# Go through each item in word_list
for i in range(len(word_list) -1):
    word = word_list[i]
    next_word = word_list[i + 1]

    # Add it to the dictionary with a value of an empty list if its new
    if word not in d:
        d[word] = []

    # Add the following word to the key's value list
    d[word].append(next_word)

    # Add it to start list if appropriate
        # If first letter is a Capital (for 1 letter words like I, A ...)
    if word[0].isupper():
        start_words.append(word)
    
    # If the word is more than 1 letter long and the first character is a "
    # and the second character is Capital
    if len(word) > 1:
        if word[0] == '"' and word[1].isupper():
            start_words.append(word)

    # If word contains . ! or ? add to stop list
    if '.' in word or '!' in word or '?' in word:
        stop_words.append(word)

'We have build word dictionary and start and stop lists'

# Build a sentence
# Recursive function
# Takes in a word and the built sentence so far, 
    # Adds the word to the sentence
    # chooses the next word and passes that and the new sentence into the next call
# If the word is in the stop list, add the word and then end the cycle
    # Return the sentence

def build_sentence(word, sentence):

    sentence = sentence

    # Put the word in the sentence list
    sentence.append(word)

    # Break the cycle if the word is in the stop list
    if word in stop_words:
        return sentence

    # Pick the next word - from the list stored by the word key
    random_next_word = random.choice(d[word])

    return build_sentence(random_next_word, sentence)

# Function for printing generated sentences
def print_sentences(num_sentences):
    for i in range(num_sentences):
        # Start with random word
        rand_start = random.choice(start_words)

        # Build a list of words for new sentence
        new_sentence = build_sentence(rand_start, [])

        # Print as a sentence
        print(f'Sentence {i+1}: \n')
        for rand_word in new_sentence:
            print(rand_word, end=" ")
        print('\n')


# Print 5 random sentences
print_sentences(5)

