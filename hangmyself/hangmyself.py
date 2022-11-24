import random
HANGMAN_PICS = [
""" 
    _____ 
   |     |
   |
   |
   |
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

""" 
    _____ 
   |     |
   |     o
   |
   |
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

""" 
    _____ 
   |     |
   |     o
   |     |
   |
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

"""
    _____ 
   |     |
   |     o
   |    /|
   |
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

"""
    _____ 
   |     |
   |     o
   |    /|\\
   |
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

"""
    _____ 
   |     |
   |     o
   |    /|\\
   |    /
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

"""
    _____ 
   |     |
   |     o
   |    /|\\
   |    / \\
   |
  _|_
  | |_______
  |          |
  |___________| """ ,

]


userName=str(input("\n" + "Hi! Please enter your name:"))

print("\n" + "\t" + "H A N G M A N" + "\n" +"\n" + "  Welcome to The Hangman Game, " + userName + "!")

userChoice = int(input("\n" + "\t" + "1. Play Hangman" + "\n" + "\t" + "2. Print top 5 players" + "\n" + "\t" + "3. Quit" + "\n" + "\n" + "  >>"))

counter = 0
while counter == 0:
 if userChoice == 1:
    print("\n" + "HANGMAN" + "\n")
    print("Player: ", userName)
    print(HANGMAN_PICS[0])



 elif userChoice == 2:
  print("\n" + "HANGMAN" + "\n")
  print("Work in Progress.")


 elif userChoice == 3:
  print("\n" + "Thank you for playing!")
  break