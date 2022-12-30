import json
import hashlib
import os
import datetime
from colorama import Fore, Back, Style

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
    print(Fore.RED + '\nIncorrect username or password!' + Style.RESET_ALL)
    print(f"You are left with {i}/", max_attempt,  'attempt(s)\n')
    if i == 0:
      print(Fore.Red + "Sorry you have used your max number of attempts at logging in" + Style.RESET_ALL)
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

def print_word_list_and_meaning():
  # Open the file and read the contents
  with open('wordlist.txt') as f:
      contents = f.read()

  # Parse the contents of the file as a JSON object
  words = json.loads(contents)

  # Print the list of words
  for i, word in enumerate(words, start=1):
      print(f"{i}. {word['word']} - {word['meaning']}\n")

def word_settings():
  def replace_word():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    
    while True:
      counter = 1
      print("============ WORDLIST ============\n")
      print_word_list()
    # Prompt the user for the word to replace
      userInput = input("\nEnter the" + Fore.RED + " WORD " + Style.RESET_ALL + "to be replaced (enter 'q' to exit): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

      # Flag to track whether the word was found

      # Iterate through the list of dictionaries and find the dictionary containing the word to replace
      for item in data:
        if userInput == item["word"]:
          counter = 0
          userInputreplace = input("Enter replacement: ")
          item["word"] = userInputreplace.strip()
          os.system('cls' if os.name == 'nt' else 'clear')

          # Convert the dictionary back into a JSON string
          json_data = json.dumps(data,indent=4)

          # Open the file in write mode
          with open("wordlist.txt", "w") as f:
            # Write the modified JSON string to the file
            f.write(json_data)

          print(Fore.GREEN + f"\nWord Changed Successfully!"  + Style.RESET_ALL , f"{userInput} --> {userInputreplace}\n")

      # If the word was not found, display an error message
      if counter > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nSorry, the word '{userInput}' does not exist, please enter an" + Fore.RED + " EXISTING "  + Style.RESET_ALL +  "word to be replaced.")
      

  def replace_meaning():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    
    while True:
      counter = 1
      print("================= WORDLIST =================\n")
      print_word_list_and_meaning()
      userInput = input("\nEnter whichever" + Fore.RED + " WORD" + Style.RESET_ALL + "'s meaning you want to" + Fore.GREEN + " CHANGE " + Style.RESET_ALL + "(Press 'q' to exit): ")

      if userInput == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break


      # Iterate through the dictionary and replace the value for the specific word
      for item in data:
        if userInput == item['word']:
          counter = 0
          userInputreplace = input("Enter replacement meaning: ")
          item["meaning"] = userInputreplace
          os.system('cls' if os.name == 'nt' else 'clear')

          # Convert the dictionary back into a JSON string
          json_data = json.dumps(data,indent=4)

          # Open the file in write mode
          with open("wordlist.txt", "w") as f:
            # Write the modified JSON string to the file
            f.write(json_data)

          print(Fore.GREEN + f"\nMeaning Changed Successfully!\n" + Style.RESET_ALL)

      if counter > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nSorry, the word '{userInput}' does not exist, please enter an" + Fore.RED + " EXISTING " + Style.RESET_ALL + "word.")


  def add_new_word_meaning():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    while True:
      print("============ WORDLIST ============\n")
      print_word_list()
      # Get the new word and meaning from the user
      new_word = input("\nEnter a new word that you want to" + Fore.GREEN + " ADD " + Style.RESET_ALL + "(Press 'q' to quit): ").strip().lower()
      if new_word == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      new_meaning = input("Enter it's Definition (Press 'q' to quit): ")
      if new_meaning == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

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

      print(Fore.GREEN + "\nNew Word and Meaning successfully added!" + Style.RESET_ALL)

  def delete_word_meaning():
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    while True:
      print("============ WORDLIST ============\n")
      print_word_list()
      userInput = input("\nEnter a word that you want to" + Fore.RED + " DELETE " + Style.RESET_ALL + "Definition will be deleted as well (press 'q' to quit): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break


      # Iterate through the list of dictionaries and find the dictionary containing the word to delete
      for item in data:
        if userInput == item['word']:
          while True: 
            are_u_sure = input(f"Are you sure you want to" + Fore.RED + " DELETE " + Style.RESET_ALL + f"{userInput}? [Y/N]: ")
            if are_u_sure.lower() == 'y':

              data.remove(item)
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)
              
              print(Fore.GREEN + "\nWord and meaning successfully deleted!" + Style.RESET_ALL)
              
              break

            elif are_u_sure.lower() == 'n':
              os.system('cls' if os.name == 'nt' else 'clear')
              break

            else:
              print(Fore.RED + "Invalid Input, please enter 'y' or 'n'" + Style.RESET_ALL)



  while True:
    print(Fore.GREEN + "            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|"  + Style.RESET_ALL )
    userChoice2 = int(input("\n" + "\t" + "1. Replace word" + "\n" + "\t" + "2. Replace meaning" + "\n" + "\t" + "3. Add word and meaning"+ "\n" + "\t" + "4. Delete word and meaning"+ "\n" + "\t" + Fore.RED + "5. Exit" + Style.RESET_ALL + "\n" + "\n" + "  >>"))

    if userChoice2 == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      replace_word()
    elif userChoice2 == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      replace_meaning()
    elif userChoice2 == 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      add_new_word_meaning()
    elif userChoice2 == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      delete_word_meaning()
    elif userChoice2 == 5:
      return False

def change_settings():
  
    with open("game-settings.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    while True:
        print(Fore.GREEN + "            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|"  + Style.RESET_ALL )
        print("\nEnter the number of the game setting you want to change\n")
        choice = int(input("\t1. Number of attempts\n\t2. Number of words\n\t3. Number of top players\n\t" + Fore.RED + "4. Exit\n\n" + Style.RESET_ALL + ">> "))

        if choice == 1:

            os.system('cls' if os.name == 'nt' else 'clear')

            while True:
              print(f"Current Max Number of Wrong Attempts: {data['number of attempts']}\n")
              try:
                new_attempts = int(input("\nEnter the new number of attempts (Enter '0' to quit): "))

                if new_attempts == 0:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  break

                data['number of attempts'] = new_attempts
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Changes made successfully!\n" + Style.RESET_ALL)

              except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                # Input is not a valid integer
                print("Please enter only" + Fore.RED + " Integer " + Style.RESET_ALL + "values.\n")

        elif choice == 2:

            os.system('cls' if os.name == 'nt' else 'clear')

            while True:
              print(f"Current Total Number of Words: {data['number of words']}\n")
              try:
                new_words = int(input("Enter the new number of words (Enter '0' to quit): "))

                if new_words == 0:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  break

                data['number of words'] = new_words
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Changes made successfully!\n" + Style.RESET_ALL)

              except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                # Input is not a valid integer
                print("Please enter only" + Fore.RED + " Integer " + Style.RESET_ALL + "values.\n")

        elif choice == 3:

            os.system('cls' if os.name == 'nt' else 'clear')

            while True:
              print(f"Current Total Number of Top Players: {data['number of top players']}\n")
              try:
                new_players = int(input("Enter the new number of top players (Enter '0' to quit): "))

                if new_players == 0:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  break

                data['number of top players'] = new_players
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Changes made successfully!\n" + Style.RESET_ALL)

              except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                # Input is not a valid integer
                print("Please enter only" + Fore.RED + " Integer " + Style.RESET_ALL + "values.\n")

        elif choice == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print(Fore.RED + "\nInvalid choice!" + Style.RESET_ALL)


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
     print(Fore.YELLOW + "\nName\t\tPoints\t\tDate Joined" + Style.RESET_ALL)

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
      print(Fore.GREEN + "            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|" + Style.RESET_ALL )
      userChoice = int(input("\n" + "\t" + "1. Change word settings" + "\n" + "\t" + "2. Change game settings" + "\n" + "\t" + "3. Print report" + "\n" + "\t" + Fore.RED + "4. Exit" + Style.RESET_ALL + "\n" + "\n" + "  >>"))
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


