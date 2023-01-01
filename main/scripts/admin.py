import json
import hashlib
import os
import datetime
from colorama import Fore, Back, Style
import time

def admin_settings():

  def create_new_admin():


    # Read the data from the file and store it in a dictionary
    with open('../text_files/admin_cred.txt') as f:
      data = json.loads(f.read())

    counter = 0
    counter2 = 0
    while True:
      found = False
      if counter == 1:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Sorry this Username already exists, please try another username.\n")

      if counter2 == 1:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + "Admin Successfully created!\n" + Style.RESET_ALL)

      if counter == 0:
        NewadminUserinput = input("Set a Username (Enter 'q' to quit): ")

      if NewadminUserinput.lower() == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

      for admin in data:
        if NewadminUserinput == admin['username']:
          found = True
          counter = 1

      if found == False and counter == 0:
        while True:
          os.system('cls' if os.name == 'nt' else 'clear')
          print(Fore.RED + "*** VERY IMPORTANT ***\n" + Style.RESET_ALL)
          print(""" Password must comply with the following:\n\n• Should have at LEAST one number.\n• Should have at LEAST one uppercase and one lowercase character.\n• Should have at LEAST one of these special symbols (!@#$%).\n• Should be between 4 to 20 characters long.\n""")
          
          if counter == 2:
            print("\nPassword does not meet the requirement. Please try another password.\n")

          NewadminPass = input("\nSet a Password (Enter 'q' to quit): ")

          if NewadminPass.lower() == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
          if any(char.isdigit() for char in NewadminPass) and any(char.isupper() for char in NewadminPass) and any(char.islower() for char in NewadminPass) and any(char in "!@#$%" for char in NewadminPass) and 4 <= len(NewadminPass) <= 20:
            os.system('cls' if os.name == 'nt' else 'clear')
            counter = 0
            counter2 = 1
            password_bytes = NewadminPass.encode()
            hashed_password = hashlib.sha256(password_bytes).hexdigest()

            # Create a new dictionary with the new word and meaning
            new_item = {"username": NewadminUserinput , "password": hashed_password}

            # Add the new dictionary to the list of dictionaries
            data.append(new_item)

            # Convert the dictionary back into a JSON string
            json_data = json.dumps(data,indent=4)

            # Open the file in write mode
            with open("../text_files/admin_cred.txt", "w") as f:
              # Write the modified JSON string to the file
              f.write(json_data)

            break
          else:
            os.system('cls' if os.name == 'nt' else 'clear')
            counter = 2


  def delete_admin():
    # Read the data from the file and store it in a dictionary
    with open('../text_files/admin_cred.txt') as f:
      data = json.loads(f.read())

    counter = 0
    while True:  
      found = False
      if counter == 1:
        counter = 0
        print(Fore.GREEN + "Admin Successfully" + Fore.RED + " DELETED" + Style.RESET_ALL + "!\n")

      adminUsernameInput = input("Please enter the" + Fore.YELLOW + " Username " + Style.RESET_ALL + "of the Admin that you want to" + Fore.RED + " DELETE " + Style.RESET_ALL + "(Enter 'q' to exit): ").strip()
      if adminUsernameInput.lower() == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      adminPassInput = input(f"Please enter Admin {adminUsernameInput}'s password (Enter 'q' to quit): ")
      if adminPassInput.lower() == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break


      password_bytes = adminPassInput.encode()
      hashed_password = hashlib.sha256(password_bytes).hexdigest()
    
      for admin in data:
        if adminUsernameInput == admin['username'] and hashed_password == admin['password']:
          found = True
      
      if found == True:
        while True:
          confirmation_input = input("\nAre you sure you want to" + Fore.RED + " DELETE " + Style.RESET_ALL + "this Admin? [Y/N]: ")
          if confirmation_input.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            counter = 1
            data.remove(admin)
            # Convert the dictionary back into a JSON string
            json_data = json.dumps(data,indent=4)

            # Open the file in write mode
            with open("../text_files/admin_cred.txt", "w") as f:
              # Write the modified JSON string to the file
              f.write(json_data)
            
            break

          elif confirmation_input.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Cancelled\n" + Style.RESET_ALL)
            break
          else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input, please select only 'y' or 'n'.\n")



      if found == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Sorry" + Fore.RED + " INCORRECT " + Style.RESET_ALL + "Password or Username.\n")

  def change_admin_pass():
    # Read the data from the file and store it in a dictionary
    with open('../text_files/admin_cred.txt') as f:
      data = json.loads(f.read())

    found = False
    counter = 0
    while True:

      if counter == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + "Password changed successfully!\n" + Style.RESET_ALL)

      adminUsername = input("Enter your Username (Enter 'q' to quit): ")
      if adminUsername.lower() == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      adminPassword = input("Enter your password (Enter 'q' to quit): ")
      if adminPassword.lower() == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

      password_bytes = adminPassword.encode()
      hashed_password = hashlib.sha256(password_bytes).hexdigest()

      for admin in data:
        if adminUsername == admin['username'] and hashed_password == admin['password']:
          found = True
      
      if found == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "*** VERY IMPORTANT ***\n" + Style.RESET_ALL)
        print(""" Password must comply with the following:\n\n• Should have at LEAST one number.\n• Should have at LEAST one uppercase and one lowercase character.\n• Should have at LEAST one of these special symbols (!@#$%).\n• Should be between 4 to 20 characters long.\n""")
        print(Fore.GREEN + "Admin Found!" + Style.RESET_ALL)
        while True:
          new_pass = input("\nEnter a new password that you want to set (Enter 'q' to quit): ")

          if new_pass.lower() == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
          if any(char.isdigit() for char in new_pass) and any(char.isupper() for char in new_pass) and any(char.islower() for char in new_pass) and any(char in "!@#$%" for char in new_pass) and 4 <= len(new_pass) <= 20:
            counter = 1

            password_bytes = new_pass.encode()
            hashed_password = hashlib.sha256(password_bytes).hexdigest()

            admin['password'] = hashed_password
            os.system('cls' if os.name == 'nt' else 'clear')

            # Convert the dictionary back into a JSON string
            json_data = json.dumps(data,indent=4)

            # Open the file in write mode
            with open("../text_files/admin_cred.txt", "w") as f:
              # Write the modified JSON string to the file
              f.write(json_data)

            break
          else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "*** VERY IMPORTANT ***\n" + Style.RESET_ALL)
            print(""" Password must comply with the following:\n\n• Should have at LEAST one number.\n• Should have at LEAST one uppercase and one lowercase character.\n• Should have at LEAST one of these special symbols (!@#$%).\n• Should be between 4 to 20 characters long.\n""")
            print("Password" + Fore.RED + " DOES NOT " + Style.RESET_ALL + "meet the requirement. Please try another password.")
      
      if found == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Incorrect Username or Password.\n")



  counter = 0
  while True:

    os.system('cls' if os.name == 'nt' else 'clear')
    try:
      print(Fore.GREEN +  '''
       █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
      ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
      ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
      ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
      ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
      ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ''' + Style.RESET_ALL )
      time.sleep(0.04)
      print("\n" + "\t" + "1. Add Admin")
      time.sleep(0.04)
      print("\n" + "\t" + "2. Delete Admin")
      time.sleep(0.04)
      print("\n" + "\t" + "3. Change Admin Password")
      time.sleep(0.04)
      print("\n" + "\t" + Fore.RED + "4. Exit" + Style.RESET_ALL + "\n")

      if counter == 1:
        time.sleep(0.04)
        print("   Please choose from options" + Fore.GREEN + " 1 - 3 " + Style.RESET_ALL + "only.\n")

      userChoice = int(input("  >>"))
      if userChoice == 1:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        create_new_admin()
      elif userChoice == 2:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        delete_admin()
      elif userChoice == 3:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        change_admin_pass()
      elif userChoice == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      else:
        counter = 1

    except ValueError:
      counter = 1



def admin_login():
  max_attempt = 3
  i = max_attempt
  counter = 0
  while i <= max_attempt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTMAGENTA_EX + '''
    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║\n''' + Style.RESET_ALL)

    if counter == 1:
      print(Fore.RED + 'Incorrect username or password!' + Style.RESET_ALL)
      print(f"You are left with {i}/", max_attempt,  'attempt(s)\n')

    # Get the inputted username and password
    adminUserinput = input("Username: ")
    adminPass = input("Password: ")

    password_bytes = adminPass.encode()
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    # Read the data from the file and store it in a dictionary
    with open('../text_files/admin_cred.txt') as f:
      data = json.loads(f.read())

    # Check if the inputted username and password match the ones in the dictionary
    for admin in data:
      if admin['username'] == adminUserinput and admin['password'] == hashed_password:
        return True
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        i -= 1
        counter = 1
        if i == 0:
          print(Fore.RED + "Sorry you have used your max number of attempts at logging in" + Style.RESET_ALL)
          exit()

def print_word_list():
  # Open the file and read the contents
  with open('../text_files/wordlist.txt') as f:
      contents = f.read()

  # Parse the contents of the file as a JSON object
  words = json.loads(contents)

  # Print the list of words
  for i, word in enumerate(words, start=1):
      print(f"{i}. {word['word']}")


def print_word_list_and_meaning():
  # Open the file and read the contents
  with open('../text_files/wordlist.txt') as f:
      contents = f.read()

  # Parse the contents of the file as a JSON object
  words = json.loads(contents)

  # Print the list of words
  for i, word in enumerate(words, start=1):
      print(f"{i}. {word['word']} - {word['meaning']}\n")

def word_settings():

  def replace_word():
    # Open the file in read mode
    with open("../text_files/wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    counter = 0
    while True:
      found = False
      print("============ WORDLIST ============\n")
      print_word_list()

      if counter == 1:
        counter = 0
        print(f"\nSorry, the word '{userInput}' does not exist, please enter an" + Fore.RED + " EXISTING " + Style.RESET_ALL + "word.")

      if counter == 2:
        counter = 0
        print(Fore.GREEN + f"\nWord Changed Successfully!"  + Style.RESET_ALL , f"{userInput} --> {userInputreplace}\n")

      userInput = input("\nEnter the" + Fore.RED + " WORD " + Style.RESET_ALL + "to be replaced (enter 'q' to exit): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

      # Flag to track whether the word was found

      # Iterate through the list of dictionaries and find the dictionary containing the word to replace
      for item in data:
        if userInput == item["word"]:
          found = True
          counter = 2
          userInputreplace = input("\nEnter replacement: ")
          item["word"] = userInputreplace.strip()
          os.system('cls' if os.name == 'nt' else 'clear')

          # Convert the dictionary back into a JSON string
          json_data = json.dumps(data,indent=4)

          # Open the file in write mode
          with open("../text_files/wordlist.txt", "w") as f:
            # Write the modified JSON string to the file
            f.write(json_data)


      # If the word was not found, display an error message
      if found == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 1
      

  def replace_meaning():
    # Open the file in read mode
    with open("../text_files/wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    counter = 0
    while True:
      found = False
      print("================= WORDLIST =================\n")
      print_word_list_and_meaning()

      if counter == 1:
        counter = 0
        print(f"\nSorry, the word '{userInput}' does not exist, please enter an" + Fore.RED + " EXISTING " + Style.RESET_ALL + "word.")

      if counter == 2:
        counter = 0
        print(Fore.GREEN + f"\nMeaning Changed Successfully!\n" + Style.RESET_ALL)

      userInput = input("\nEnter whichever" + Fore.RED + " WORD" + Style.RESET_ALL + "'s meaning you want to" + Fore.GREEN + " CHANGE " + Style.RESET_ALL + "(Press 'q' to exit): ")

      if userInput == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break


      # Iterate through the dictionary and replace the value for the specific word
      for item in data:
        if userInput == item['word']:
          found = True
          counter = 2
          userInputreplace = input("\nEnter replacement meaning: ")
          item["meaning"] = userInputreplace
          os.system('cls' if os.name == 'nt' else 'clear')

          # Convert the dictionary back into a JSON string
          json_data = json.dumps(data,indent=4)

          # Open the file in write mode
          with open("../text_files/wordlist.txt", "w") as f:
            # Write the modified JSON string to the file
            f.write(json_data)

      if found == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 1


  def add_new_word_meaning():
    # Open the file in read mode
    with open("../text_files/wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    counter = 0
    while True:
      found = False
      print("============ WORDLIST ============\n")
      print_word_list()

      if counter == 1:
        counter = 0
        print(Fore.GREEN + "\nSuccessfully added!" + Style.RESET_ALL)
      if counter == 2:
        counter = 0
        print("\nPlease enter" + Fore.RED + " Non-Integer " + Style.RESET_ALL + "Values only.")
      if counter == 3:
        counter = 0
        print(f"\nSorry but the word '{new_word}' already " + Fore.RED + "EXISTS" + Style.RESET_ALL + ".")

      new_word = input("\nEnter a new word that you want to" + Fore.GREEN + " ADD " + Style.RESET_ALL + "(Press 'q' to quit): ").lower()

      # Iterate through the dictionary and replace the value for the specific word
      for item in data:
        if new_word == item['word']:
          found = True
          counter = 3
          os.system('cls' if os.name == 'nt' else 'clear')

      if " " in new_word:

        word_type = "Idioms-Proverbs"

        if len(new_word.split()) > 8:
          new_diff = "Complex"
        else:
          new_diff = "Simple"

      else:
        word_type = "Word"

        if len(new_word) > 10:
          new_diff = "Complex"
        else:
          new_diff = "Simple"

      if new_word.strip() == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      elif new_word.isnumeric():
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 2

      if found == False and counter == 0:

        new_meaning = input("\nEnter it's Definition (Press 'q' to quit): ")
        counter = 1

        if new_meaning.lower() == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break

        os.system('cls' if os.name == 'nt' else 'clear')

        new_item = {
            "word": new_word,
            "meaning": new_meaning,
            "difficulty": new_diff,
            "type": word_type,
            "enabled": "on",
        }

        # Add the new dictionary to the list of dictionaries
        data.append(new_item)


        # Convert the dictionary back into a JSON string
        json_data = json.dumps(data,indent=4)

        # Open the file in write mode
        with open("../text_files/wordlist.txt", "w") as f:
          # Write the modified JSON string to the file
          f.write(json_data)

        print("The Difficulty and Word-Type spcifics have been automatically updated.")
        print("(Words/Idioms/Proverbs are enabled by default)\n")
        print("===========================\n")
        print(f"Difficulty: {new_diff}\nWord Type: {word_type}\n")
        print("===========================\n")
        input("Press Enter to continue")

  def delete_word_meaning():
    with open("../text_files/wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    counter = 0
    while True:
      found = False
      print("============ WORDLIST ============\n")
      print_word_list()

      if counter == 1:
        counter = 0
        print(f"\nSorry, the word '{userInput}' does not exist, please enter an" + Fore.RED + " EXISTING " + Style.RESET_ALL + "word.")

      if counter == 2:
        counter = 0
        print(Fore.GREEN + "\nSuccessfully deleted!" + Style.RESET_ALL)
      
      if counter == 3:
        counter = 0
        print(Fore.RED + "\nCancelled" + Style.RESET_ALL)

      userInput = input("\nEnter a word that you want to" + Fore.RED + " DELETE " + Style.RESET_ALL + "Definition will be deleted as well (press 'q' to quit): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break


      # Iterate through the list of dictionaries and find the dictionary containing the word to delete
      for item in data:
        if userInput == item['word']:
          found = True
          counter = 2
          while True: 
            are_u_sure = input(f"\nAre you sure you want to" + Fore.RED + " DELETE " + Style.RESET_ALL + f"'{userInput}'? [Y/N]: ")
            if are_u_sure.lower() == 'y':
              os.system('cls' if os.name == 'nt' else 'clear')
              data.remove(item)
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)
              
              break

            elif are_u_sure.lower() == 'n':
              counter = 3
              os.system('cls' if os.name == 'nt' else 'clear')
              break

            else:
              print(Fore.RED + "Invalid Input, please enter 'y' or 'n'" + Style.RESET_ALL)


      if found == False:
          os.system('cls' if os.name == 'nt' else 'clear')
          counter = 1

  def toggle_items():
    
    # Open the file in read mode
    with open("../text_files/wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    def print_word_list_simple():
      # Open the file and read the contents
      with open('../text_files/wordlist.txt') as f:
        contents = f.read()

      # Parse the contents of the file as a JSON object
      words = json.loads(contents)

      print("==== Simple Wordlist ====\n")

      # Print the list of words
      for i, word in enumerate(words, start=1):
        if word['type'] == 'Word' and word['difficulty'] == 'Simple':
          if word['enabled'] == 'on':
            print(f"{i}. {word['word']} - " + Fore.GREEN + "enabled" + Style.RESET_ALL)
          else:
            print(f"{i}. {word['word']} - " + Fore.RED+ "disabled" + Style.RESET_ALL)
      
      print("\n=========================\n")

    def print_word_list_complex():
      # Open the file and read the contents
      with open('../text_files/wordlist.txt') as f:
        contents = f.read()

      # Parse the contents of the file as a JSON object
      words = json.loads(contents)

      print("==== Complex Wordlist ====\n")

      # Print the list of words
      for i, word in enumerate(words, start=1):
        if word['type'] == 'Word' and word['difficulty'] == 'Complex':
          if word['enabled'] == 'on':
            print(f"{i}. {word['word']} - " + Fore.GREEN + "enabled" + Style.RESET_ALL)
          else:
            print(f"{i}. {word['word']} - " + Fore.RED + "disabled" + Style.RESET_ALL)

      print("\n==========================\n")

    def print_idiom_proverbs_list_simple():
      # Open the file and read the contents
      with open('../text_files/wordlist.txt') as f:
        contents = f.read()

      # Parse the contents of the file as a JSON object
      words = json.loads(contents)

      print("==== Simple Idioms-Proverbs list ====\n")

      # Print the list of words
      for i, word in enumerate(words, start=1):
        if word['type'] == 'Idioms-Proverbs' and word['difficulty'] == 'Simple':
          if word['enabled'] == 'on':
            print(f"{i}. {word['word']} - " + Fore.GREEN + "enabled" + Style.RESET_ALL)
          else:
            print(f"{i}. {word['word']} - " + Fore.RED+ "disabled" + Style.RESET_ALL)
      
      print("\n==============================\n")

    def print_idiom_proverbs_list_complex():
        #Open the file and read the contents
        with open('../text_files/wordlist.txt') as f:
          contents = f.read()

        # Parse the contents of the file as a JSON object
        words = json.loads(contents)

        print("==== Complex Idioms-Proverbs list ====\n")

        # Print the list of words
        for i, word in enumerate(words, start=1):
          if word['type'] == 'Idioms-Proverbs' and word['difficulty'] == 'Complex':
            if word['enabled'] == 'on':
              print(f"{i}. {word['word']} - " + Fore.GREEN + "enabled" + Style.RESET_ALL)
            else:
              print(f"{i}. {word['word']} - " + Fore.RED + "disabled" + Style.RESET_ALL)

        print("\n====================================\n")

    def toggle_words():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_word_list_simple()
        print_word_list_complex()
        user_toggle_input = input("\nDo you want to toggle" + Fore.RED + " ALL " + Style.RESET_ALL + "words" + Fore.RED + " OFF " + Style.RESET_ALL + "or" + Fore.GREEN + " ON" + Style.RESET_ALL + "? [OFF/ON] (Press 'q' to quit): ")
        
        if user_toggle_input.lower().strip() == 'off':
          for word in data:
            if word['type'] == 'Word' and word['enabled'] == 'on':
              word['enabled'] = 'off'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'on':
          for word in data:
            if word['type'] == 'Word' and word['enabled'] == 'off':
              word['enabled'] = 'on'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'q':
          break
        else:
          print("Please enter a valid input.")
    
    def toggle_words_simple():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_word_list_simple()
        user_toggle_input = input("\nDo you want to toggle" + Fore.RED + " ALL " + Style.RESET_ALL + "SIMPLE words" + Fore.RED + " OFF " + Style.RESET_ALL + "or" + Fore.GREEN + " ON" + Style.RESET_ALL + "? [OFF/ON] (Press 'q' to quit): ")
        
        if user_toggle_input.lower().strip() == 'off':
          for word in data:
            if word['type'] == 'Word' and word['difficulty'] == 'Simple' and word['enabled'] == 'on':
              word['enabled'] = 'off'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'on':
          for word in data:
            if word['type'] == 'Word' and word['difficulty'] == 'Simple' and word['enabled'] == 'off':
              word['enabled'] = 'on'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break
        else:
          print("Please enter a valid input.")
    
    def toggle_words_complex():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_word_list_complex()
        user_toggle_input = input("\nDo you want to toggle" + Fore.RED + " ALL " + Style.RESET_ALL + "COMPLEX words" + Fore.RED + " OFF " + Style.RESET_ALL + "or" + Fore.GREEN + " ON" + Style.RESET_ALL + "? [OFF/ON] (Press 'q' to quit): ")
        
        if user_toggle_input.lower().strip() == 'off':
          for word in data:
            if word['type'] == 'Word' and word['difficulty'] == 'Complex' and word['enabled'] == 'on':
              word['enabled'] = 'off'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'on':
          for word in data:
            if word['type'] == 'Word' and word['difficulty'] == 'Complex' and word['enabled'] == 'off':
              word['enabled'] = 'on'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)
                
        elif user_toggle_input.lower().strip() == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break
        else:
          print("Please enter a valid input.")

    def toggle_idiom_proverbs():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_idiom_proverbs_list_simple()
        print_idiom_proverbs_list_complex()
        user_toggle_input = input("\nDo you want to toggle" + Fore.RED + " ALL " + Style.RESET_ALL + "Idioms-Proverbs" + Fore.RED + " OFF " + Style.RESET_ALL + "or" + Fore.GREEN + " ON" + Style.RESET_ALL + "? [OFF/ON] (Press 'q' to quit): ")
        
        if user_toggle_input.lower().strip() == 'off':
          for word in data:
            if word['type'] == 'Idioms-Proverbs' and word['enabled'] == 'on':
              word['enabled'] = 'off'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'on':
          for word in data:
            if word['type'] == 'Idioms-Proverbs' and word['enabled'] == 'off':
              word['enabled'] = 'on'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'q':
          break
        else:
          print("Please enter a valid input.\n")

    def toggle_idiom_proverbs_simple():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_idiom_proverbs_list_simple()
        user_toggle_input = input("\nDo you want to toggle" + Fore.RED + " ALL " + Style.RESET_ALL + "SIMPLE Idioms-Proverbs" + Fore.RED + " OFF " + Style.RESET_ALL + "or" + Fore.GREEN + " ON" + Style.RESET_ALL + "? [OFF/ON] (Press 'q' to quit): ")
        
        if user_toggle_input.lower().strip() == 'off':
          for word in data:
            if word['type'] == 'Idioms-Proverbs' and word['difficulty'] == 'Simple' and word['enabled'] == 'on':
              word['enabled'] = 'off'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'on':
          for word in data:
            if word['type'] == 'Idioms-Proverbs' and word['difficulty'] == 'Simple' and word['enabled'] == 'off':
              word['enabled'] = 'on'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break
        else:
          print("Please enter a valid input.")

    def toggle_idiom_proverbs_complex():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_idiom_proverbs_list_complex()
        user_toggle_input = input("\nDo you want to toggle" + Fore.RED + " ALL " + Style.RESET_ALL + "COMPLEX words" + Fore.RED + " OFF " + Style.RESET_ALL + "or" + Fore.GREEN + " ON" + Style.RESET_ALL + "? [OFF/ON] (Press 'q' to quit): ")
        
        if user_toggle_input.lower().strip() == 'off':
          for word in data:
            if word['type'] == 'Idioms-Proverbs' and word['difficulty'] == 'Complex' and word['enabled'] == 'on':
              word['enabled'] = 'off'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'on':
          for word in data:
            if word['type'] == 'Idioms-Proverbs' and word['difficulty'] == 'Complex' and word['enabled'] == 'off':
              word['enabled'] = 'on'
              # Convert the dictionary back into a JSON string
              json_data = json.dumps(data,indent=4)

              # Open the file in write mode
              with open("../text_files/wordlist.txt", "w") as f:
                # Write the modified JSON string to the file
                f.write(json_data)

        elif user_toggle_input.lower().strip() == 'q':
          os.system('cls' if os.name == 'nt' else 'clear')
          break
        else:
          print("Please enter a valid input.")

    def toggle_specific_word():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())

      counter = 0
      while True:
        found = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print_word_list_simple()
        print_word_list_complex()

        if counter == 1:
          print(f"The word '{word_input}' does not exist, please try an" + Fore.RED + " EXISTING " + Style.RESET_ALL + "word.\n")

        word_input = input("\nEnter a Word (Press 'q' to quit): ")
        for word in data:
          if word['word'] == word_input and word['type'] == 'Word':
            counter = 0
            found = True
            if found == True:
                if word['enabled'] == 'on':
                  word['enabled'] = 'off'
                  # Convert the dictionary back into a JSON string
                  json_data = json.dumps(data,indent=4)

                  # Open the file in write mode
                  with open("../text_files/wordlist.txt", "w") as f:
                    # Write the modified JSON string to the file
                    f.write(json_data)

                elif word['enabled'] == 'off':
                  word['enabled'] = 'on'
                  # Convert the dictionary back into a JSON string
                  json_data = json.dumps(data,indent=4)

                  # Open the file in write mode
                  with open("../text_files/wordlist.txt", "w") as f:
                    # Write the modified JSON string to the file
                    f.write(json_data)

        if found == False:
          counter = 1

        if word_input.lower().strip() == 'q':
          break

    def toggle_specific_idiom_proverbs():

      # Open the file in read mode
      with open("../text_files/wordlist.txt", "r") as f:
        # Parse the JSON string in the file
        data = json.loads(f.read())
      

      counter = 0
      while True:
        found = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print_idiom_proverbs_list_simple()
        print_idiom_proverbs_list_complex()

        if counter == 1:
          print(f"The Idiom-Proverb '{word_input}' does not exist, please try an" + Fore.RED + " EXISTING " + Style.RESET_ALL + "Idiom-Proverb.\n")

        word_input = input("\nPlease enter an Idiom-Proverb (Enter 'q' to quit): ")
        for word in data:
          if word['word'] == word_input and word['type'] == 'Idioms-Proverbs':
            found = True
            counter = 0
            if found == True:
              if word['enabled'] == 'on':
                word['enabled'] = 'off'
                # Convert the dictionary back into a JSON string
                json_data = json.dumps(data,indent=4)

                # Open the file in write mode
                with open("../text_files/wordlist.txt", "w") as f:
                  # Write the modified JSON string to the file
                  f.write(json_data)
              elif word['enabled'] == 'off':
                word['enabled'] = 'on'
                # Convert the dictionary back into a JSON string
                json_data = json.dumps(data,indent=4)

                # Open the file in write mode
                with open("../text_files/wordlist.txt", "w") as f:
                  # Write the modified JSON string to the file
                  f.write(json_data)

        if found == False:
          counter = 1

        if word_input.lower().strip() == 'q':
          break
  

    counter = 0
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      try:
        print(Fore.GREEN +  '''
         █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
        ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
        ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
        ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
        ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
        ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ''' + Style.RESET_ALL )
        time.sleep(0.04)
        print("\n" + "\t" + "1. Toggle Words")
        time.sleep(0.04)
        print("\n" + "\t" + "2. Toggle Idioms-Proverbs")
        time.sleep(0.04)
        print("\n" + "\t" + Fore.RED + "3. Exit\n" + Style.RESET_ALL)
        time.sleep(0.04)

        if counter == 1:
          counter = 0
          time.sleep(0.04)
          print("   Please choose from options" + Fore.GREEN + " 1 - 3 " + Style.RESET_ALL + "only.\n")

        userInput = int(input("  >>"))

        if userInput == 1:
          counter = 0

          while True:
            try:
              os.system('cls' if os.name == 'nt' else 'clear')
              print_word_list_simple()
              print_word_list_complex()
              time.sleep(0.04)
              print("\n" + "1. Simple Words")
              time.sleep(0.04)
              print("\n" + "2. Complex Words")
              time.sleep(0.04)
              print("\n" + "3. Toggle Specific Words")
              time.sleep(0.04)
              print("\n" + "4. Toggle All Words")
              time.sleep(0.04)
              print("\n" + Fore.RED + "5. Exit\n" + Style.RESET_ALL)

              if counter == 1:
                counter = 0
                time.sleep(0.04)
                print("Please choose from options" + Fore.GREEN + " 1 - 5 " + Style.RESET_ALL + "only.\n")

              toggle_input = int(input(">>"))

              if toggle_input == 1:
                toggle_words_simple()
              elif toggle_input == 2:
                toggle_words_complex()
              elif toggle_input == 3:
                toggle_specific_word()
              elif toggle_input == 4:
                toggle_words()
              elif toggle_input == 5:
                break
              else:
                os.system('cls' if os.name == 'nt' else 'clear')
                counter = 1

            except ValueError:
              os.system('cls' if os.name == 'nt' else 'clear')
              counter = 1

        elif userInput == 2:
          counter = 0
          while True:
            try:
              os.system('cls' if os.name == 'nt' else 'clear')
              print_idiom_proverbs_list_simple()
              print_idiom_proverbs_list_complex()
              time.sleep(0.04)
              print("\n" + "1. Simple Idioms-Proverbs")
              time.sleep(0.04)
              print("\n" + "2. Complex Idioms-Proverbs")
              time.sleep(0.04)
              print("\n" + "3. Toggle Specific Idioms-Proverbs")
              time.sleep(0.04)
              print("\n" + "4. Toggle All Idioms-Proverbs")
              time.sleep(0.04)
              print("\n" + Fore.RED + "5. Exit\n" + Style.RESET_ALL)
              
              if counter == 1:
                counter = 0
                time.sleep(0.04)
                print("Please choose from options" + Fore.GREEN + " 1 - 5 " + Style.RESET_ALL + "only.\n")

              toggle_input = int(input(">>"))
              
              if toggle_input == 1:
                toggle_idiom_proverbs_simple()
              elif toggle_input == 2:
                toggle_idiom_proverbs_complex()
              elif toggle_input == 3:
                toggle_specific_idiom_proverbs()
              elif toggle_input == 4:
                toggle_idiom_proverbs()
              elif toggle_input == 5:
                break
              else:
                os.system('cls' if os.name == 'nt' else 'clear')
                counter = 1

            except ValueError:
              os.system('cls' if os.name == 'nt' else 'clear')
              counter = 1

        elif userInput == 3:
          break
        else:
          counter = 1
      except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 1


  counter = 0
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
      print(Fore.GREEN +  '''
       █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
      ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
      ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
      ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
      ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
      ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ''' + Style.RESET_ALL )
      time.sleep(0.04)
      print("\n" + "\t" + "1. Replace word")
      time.sleep(0.04)
      print("\n" + "\t" + "2. Replace meaning")
      time.sleep(0.04)
      print("\n" + "\t" + "3. Add word and meaning")
      time.sleep(0.04)
      print("\n" + "\t" + "4. Delete word and meaning")
      time.sleep(0.04)
      print("\n" + "\t" + "5. Toggle words")
      time.sleep(0.04)
      print("\n" + "\t" + Fore.RED + "6. Exit" + Style.RESET_ALL + "\n")
      time.sleep(0.04)

      if counter == 1:
        counter = 0
        time.sleep(0.04)
        print("   Please choose from options" + Fore.GREEN + " 1 - 6 " + Style.RESET_ALL + "only.\n")

      userChoice2 = int(input("  >>"))

      if userChoice2 == 1:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        replace_word()
      elif userChoice2 == 2:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        replace_meaning()
      elif userChoice2 == 3:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        add_new_word_meaning()
      elif userChoice2 == 4:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        delete_word_meaning()
      elif userChoice2 == 5:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        toggle_items()
      elif userChoice2 == 6:
        return False
      else:
        counter = 1

    except ValueError:
      os.system('cls' if os.name == 'nt' else 'clear')
      counter = 1

def change_settings():
  
    with open("../text_files/game-settings.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    counter = 0
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      try:
        print(Fore.GREEN +  '''
         █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
        ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
        ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
        ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
        ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
        ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ''' + Style.RESET_ALL )
        time.sleep(0.04)
        print("\n\tEnter the number of the game setting you want to change\n")
        time.sleep(0.04)
        print("\t1. Number of attempts")
        time.sleep(0.04)
        print("\n\t2. Number of words")
        time.sleep(0.04)
        print("\n\t3. Number of top players")
        time.sleep(0.04)
        print("\n\t" + Fore.RED + "4. Exit\n" + Style.RESET_ALL)
        time.sleep(0.04)

        if counter == 1:
          counter = 0
          time.sleep(0.04)
          print("   Please choose from options" + Fore.GREEN + " 1 - 4 " + Style.RESET_ALL + "only.\n")

        choice = int(input(">> "))

        if choice == 1:

          counter = 0

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
          counter = 0

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

          counter = 0

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

          counter = 0

          os.system('cls' if os.name == 'nt' else 'clear')
          break

        else:
          counter = 1
          


        json_data = json.dumps(data,indent=4)

        # Open the file in write mode
        with open("../text_files/game-settings.txt", "w") as f:
          # Write the modified JSON string to the file
          f.write(json_data)
      
      except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 1

def print_report():
  while True:
     try:
      # Read in the start and end dates from the user
      start_date_str = input("Enter the start date (DD-MM-YY): ")
      end_date_str = input("Enter the end date (DD-MM-YY): ")
      os.system('cls' if os.name == 'nt' else 'clear')

      # Convert the date strings to datetime objects
      start_date = datetime.datetime.strptime(start_date_str, "%d-%m-%y")
      end_date = datetime.datetime.strptime(end_date_str, "%d-%m-%y")

      # Open the file containing the game data
      with open("../text_files/game_logs.txt") as f:
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
      time.sleep(0.04)
      print("\nGame Report")
      time.sleep(0.04)
      print("------------")
      time.sleep(0.04)
      print(Fore.YELLOW + "\nName\t\tPoints\t\tDate Joined\n" + Style.RESET_ALL)

      # Iterate over the games
      for game in games:
            # Convert the date string to a datetime object
            date = datetime.datetime.strptime(game["date"], "%d-%m-%y")
            if start_date <= date <= end_date:
              time.sleep(0.04)
              print(f"{game['name']}\t\t{game['points']}\t\t{game['date']}")
            elif start_date >= date >= end_date:
              time.sleep(0.04)
              print(f"{game['name']}\t\t{game['points']}\t\t{game['date']}")
          

      # Print the report footer
      print("\n------------")

      exit_input = input("\nEnter 'q' to quit: ").lower()
      if exit_input == 'q':
        break

     except ValueError:
      print("Please enter" + Fore.RED + " valid Dates." + Style.RESET_ALL)

if admin_login() is True:
  counter = 0
  while True:

    os.system('cls' if os.name == 'nt' else 'clear')
    try:
      print(Fore.GREEN +  '''
       █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
      ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
      ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
      ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
      ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
      ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ''' + Style.RESET_ALL )
      time.sleep(0.04)
      print("\n" + "\t" + "1. Change word settings")
      time.sleep(0.04)
      print("\n" + "\t" + "2. Change game settings")
      time.sleep(0.04)
      print("\n" + "\t" + "3. Print report")
      time.sleep(0.04)
      print("\n" + "\t" + "4. Change Admin Settings")
      time.sleep(0.04)
      print("\n" + "\t" + Fore.RED + "5. Exit" + Style.RESET_ALL + "\n")
      time.sleep(0.04)

      if counter == 1:
        time.sleep(0.04)
        print("   Please choose from options" + Fore.GREEN + " 1 - 5 " + Style.RESET_ALL + "only.\n")
      
      userChoice = int(input("  >>"))
      if userChoice == 1:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        word_settings()
      elif userChoice == 2:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        change_settings()
      elif userChoice == 3:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print_report()
      elif userChoice == 4:
        counter = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        admin_settings()
      elif userChoice == 5:
        break
      else:
       counter = 1

    except ValueError:
      os.system('cls' if os.name == 'nt' else 'clear')
      counter = 1



