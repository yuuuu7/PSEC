import random
import json
import datetime


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

def print_meaning_word(selected_word):

# Open the wordlist file and parse the contents
 with open("wordlist.txt") as f:
    wordlist = json.loads(f.read())

# Find the dictionary with the selected word
 selected_dictionary = None
 for dictionary in wordlist:
    if dictionary['word'] == selected_word:
        selected_dictionary = dictionary
        break

# If a dictionary was found, print the word and meaning
 if selected_dictionary:
    word = selected_dictionary['word']
    meaning = selected_dictionary['meaning']
    print(f"{word}: {meaning}")
 else:
    print("Word not found.")

def update_gamelogs():
  with open('game_logs.txt', 'a') as f:
    info = "{}\t{}\t{}\n".format(userName, points, date_now)
    f.write(info)

with open("game-settings.txt") as f:
    settings = json.load(f)

# Get the game settings
max_incorrect_guesses = settings["number of attempts"]
total_number_of_words = settings['number of words']
number_of_top_players = settings['number of top players']

date_now = datetime.date.today()

session = 0
while (session < 3):
 print("\n" + "\t" + "H A N G M A N" + "\n" +"\n" + "  Welcome to The Hangman Game !")
 userChoice = int(input("\n" + "\t" + "1. Play Hangman" + "\n" + "\t" + "2. Display the top 5 players" + "\n" + "\t" + "3. Quit" + "\n" + "\n" + "  >>"))

 if userChoice == 1:
      session += 1
      userName = input("\n" + "Please enter your name:")

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
      while True:

         print("\n" + "HANGMAN" + "\n")
         print("Player: ", userName)
         print(session, 'of 3\n\n\n')
         
         if i == 0:
          print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}')
         else:
          print(f'Word: {" ".join([c if c in guesses else "_" for c in word])}\n')
          print(f'Incorrect letters: {wrong_guesses}', '(', i, ')\n')
          print("You have used", i,"/", max_incorrect_guesses, "of max number of guesses\n")

         userGuess = input("Guess a letter: ")
        

         if userGuess in word:
          guesses.append(userGuess)
  
         elif userGuess not in word:
            i+=1
            wrong_guesses.append(userGuess)

            if i == max_incorrect_guesses:
              print("You have used all of your attempts, Sorry!")
              update_gamelogs()
              break

         elif all([c in guesses for c in word]):
            print("Congratulations! You won the game!")
            print(f"The word was: {word}. It means {meaning}\n")
            points += 100
            print(f"You have earned: {points} points!")
            update_gamelogs()
            break

      print(f"Thanks for playing! You have earned this many points: {points} \n")
      exit_input = int(input("Press '0' to exit: "))
      if exit_input == 0:
        session = session


 
 elif userChoice == 2:
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