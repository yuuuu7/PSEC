import json
import random

with open("wordlist.txt") as f:
       wordlist = json.loads(f.read())

      # Choose a random word from the wordlist
       selected_dictionary = random.choice(wordlist)

      # Extract the word and meaning from the dictionary
       word = selected_dictionary['word']
       meaning = selected_dictionary['meaning']

    # Set up the game
guesses = []
max_guesses = 6

    # Main game loop
while True:
        print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
        print(f'Guesses: {guesses}')

        # Get the player's next guess
        guess = input('Enter your guess: ')

        # Update the game state based on the guess
        if guess in word:
            guesses.append(guess)
        else:
            max_guesses -= 1

        # Check if the player has won or lost
        if all(c in guesses for c in word):
            print('You win!')
            break
        elif max_guesses == 0:
            print('You lose!')
            break


