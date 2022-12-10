import random
import json

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
      break
    elif(userName is int):
      # The input is not a non-empty string, so it is invalid
      print("You cannot have Empty Spaces and Only-Numbers for your Username!")

    '''points = 1000

    with open('userinfo.txt', 'w') as f:
     info = "{} {}".format(userName, points)
     f.write(info) '''


 
 elif userChoice == 2:
   print("\n" + "\t" + "HANGMAN" + "\n")
   print("============== Top 5 Players ==============")
   user_stats('userinfo.txt')
   exit_input = int(input("Press '0' to exit: "))
   if (exit_input == 0):
     session = 2


 elif userChoice == 3:
  print("\n" + "Thank you for playing!")
  break


    