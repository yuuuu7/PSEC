# Open the "dictionary.txt" file and read the words into a dictionary
# The file should have the format "word:definition" for each line
with open("wordlist.txt") as file:
    words = {}
    for line in file:
        word = line

# Use the random.choice() function to select a random word
import random
word = random.choice(list(words))

# Use the selected word in your program
print("The random word is:", word)


