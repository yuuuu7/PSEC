

import json
import random

# Open the wordlist file and parse the contents
with open("wordlist.txt") as f:
    wordlist = json.loads(f.read())

# Choose a random word from the wordlist
selected_dictionary = random.choice(wordlist)

# Extract the word and meaning from the dictionary
word = selected_dictionary['word']
meaning = selected_dictionary['meaning']

print("The word to guess was: " , word)