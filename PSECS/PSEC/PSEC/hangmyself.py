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

word_list = {
    "hefty": "Something that is of considerable weight or size" ,
    "lambent": "moving about as if touching lightly; flickering; glowing" ,
    "sugar": "an Ingredient or source of food that tastes sweet",
    "deer": "It has large ears, short tails, and long, slender legs",
    "zebra": "African equines with distinctive black-and-white striped coats",

    
}

print("H A N G M A N")
login = input("Please select wether you are a Player or Admin: " + "\n" + "1. Player" + "\n" + "2. Admin")

if login is 2:
  passwd = input("Please enter the admin password: ")
    