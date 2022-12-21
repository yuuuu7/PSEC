import random
import json
import datetime
import ast

def update_userinfo(file_name):
  with open(file_name, 'a') as f:
    info = "{}\t{}\t{}\n".format(userName, points, date_now)
    f.write(info)

def read_file(file_name):
  # Open the file in read-only mode
  with open(file_name, "r") as file:
    # Read the contents of the file and return them
    data = json.loads(file.read())
    formatted_json = json.dumps(data, indent=4)
    return formatted_json

def user_stats(file_name):
  with open(file_name, 'r') as file:
   for line in file:
    print(line)

def update_gamelogs():
  with open('game_logs.txt', 'a') as f:
    info = "{}\t{}\t{}\n".format(userName, points, date_now)
    f.write(info)

def print_hangman_art():
  with open('hangman_art.txt') as f:
   hangman_art = ast.literal_eval(f.read())


   print(hangman_art[stage])

with open("game-settings.txt") as f:
  settings = json.load(f)

# Get the game settings
max_incorrect_guesses = settings["number of attempts"]
total_number_of_words = settings['number of words']
number_of_top_players = settings['number of top players']

date_now = datetime.date.today()

session = 0
counter = 0
data = {}
while True:

  print("\n" + "\t" + "H A N G M A N" + "\n" +"\n" + "  Welcome to The Hangman Game !")
  userChoice = int(input("\n" + "\t" + "1. Play Hangman" + "\n" + "\t" + "2. Display the top 5 players" + "\n" + "\t" + "3. Quit" + "\n" + "\n" + "  >>"))

  if userChoice == 1:
    while userChoice ==1:
      session += 1
      data = {}
      counter = 0
      while counter == 0:
        userName = input("\n" + "Please enter your name:")
        # Create an empty dictionary to store the data
        with open('game_logs.txt', 'r') as f:
          # Read the file line by line
          for line in f:
            # Split the line into fields
            fields = line.split(' ')
            # Add the data to the dictionary, using the username as the key
            data[fields[0]] = fields[1:]

        # Check if the username we are looking for exists in the dictionary
        if userName in data:
          # If it does, the username already exists
          print('Username already exists, please try another Username instead!')
          counter = 0
        else:
          break


      
      with open("wordlist.txt") as f:
        wordlist = json.loads(f.read())

        # Choose a random word from the wordlist
        selected_dictionary = random.choice(wordlist)

        # Extract the word and meaning from the dictionary
        word = selected_dictionary['word']
        meaning = selected_dictionary['meaning']

        i=0
        points = 0
        guesses = []
        wrong_guesses = []
        stage = 0
        counter = 0
        counter2 = 0
        while(session <= 3):

          print("\n" + "HANGMAN" + "\n")
          print("Player: ", userName)
          print(session, 'of 3\n')

          if counter2 == 0:
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
            print(f'\nIncorrect letters: {wrong_guesses}', '(', counter, ')\n')
          else:
            stage += 1
            print_hangman_art()
            print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}\n')
            print(f'Incorrect letters: {wrong_guesses}', '(', counter, ')\n')
            print("You have used", i,"/", max_incorrect_guesses, "of max number of incorrect guesses\n")

          userGuess = input("Guess a letter: ")
                        

          if userGuess in word:
            counter2 = 0
            guesses.append(userGuess)
          elif userGuess not in word:
            i+=1
            counter += 1
            counter2 += 1
            wrong_guesses.append(userGuess)

          if i == max_incorrect_guesses:
            print("\nYou have used all of your", i, '/', max_incorrect_guesses, "incorrect attempts!\n")
            update_gamelogs()
            break

          if all([c in guesses for c in word]):
            print("\nCongratulations! You got the word right!\n")
            print(f"The word was: {word}. It means {meaning}\n")
            points += 100 #testing points system only
            update_gamelogs()
            break

        print(f"Thanks for playing! You have earned {points} points from this session! \n")

        exit_input = input("Do you want to play again? [Y/N]: ")

        if exit_input.lower() == 'y' and session < 3:
          userChoice = 1
          counter = 0
        else:
          break

  
  if userChoice == 2:
    print("\n" + "\t" + "HANGMAN" + "\n")
    print("============== Top 5 Players ==============")
    print("Name\tPoints\tDate")
    user_stats('game_logs.txt')
    exit_input = int(input("Press '0' to exit: "))
    if (exit_input == 0):
      session = session


  elif userChoice == 3:
    print("\n" + "Thank you for playing!")
    break