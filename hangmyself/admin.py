import json
import hashlib
import os
import datetime

def admin_login():
 max_attempt = 3
 i = max_attempt
 while i <= max_attempt:

  # Get the inputted username and password
  adminUserinput = input("Username: ")
  adminPass = input("Password: ")

  password_bytes = adminPass.encode()
  hashed_password = hashlib.sha256(password_bytes).hexdigest()
  # Read the data from the file and store it in a dictionary
  with open('admin.txt') as f:
    data = json.loads(f.read())

  # Check if the inputted username and password match the ones in the dictionary
  if data['username'] == adminUserinput and data['password'] == hashed_password:
    return True
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    i -= 1
    print('\nIncorrect username or password!')
    print(f"You are left with {i}/", max_attempt,  'attempt(s)\n')
    if i == 0:
      print("Sorry you have used your max number of attempts at logging in")
      exit()

def print_word_list():
  # Open the file and read the contents
  with open('wordlist.txt') as f:
      contents = f.read()

  # Parse the contents of the file as a JSON object
  words = json.loads(contents)

  # Print the list of words
  for i, word in enumerate(words, start=1):
      print(f"{i}. {word['word']}")

def word_settings():
  def replace_word():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    found = False
    while not found:
      print_word_list()
    # Prompt the user for the word to replace
      userInput = input("\nEnter the word to be replaced (enter 'q' to exit): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

      # Flag to track whether the word was found

      # Iterate through the list of dictionaries and find the dictionary containing the word to replace
      for item in data:
        if userInput == item["word"]:
          found = True
          userInputreplace = input("Enter replacement: ")
          item["word"] = userInputreplace.strip()
          print(f"\nWord Changed Successfully! {userInput} --> {userInputreplace}")

      # If the word was not found, display an error message
      if not found:
        print(f"\nSorry, the word '{userInput}' does not exist, please enter an EXISTING word to be replaced.")
      

    # Convert the dictionary back into a JSON string
    json_data = json.dumps(data,indent=4)

    # Open the file in write mode
    with open("wordlist.txt", "w") as f:
      # Write the modified JSON string to the file
      f.write(json_data)

  def replace_meaning():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    found = False
    while not found:
      userInput = input("\nEnter whichever (Word)'s meaning you want to change(Press 'q' to exit): ")

      if userInput == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break


      # Iterate through the dictionary and replace the value for the specific word
      for item in data:
        if userInput == item['word']:
          found = True
          userInputreplace = input("Enter replacement meaning: ")
          item["meaning"] = userInputreplace
          print(f"\nMeaning Changed Successfully!")

      if not found:
          print(f"\nSorry, the word '{userInput}' does not exist, please enter an EXISTING word.")

    # Convert the dictionary back into a JSON string
    json_data = json.dumps(data,indent=4)

    # Open the file in write mode
    with open("wordlist.txt", "w") as f:
      # Write the modified JSON string to the file
      f.write(json_data)

  def add_new_word_meaning():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    # Get the new word and meaning from the user
    new_word = input("Enter a new word that you want to add: ").strip().lower()
    new_meaning = input("Enter it's Definition: ")

    # Create a new dictionary with the new word and meaning
    new_item = {"word": new_word, "meaning": new_meaning}

    # Add the new dictionary to the list of dictionaries
    data.append(new_item)


    # Convert the dictionary back into a JSON string
    json_data = json.dumps(data,indent=4)

    # Open the file in write mode
    with open("wordlist.txt", "w") as f:
      # Write the modified JSON string to the file
      f.write(json_data)

  def delete_word_meaning():
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    found = False
    while not found:
      print_word_list()

      userInput = input("\nEnter a word that you want to delete (Definition will be deleted as well): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break


      # Iterate through the list of dictionaries and find the dictionary containing the word to delete
      for item in data:
        if userInput == item['word']:
          found = True
          data.remove(item)

    # Convert the dictionary back into a JSON string
    json_data = json.dumps(data,indent=4)

    # Open the file in write mode
    with open("wordlist.txt", "w") as f:
      # Write the modified JSON string to the file
      f.write(json_data)


  while True:
    print("            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|" )
    userChoice2 = int(input("\n" + "\t" + "1. Replace word" + "\n" + "\t" + "2. Replace meaning" + "\n" + "\t" + "3. Add word and meaning"+ "\n" + "\t" + "4. Delete word and meaning"+ "\n" + "\t" + "5. Exit" + "\n" + "\n" + "  >>"))

    if userChoice2 == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      replace_word()
    elif userChoice2 == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      replace_meaning()
    elif userChoice2 == 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      add_new_word_meaning()
      print("\nNew Word and Meaning successfully updated!")
    elif userChoice2 == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      delete_word_meaning()
      print("\nWord and meaning successfully deleted!")
    elif userChoice2 == 5:
      return False

def change_settings():
  
    with open("game-settings.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    while True:
        print("            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|" )
        print("\nEnter the number of the game setting you want to change\n")
        choice = int(input("\t1. Number of attempts\n\t2. Number of words\n\t3. Number of top players\n\t4. Exit\n\n>> "))

        if choice == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            new_attempts = int(input("\nEnter the new number of attempts: "))
            data['number of attempts'] = new_attempts
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nChanges made successfully!")
        elif choice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            new_words = int(input("Enter the new number of words: "))
            data['number of words'] = new_words
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nChanges made successfully!")
        elif choice == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            new_players = int(input("Enter the new number of top players: "))
            data['number of top players'] = new_players
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nChanges made successfully!")
        elif choice == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("\nInvalid choice!")


    
        json_data = json.dumps(data,indent=4)

        # Open the file in write mode
        with open("game-settings.txt", "w") as f:
          # Write the modified JSON string to the file
          f.write(json_data)

def print_report():
  while True:
     # Read in the start and end dates from the user
     start_date_str = input("Enter the start date (DD-MM-YY): ")
     end_date_str = input("Enter the end date (DD-MM-YY): ")
     os.system('cls' if os.name == 'nt' else 'clear')

     # Convert the date strings to datetime objects
     start_date = datetime.datetime.strptime(start_date_str, "%d-%m-%y")
     end_date = datetime.datetime.strptime(end_date_str, "%d-%m-%y")

     # Open the file containing the game data
     with open("game_logs.txt") as f:
          # Read in the contents of the file and parse the JSON data
          games = json.loads(f.read())

     # Check if the start date is more recent than the end date
     if start_date > end_date:
          # Sort the games in reverse order if the start date is more recent
          games.sort(key=lambda x: x["date"], reverse=True)
     else:
          # Sort the games in ascending order if the start date is less recent
          games.sort(key=lambda x: x["date"])
    
     print(f"Start Date: {start_date_str}\nEnd Date: {end_date_str}")
     # Print the report header
     print("\nGame Report")
     print("------------")
     print("\nName\t\tPoints\t\tDate Joined")

     # Iterate over the games
     for game in games:
          # Convert the date string to a datetime object
          date = datetime.datetime.strptime(game["date"], "%d-%m-%y")

          print(f"{game['name']}\t\t{game['points']}\t\t{game['date']}")
        

     # Print the report footer
     print("\n------------")

     exit_input = input("\nEnter 'q' to quit: ").lower()
     if exit_input == 'q':
      break

if admin_login() is True:
  while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|" )
      userChoice = int(input("\n" + "\t" + "1. Change word settings" + "\n" + "\t" + "2. Change game settings" + "\n" + "\t" + "3. Print report" + "\n" + "\t" + "4. Exit" + "\n" + "\n" + "  >>"))
      if userChoice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        word_settings()
      if userChoice == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        change_settings()
      if userChoice == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_report()
      if userChoice == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        break


