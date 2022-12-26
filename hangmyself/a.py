import random
import json
import datetime
import ast
import re

def is_valid_username(input_str, authorized_chars):
  with open("game_logs.txt") as f:
    data = json.loads(f.read())

  for c in input_str:
    # Check if the character is present in the authorized_chars list
    if c not in authorized_chars:
        # The character is not authorized
        print("Invalid username. Only upper and lowercase letters, '-', and '/' are allowed.")
        return False
        
  # Iterate over the list of dictionaries
  for player in data:
      # Check if the username is present in the data
      if input_str == player['name']:
        print("Sorry this username already exists, try a different username.")
        # The username is present in the data
        return False

  # If we reach this point, the username is not present in the data
  return True


def create_default_gs_file(file_name):
  # Handle the FileNotFoundError exception
  try:
    # Open the file in read mode
    file = open(file_name, 'r')
    # Read the contents of the file
    contents = file.read()
  except FileNotFoundError:
    # If the file does not exist, create a new file and write the game settings to it
    file = open(file_name, 'w')
    file.write('{\n  "number of attempts": 6,\n  "number of words": 3,\n  "number of top players": 0\n}')
  finally:
    # Close the file
    file.close()

def create_default_wordlist_file(filename):
    # JSON data to be written to the file
    data = [
        {
            "word": "abed",
            "meaning": "in bed"
        },
        {
            "word": "bell",
            "meaning": "a device that makes a ringing sound when struck or when electrical circuit is completed"
        },
        {
            "word": "bump",
            "meaning": "a collision in which two or more objects strike together"
        },
        {
            "word": "care",
            "meaning": "the provision of what is necessary for the health, welfare, maintenance, and protection of someone or something"
        },
        {
            "word": "card",
            "meaning": "a flat, thin piece of stiff paper, cardboard, or plastic, especially one used for writing or printing on"
        },
        {
            "word": "door",
            "meaning": "a hinged, sliding, or revolving barrier at the entrance to a building, room, or vehicle, or in the framework of a cupboard"
        },
        {
            "word": "fist",
            "meaning": "a hand with the fingers clenched in the palm (as for hitting)"
        },
        {
            "word": "grin",
            "meaning": "to smile broadly, often with the corners of the mouth turned up and the teeth exposed"
        },
        {
            "word": "haze",
            "meaning": "a state of mental confusion or unawareness"
        },
        {
            "word": "hope",
            "meaning": "a feeling of expectation and desire for a certain thing to happen"
        },
        {
            "word": "joke",
            "meaning": "something said or done to evoke laughter"
        },
        {
            "word": "jolt",
            "meaning": "a sudden shake or jar"
        },
        {
            "word": "leap",
            "meaning": "to spring with a sudden movement, especially to jump from one place to another"
        },
        {
            "word": "leek",
            "meaning": "a vegetable with a long, thin green stalk and white flesh, related to the onion and garlic, and used in cooking"
        },
        {
            "word": "leer",
            "meaning": "a sly or lecherous look"
        },
        {
            "word": "menu",
            "meaning": "a list of the dishes available in a restaurant"
        },
        {
            "word": "mine",
            "meaning": "a place where coal, oil, or other minerals are extracted from the earth"
        },
        {
            "word": "mint",
            "meaning": "a place where money is coined by authority of the government"
        },
        {
            "word": "mock",
            "meaning": "to treat with contempt or ridicule"
        },
        {
            "word": "note",
            "meaning": "a written or printed communication, usually on paper, consisting of a few lines of words or numbers"
        }
    ]

    try:
        # Open the file in write mode
        with open(filename, "w") as f:
            # Write the JSON data to the file
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        # Create a new file in write mode
        with open(filename, "w") as f:
            # Write the JSON data to the file
            json.dump(data, f, indent=4)


def update_gamelogs():
  with open('game_logs.txt') as f:
    data = json.loads(f.read())
    
  new_player= {"name": userName, "points": points, "date": date_now}

  data.append(new_player)

  json_data = json.dumps(data,indent=4)

  # Open the file in write mode
  with open("game_logs.txt", "w") as f:
    # Write the modified JSON string to the file
    f.write(json_data)

def print_hangman_art():
  with open('hangman_art.txt') as f:
   hangman_art = ast.literal_eval(f.read())


   print(hangman_art[stage])

def print_top_players():
  with open("game_logs.txt") as file:
    contents = file.read()

  # Parse the contents of the file and store the result in a variable
  data = json.loads(contents)

  # Sort the data by points in descending order
  sorted_list = sorted(data, key=lambda x: x['points'], reverse=True)

  # Print the top 5 players in the desired format
  for player in sorted_list[:5]:
      name = player['name']
      points = player['points']
      date = player['date']
      print(f"{name}\t{points}\t{date}\n")

create_default_gs_file('game-settings.txt')
with open("game-settings.txt") as f:
  settings = json.load(f)


# Get the game settings
max_incorrect_guesses = settings["number of attempts"]
total_number_of_words = settings['number of words']
number_of_top_players = settings['number of top players']


date_today = datetime.date.today()
date_now = date_today.strftime("%d-%m-%y")

# Define a list of allowed characters
allowed_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '/']


session = 0
counter = 0
data = {}
stage=6
userChoice = 0
while True and userChoice == 0:

  print(" _    _              _   _    _____   __  __              _   _ \n| |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |\n| |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |\n|  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |\n| |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |\n|_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|")
  print_hangman_art()
  userChoice = int(input("\n" + "\t" + "1. Play Hangman" + "\n" + "\t" + "2. Display the top 5 players" + "\n" + "\t" + "3. Quit" + "\n" + "\n" + "  >>"))

  if userChoice == 1:
      session += 1
      data = {}
      counter = 0
      while counter == 0:
        userName = input("\n" + "Please enter your name:")
        if is_valid_username(userName, allowed_characters):
          break
        else:
          counter = 0


      create_default_wordlist_file('wordlist.txt')

     
      points = 0

      while session <= 3:
        i = 0
        max_points = 30
        guesses = []
        wrong_guesses = []
        stage = 0
        counter = 0
        counter2 = 0
        points2 = 0
        counter3 = 0

        with open("wordlist.txt") as f:
          wordlist = json.loads(f.read())

          # Choose a random word from the wordlist
          selected_dictionary = random.choice(wordlist)

          # Extract the word and meaning from the dictionary
          word = selected_dictionary['word']
          meaning = selected_dictionary['meaning']

        while i < max_incorrect_guesses:
          print("\n" + "HANGMAN" + "\n")
          print("Player: ", userName)
          print(session, 'of 3\n')

          if counter2 == 0:
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
            print(f'\nIncorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")
          elif counter3 > 0:
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
            print(f'\nIncorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")
            print("You have already guessed this letter! Try a different letter!\n")
          else:
            stage += 1
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}\n')
            print(f'Incorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")

          userGuess = input("Guess a letter: ").lower().strip()

          if userGuess in word and userGuess not in guesses:
            counter2 = 0
            guesses.append(userGuess)
            if points <= max_points:
              points2 += 2
              points += 2
          elif userGuess in word and userGuess in guesses:
            counter3 += 1
          elif userGuess not in word and userGuess in wrong_guesses:
            counter3 += 1
          elif userGuess not in word:
            i += 1
            counter += 1
            counter2 += 1
            wrong_guesses.append(userGuess)

          if all([c in guesses for c in word]):
            print("\nCongratulations! You got the word right!\n")
            print(f"The word was: {word}. It means {meaning}\n")
            break

        if i == max_incorrect_guesses:
          stage = 6
          print_hangman_art()
          print("\nYou have used all of your", i, '/', max_incorrect_guesses, "incorrect attempts!\n")

        print(f"\nThanks for playing! You have earned {points2} points from this session!\n")
        play_again = input("Do you want to play again? [Y/N]: ").lower()
        if play_again.lower() == "y":
          session += 1
        elif play_again.lower() == "n":
          userChoice = 0
          update_gamelogs()
          print("\nThank you for playing!")
          if points < 15:
            print("\nSorry, you lost!")
          else:
            print("\nYou won!")
          break
        elif session == 3:
          userChoice = 0
          update_gamelogs()
          print("Sorry you have reached the max number of sessions!")
          if points < 15:
            print("\nSorry, you lost!")
          else:
            print("\nYou won!")
          break
        else:
          print("Please enter a valid input.")

  
  if userChoice == 2:
    print("\n" + "\t" + "HANGMAN" + "\n")
    print("============== Top 5 Players ==============")
    print("Name\tPoints\tDate")
    print_top_players()
    exit_input = int(input("Press '0' to exit: "))
    if (exit_input == 0):
      userChoice = 0

  elif userChoice == 3:
    print("\n" + "Thank you for playing!")
    break