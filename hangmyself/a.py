import random
import json
import datetime
import ast
import os
from colorama import Fore, Back, Style
import time

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
    file.write('{\n  "number of attempts": 6,\n  "number of words": 20,\n  "number of top players": 5\n}')
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
 try:
  with open('hangman_art.txt') as f:
   hangman_art = ast.literal_eval(f.read())


   print(hangman_art[stage])
 except ValueError:
  print("The file 'hangman_art.txt' is empty, please contact an Administrator to solve this issue.")

def print_top_players():
  with open("game_logs.txt") as file:
    contents = file.read()

  # Parse the contents of the file and store the result in a variable
  data = json.loads(contents)

  # Sort the data by points in descending order
  sorted_list = sorted(data, key=lambda x: x['points'], reverse=True)
  i = 1
  # Print the top 5 players in the desired format
  for player in sorted_list[:no_of_top_players]:
      name = player['name']
      points = player['points']
      date = player['date']
      print(f"    {i}. {name} - > {points} points\n")
      time.sleep(0.04)
      i += 1


try:
  with open("game-settings.txt") as f:
    settings = json.load(f)
except ValueError:
  print("Sorry but the Game Settings file is empty, please contact an Administrator to fix this issue.")
  exit()
except FileNotFoundError:
  create_default_gs_file('game-settings.txt')
  


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
  os.system('cls' if os.name == 'nt' else 'clear')
  print(Fore.BLUE + """ 
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  """ + Style.RESET_ALL)
  print('''
      \t   ____
      \t  |    |
      \t  |    O
      \t  |   /|\\
      \t  |   / \\
      \t  |
        __|__
    ''')
  time.sleep(0.04)
  print("\n" + "\t" + "1. Play Hangman")
  time.sleep(0.04)
  print("\n" + "\t" + "2. Display the top 5 players")
  time.sleep(0.04)
  print("\n" + "\t" + Fore.RED + "3. Quit" + Style.RESET_ALL + "\n" + "\n")
  time.sleep(0.04)
  userChoice = int(input("  >>"))

  if userChoice == 1:
      # Clear the terminal screen
      os.system('cls' if os.name == 'nt' else 'clear')
      session += 1
      data = {}
      counter = 0
      while counter == 0:
        userName = input("\n" + "Please enter your name:")
        if is_valid_username(userName, allowed_characters):
          # Clear the terminal screen
          os.system('cls' if os.name == 'nt' else 'clear')
          break
        else:
          counter = 0

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
        correct_guess_counter = 0
        wrong_guess_counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
          with open("wordlist.txt") as f:
            wordlist = json.loads(f.read())

            # Choose a random word from the wordlist
            selected_dictionary = random.choice(wordlist)

            # Extract the word and meaning from the dictionary
            word = selected_dictionary['word']
            meaning = selected_dictionary['meaning']
        except FileNotFoundError:
          create_default_wordlist_file('wordlist.txt')
        except ValueError:
          print("Sorry, the file 'wordlist.txt' is empty, please contact an Administrator to fix this issue.")

        while i < max_incorrect_guesses:
          os.system('cls' if os.name == 'nt' else 'clear')
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
            correct_guess_counter += 1
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
            wrong_guess_counter += 1
            wrong_guesses.append(userGuess)

          if all([c in guesses for c in word]):
            print(f"\nCongratulations! After {correct_guess_counter} Correct Guesses and {wrong_guess_counter} Wrong Guesses, you got the word right!")
            print(f"The word was: {word}.")
            print(f"It means {meaning}.")
            break

        if i == max_incorrect_guesses:
          os.system('cls' if os.name == 'nt' else 'clear')
          stage = 6
          print_hangman_art()
          print("\nYou have used all of your", i, '/', max_incorrect_guesses, "incorrect attempts!\n")

        print(f"\nThanks for playing! You have earned {points2} points from this session!\n")
        while True:
          play_again = input("Do you want to play again? [Y/N]: ").lower()
          if play_again.lower() == "y":
            session += 1
          elif play_again.lower() == "n":
            userChoice = 0
            update_gamelogs()
            if points < 15:
              print(Fore.RED + "\nSorry, you lost!" + Style.RESET_ALL)
            else:
              print("\nYou won the game!")
            break
          elif session == 3:
            userChoice = 0
            update_gamelogs()
            print(Fore.RED + "Sorry you have reached the max number of sessions!")
            if points < 15:
              print(Fore.RED + "\nSorry, you lost!" + Style.RESET_ALL )
            else:
              print(Fore.GREEN + "\nYou won!" + Style.RESET_ALL)
            break
          else:
            print(Fore.RED + "Please enter a valid input." + Style.RESET_ALL)

        break

  
  if userChoice == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('game-settings.txt') as f:
      data = json.loads(f.read())

    no_of_top_players = data['number of top players']
     
    print("\n" + Fore.YELLOW + """ 
    ██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
    ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
    ██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║
    ██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
    ███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
    ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝""" + Style.RESET_ALL + "\n")
    print(f"    ============== Top {no_of_top_players} Players ==============\n")
    print_top_players()
    print("    ==========================================\n")
    exit_input = int(input("    Enter '0' to exit: "))
    if (exit_input == 0):
      os.system('cls' if os.name == 'nt' else 'clear')
      userChoice = 0

  elif userChoice == 3:
    print("\n" + "Thank you for playing!")
    break