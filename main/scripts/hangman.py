"""
Main Program

StudentID:      p2227452
Name:           Lim Yu Liang
Class:          DISM/FT/1B/02
Assessment:     CA1-1

Script name:
    admin.py

Purpose:
    This script is the admin panel for the hangman game.

Usage syntax:
    python hangman.py

Input file:
    ./scripts/admin.py
    ./scripts/hangman.py


Output file:
    ./text_files/game_logs.txt
    ./text_files/game_settings.txt
    ./text_files/word_list.txt

Python Version:
    Python 3.10.9

Reference:
https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python
https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

Library/Module:
- these modules are installed by default in Python 3.11
    - hashlib
    - random
    - json
    - os
    - time
    - datetime


Known Issues:
    - Different counters are each used for different Error Message Displays for most of the code
     - I understand that this is not good practice as it might the code very messy and a global variable reference may cause an Error
     - I did it because the Graphical Interface the user will be experiencing will be a lot more clearer and easy to read and use
     - I will take note of it in the future as it is not the best practice and try other methods to fix it
"""
import random
import json
import datetime
import ast
import os
from colorama import Fore, Back, Style
import time

def is_valid_username(input_str, authorized_chars) -> bool:
  """
        Checks whether userinput for username is valid

        Args:
            input_str: Input name of player
            authorized_chars: allowed characters for use
        """
  with open("../text_files/game_logs.txt") as f:
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
      if input_str == player['name'].lower():
        print("Sorry this username already exists, try a different username.")
        # The username is present in the data
        return False

  # If we reach this point, the username is not present in the data
  return True


def create_default_gs_file(file_name) -> None:
  """
        Creates a default game settings file

        Args:
            file_name: file's name
        """

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

def create_default_wordlist_file(filename) -> None:
    """
        Creates a default wordlist file

        Args:
           filename: file's name
        """

    # JSON data to be written to the file
    data = [
    {
        "word": "abed",
        "meaning": "in bed",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "bell",
        "meaning": "a device that makes a ringing sound when struck or when electrical circuit is completed",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "bump",
        "meaning": "a collision in which two or more objects strike together",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "care",
        "meaning": "the provision of what is necessary for the health, welfare, maintenance, and protection of someone or something",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "card",
        "meaning": "a flat, thin piece of stiff paper, cardboard, or plastic, especially one used for writing or printing on",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "abstemious",
        "meaning": "abstaining from or moderation in the consumption of food and drink",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "insouciance",
        "meaning": "a lack of concern or care; nonchalance",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "fastidious",
        "meaning": "paying great attention to detail; meticulous",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "extemporize",
        "meaning": "speak, perform, or produce (something) with little or no preparation",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "magnanimous",
        "meaning": "unselfishly generous",
        "type": "Word",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "once in a blue moon",
        "meaning": "rarely",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "curiosity killed the cat",
        "meaning": "being too curious can lead to trouble",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "beating around the bush",
        "meaning": "not speaking directly about a topic",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "beating a dead horse",
        "meaning": "to continue discussing or trying to do something that has already been unsuccessful",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "time heals all wounds",
        "meaning": "eventually everything will be okay",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Simple"
    },
    {
        "word": "you cant make an omelette without breaking a few eggs",
        "meaning": "in order to achieve something, it is necessary to accept that there may be negative consequences or sacrifices",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "the pen is mightier than the sword",
        "meaning": "the power of words and communication is greater than physical force or violence",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "a bird in the hand is worth two in the bush",
        "meaning": "something you have is worth more than something you may have in the future",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "where there is smoke there is fire",
        "meaning": "there is likely to be a problem or situation if there are signs or indications of it",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Complex"
    },
    {
        "word": "the best things in life are free",
        "meaning": "the most valuable or enjoyable things in life do not have a financial cost",
        "type": "Idioms-Proverbs",
        "enabled": "on",
        "difficulty": "Complex"
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


def update_gamelogs() -> None:
  """
        updates player's name,points and date joined into game_logs.txt

        """
  with open('../text_files/game_logs.txt') as f:
    data = json.loads(f.read())
    
  new_player= {"name": userName, "points": points, "date": date_now}

  data.append(new_player)

  json_data = json.dumps(data,indent=4)

  # Open the file in write mode
  with open("../text_files/game_logs.txt", "w") as f:
    # Write the modified JSON string to the file
    f.write(json_data)

def print_hangman_art() -> None:
 """
        prints hangman art based on stage

        Args:
        """
 try:
  with open('../text_files/hangman_art.txt') as f:
   hangman_art = ast.literal_eval(f.read())


  print(hangman_art[stage])
 except ValueError:
  print("The file 'hangman_art.txt' is empty, please contact an Administrator to solve this issue.")

def print_top_players() -> None:

  """
        Prints top X players

        Args:
            player (str): Input name of player
        """
  def print_leaderboard():
    with open("../text_files/game_logs.txt") as file:
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
  
  os.system('cls' if os.name == 'nt' else 'clear')
  with open('../text_files/game-settings.txt') as f:
    data = json.loads(f.read())

  no_of_top_players = data['number of top players']
    
  while True:
    print("\n" + Fore.YELLOW + """ 
    ██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
    ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
    ██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║
    ██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
    ███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
    ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝""" + Style.RESET_ALL + "\n")
    print(f"    ============== Top {no_of_top_players} Players ==============\n")
    print_leaderboard()
    print("    ==========================================\n")
    exit_input = int(input("    Enter '0' to exit: "))
    if (exit_input == 0):
      os.system('cls' if os.name == 'nt' else 'clear')
      break



#Checks to see if game-settings.txt is empty or does not exist
#If it doesnt exist, a default game-settings file will be created
#If the game-settings is empty, the code will exit automatically as the game cannot run without game-settings
try:
  with open("../text_files/game-settings.txt") as f:
    settings = json.load(f)
except ValueError:
  print("Sorry but the Game Settings file is empty, please contact an Administrator to fix this issue.")
  exit()
except FileNotFoundError:
  create_default_gs_file('../text_files/game-settings.txt')

#Checks to see if wordlist.txt is empty or does not exist
#If it doesnt exist, a default wordlist file will be created
#If the game-settings is empty, the code will exit automatically as the game cannot run without a wordlist
try:
  with open("../text_files/wordlist.txt") as f:
    wordlist = json.loads(f.read())
    
except FileNotFoundError:

  create_default_wordlist_file('../text_files/wordlist.txt')

except ValueError:

  print("Sorry, the file 'wordlist.txt' is empty, please contact an Administrator to fix this issue.")
  exit()
  


# Get the game settings
max_incorrect_guesses = settings["number of attempts"]
total_number_of_words = settings['number of words']
number_of_top_players = settings['number of top players']

#Getting the date today formatting it in DD-MM-YY
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
      session = 0
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

      #points are outside of the loop as we do not want to reset the player's points 
      points = 0
      while session <= 3:
        #Initializing variables so that the game can run smoothly
        i = 0

        guesses = [' ',]
        wrong_guesses = []
        vowels = ['a','e','i','o','u']

        stage = 0

        #points2 is to calculate how much points they have earned EACH session
        points2 = 0
        
        #Each counter returns to different If statements for different Error Messages 
        counter = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0

        correct_guess_counter = 0
        wrong_guess_counter = 0

        lifeline_used = False
        lifeline_used_2 = False

        os.system('cls' if os.name == 'nt' else 'clear')

        with open("../text_files/wordlist.txt") as f:
          wordlist = json.loads(f.read())
          
          #Only enabled words are allowed to be picked
          enabled_words = [word for word in wordlist if word['enabled'] == 'on']

          # Choose a random word from the list of enabled words
          selected_dictionary = random.choice(enabled_words)

          # Extract the word and meaning from the dictionary
          word = selected_dictionary['word']
          meaning = selected_dictionary['meaning']

        while i < max_incorrect_guesses:
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\n" + "HANGMAN" + "\n")
          print("Player: ", userName)
          print(session, 'of 3\n')

          if counter2 == 0:
            #If nothing goes wrong and user's guess is correct
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
            print(f'\nIncorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")
          elif counter3 > 0:
            #If user is trying to guess a letter that they have previously guessed or gotten from Lifeline
            counter3 = 0
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
            print(f'\nIncorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")
            print("You have already guessed this letter! Try a different letter!\n")
          elif counter4 == 1:
            #If user is trying to enter multiple characters or non-alphabets
            counter4 = 0
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
            print(f'\nIncorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")
            print("Please guess only" + Fore.YELLOW + " ONE " + Style.RESET_ALL + "letter!\n")
          else:
            #If nothing goes wrong and user guess is incorrect, hangman art will change and so will the other trackers
            stage += 1
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}\n')
            print(f'Incorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")

          userGuess = input("Guess a letter (Enter '0' to use Lifeline): ").lower().strip()
                
          if len(userGuess) != 1 or userGuess == ' ':
            #Checks if user guess is having more than or less than 1 character, and if it is an empty space
            counter4 = 1
            counter2 = 1
            #returns to counter4 == 1 error statement

          elif userGuess == '0':
            #Jumps to the Lifeline Menu
            os.system('cls' if os.name == 'nt' else 'clear')

            while True:


                  if lifeline_used == False and lifeline_used_2 == False and points >= 4:
                    #If both lifelines are unused
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======= Lifeline =======\n")
                    print("1. Show all Vowels\n2. Show Definition\n3. Exit\n")
                    lifeline_choice = input(">>")

                  elif lifeline_used == True and lifeline_used_2 == False and points >= 4:
                    #If Show Vowels is used, the color will turn from white to red as to indicate inusability since lifelines can be only used once
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======= Lifeline =======\n")
                    print("1. " + Fore.RED + "Show all Vowels" + Style.RESET_ALL + "\n2. Show Definition\n3. Exit\n")
                    lifeline_choice = input(">>")

                  elif lifeline_used == False and lifeline_used_2 == True and points >= 4:
                    #If Show Definition is used, the color will turn from white to red as to indicate inusability since lifelines can be only used once
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======= Lifeline =======\n")
                    print("1. Show all Vowels" + "\n2. " + Fore.RED + "Show Definition" + Style.RESET_ALL + "\n3. Exit\n")
                    print(Fore.YELLOW + "Meaning: " + Style.RESET_ALL + f"{meaning}")
                    lifeline_choice = input("\n>>")

                  elif lifeline_used == True and lifeline_used_2 == True:
                    #If Both Lifelines is used, the color will turn from white to red as to indicate inusability since lifelines can be only used once
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======= Lifeline =======\n")
                    print("1. " + Fore.RED + "Show all Vowels" + Style.RESET_ALL + "\n2. " + Fore.RED + "Show Definition" + Style.RESET_ALL + "\n3. Exit\n")
                    print(Fore.YELLOW + "Meaning: " + Style.RESET_ALL + f"{meaning}")
                    print(Fore.RED + "\nAll lifelines have been used. You cannot use any more lifelines." + Style.RESET_ALL)
                    lifeline_choice = input("\n>>")
                  
                  else:
                    #If user does not have enough points to be using a Lifeline
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======= Lifeline =======\n")
                    print("1. " + Fore.BLACK + "Show all Vowels" + Style.RESET_ALL + "\n2. " + Fore.BLACK + "Show Definition" + Style.RESET_ALL + "\n3. Exit\n")
                    print("You have" + Fore.RED + " INSUFFICIENT " + Style.RESET_ALL + "points to use" + Fore.GREEN + " Lifelines" + Style.RESET_ALL)
                    lifeline_choice = input("\n>>")

                  if lifeline_choice == '1':
                    if not lifeline_used and points >= 4:
                      points -= 4
                      points2 -= 4
                      os.system('cls' if os.name == 'nt' else 'clear')
                      vowels_in_word = []

                      for c in word:
                          if c in vowels:
                              vowels_in_word.append(c)
                              #Appends to guesses so if user guesses vowels again an error message will throw
                              guesses.append(c)
                      # show all vowels in the word
                      vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

                      for c in word:
                          if c in vowel_count:
                            #If the vowel appears more than 1 time in the word, the number will increase, showing the total number of vowels that are present in the word for the user
                            vowel_count[c] += 1
                      print(Fore.GREEN + "\nVowels Present:\n\n" + Style.RESET_ALL + "==============")

                      for vowel, count in vowel_count.items():
                        print(f"{vowel} - {count}")
                      #Prints all the vowels with their corresponding number count for the user to see
                      #counter variable 'i' is assigned the index of the current character 'c' in the word string.

                      for c in word:
                        if c in vowels_in_word and c not in guesses:
                          #If there are vowels that the user has yet to guess that was appended in vowels_in_word, it will append to guesses to prevent a re-guess
                          guesses.append(c)
                      print("\n==============\n")
                      continue_input = input("Press enter to continue")
                      lifeline_used = True



                  elif lifeline_choice == '2':
                    if not lifeline_used_2 and points >= 4:
                      points -= 4
                      points2 -= 4
                      os.system('cls' if os.name == 'nt' else 'clear')
                      # show the definition of the word
                      print(f"Definition: {meaning}")
                      continue_input = input("\nPress enter to continue")
                      lifeline_used_2 = True
 

                  else:
                    break

          elif not userGuess.isalpha():
            #Checks if userguess is an alphabet or not
            counter4 = 1
            counter2 = 1
            #returns to counter4 == 1 error statement

          elif userGuess in word and userGuess not in guesses:
            #If what the user is guessing has not already been guesses before, the new guess will append to its respective correct/wrong guesses lists
            counter2 = 0
            correct_guess_counter += 1
            guesses.append(userGuess)
            points2 += 2
            points += 2

          elif userGuess in word and userGuess in guesses:
            #Checks if userguess has already been guessed and returns to an Error message throwing if-condition
            counter2 = 1
            counter3 += 1

          elif userGuess not in word and userGuess in wrong_guesses:
            #Checks if userguess has already been guessed and returns to an Error message Throwing if-condition
            counter2 = 1
            counter3 += 1
            
          elif userGuess not in word and userGuess not in wrong_guesses:
            #If what the user is guessing has not already been guesses before, the new guess will append to its respective correct/wrong guesses lists
            i += 1
            counter += 1
            counter2 += 1
            wrong_guess_counter += 1
            wrong_guesses.append(userGuess)

          if i == max_incorrect_guesses:
            #If the user has used up all of their incorect attempts, they are no longer allowed to continue playing, and breaks out of the while loop
            os.system('cls' if os.name == 'nt' else 'clear')
            stage = 6
            print_hangman_art()
            print("\nYou have used all of your", i, '/', max_incorrect_guesses, "incorrect attempts!\n")
          
          if all([c in guesses for c in word]):
            #If the user manages to guess all the letters inside the chosen word, the code breaks out
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nCongratulations! After {correct_guess_counter} Correct Guesses and {wrong_guess_counter} Wrong Guesses, you got the word right!\n")
            print(f"The word was: {word}.")
            print(f"It means: {meaning}.")
            break
        
        #Either the user has used up all of their incorrect attempts or they have managed to guessed all the letters correctly
        print(f"\nThanks for playing! You have earned {points2} points from this session!\n")
        play_again_bool = False
        while True:
          #Prompting the user whether they want to play the game again 
          play_again = input("\nDo you want to play again? [Y/N]: ").lower()
          if play_again.lower() == "y":
            #If the user chooses to play again, a new session is started and their Name,Points and Date Joined are not updated until they either choose NOT to play again or sessions have hit the limit (3)
            session += 1
            play_again_bool = True
            break
          elif play_again.lower() == "n":
            #If the user chooses not to play again, the code breaks out into the main menu and updates their Name,Points and Date Joined into game_logs.txt
            play_again_bool = False
            #Userchoice = 0 so they are brought back to the main menu
            userChoice = 0
            #updates user's information
            update_gamelogs()
            if points2 < 15:
              #If points earned that session is less than 15 they lose
              print(Fore.RED + "\nSorry, you lost!\n" + Style.RESET_ALL)
            else:
              #If its more than 15, they win the game.
              print(Fore.GREEN + "\nYou won the game!\n" + Style.RESET_ALL)
            break
          elif session == 3:
            #If the # of sessions has hit 3, the code breaks out into the main menu and updates their Name,Points and Date Joined into game_logs.txt
            play_again_bool = False
            #Userchoice = 0 so they are brought back to the main menu
            userChoice = 0
            #updates user's information
            update_gamelogs()
            print(Fore.RED + "Sorry you have reached the max number of sessions!" + Style.RESET_ALL + f" You have earned a total of {points} from all 3 Sessions")
            if points2 < 15:
              #If points earned that session is less than 15 they lose
              print(Fore.RED + "\nSorry, you lost!\n" + Style.RESET_ALL )
            else:
              #If its more than 15, they win the game.
              print(Fore.GREEN + "\nYou won the game!\n" + Style.RESET_ALL)
            break
          else:
            #Validation of user input
            print(Fore.RED + "Please enter a valid input." + Style.RESET_ALL)
        
        if play_again_bool == False:
          #If user decides not to play again, pressing enter or any key brings them out back into the main menu
          continue_input = input("Press Enter to continue")
          break


          

  
  if userChoice == 2:
    #Prints the leaderboard
    print_top_players()
    #When exiting, user is brought back to the main menu
    userChoice = 0

  elif userChoice == 3:
    #Exits the code
    print("\n" + "Thank you for playing!")
    break