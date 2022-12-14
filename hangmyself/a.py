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

with open("game_settings.txt") as f:
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
    if type(userName) == str and len(userName) > 0:
     # The input is a non-empty string, so it is valid
      print("\n" + "HANGMAN" + "\n")
      print("Player: ", userName)
      print(session, 'of 3')
      exit_input = int(input("Press '0' to exit: "))
      if exit_input == 0:
        session = session
    elif(userName is int):
      # The input is not a non-empty string, so it is invalid
      print("You cannot have Empty Spaces and Only-Numbers for your Username!")

    points = 1000
    date = '29/10/2022'
    with open('game_logs.txt', 'a') as f:
     info = "{}\t{}\t{}\n".format(userName, points, date_now)
     f.write(info)


 
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