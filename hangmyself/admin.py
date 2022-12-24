import json

username = 'admin'
password = '1'

adminUserinput = input("Username: ")
adminPass = input("Password: ")

def word_settings():
  def replace_word():
    # Open the file in read mode
    with open("wordlist.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    found = False
    while not found:
    # Prompt the user for the word to replace
      userInput = input("\nEnter the word to be replaced (enter 'q' to exit): ").strip().lower()

      # Exit the program if the user enters 'q'
      if userInput == 'q':
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

    userInput = input("\nEnter a word that you want to delete (Definition will be deleted too): ").strip().lower()

    found = False
    while not found:
      # Exit the program if the user enters 'q'
      if userInput == 'q':
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
    userChoice2 = int(input("\n" + "\t" + "1. Replace word" + "\n" + "\t" + "2. Replace meaning" + "\n" + "\t" + "3. Add word and meaning"+ "\n" + "\t" + "4. Delete word and meaning"+ "\n" + "\t" + "5. Exit" + "\n" + "\n" + "  >>"))

    if userChoice2 == 1:
      replace_word()
    elif userChoice2 == 2:
      replace_meaning()
    elif userChoice2 == 3:
      print("\nNew Word and Meaning successfully updated!")
      add_new_word_meaning()
    elif userChoice2 == 4:
      print("\nWord and meaning successfully deleted!")
      delete_word_meaning()
    elif userChoice2 == 5:
      return False

def change_settings():
  
    with open("game-settings.txt", "r") as f:
      # Parse the JSON string in the file
      data = json.loads(f.read())

    while True:
        print("\nEnter the number of the game setting you want to change\n")
        choice = int(input("\t1. Number of attempts\n\t2. Number of words\n\t3. Number of top players\n\t4. Exit\n\n>> "))

        if choice == 1:
            new_attempts = int(input("\nEnter the new number of attempts: "))
            data['number of attempts'] = new_attempts
            print("\nChanges made successfully!")
        elif choice == 2:
            new_words = int(input("Enter the new number of words: "))
            data['number of words'] = new_words
            print("\nChanges made successfully!")
        elif choice == 3:
            new_players = int(input("Enter the new number of top players: "))
            data['number of top players'] = new_players
            print("\nChanges made successfully!")
        elif choice == 4:
            break
        else:
            print("\nInvalid choice!")


    
        json_data = json.dumps(data,indent=4)

        # Open the file in write mode
        with open("game-settings.txt", "w") as f:
          # Write the modified JSON string to the file
          f.write(json_data)

if adminUserinput == username and adminPass == password:
    while True:

        print("            _____    __  __   _____   _   _\n    /\     |  __ \  |  \/  | |_   _| | \ | |\n   /  \    | |  | | | \  / |   | |   |  \| |\n  / /\ \   | |  | | | |\/| |   | |   | . ` |\n / ____ \  | |__| | | |  | |  _| |_  | |\  |\n/_/    \_\ |_____/  |_|  |_| |_____| |_| \_|" )
        userChoice = int(input("\n" + "\t" + "1. Change word settings" + "\n" + "\t" + "2. Change game settings" + "\n" + "\t" + "3. Print report" + "\n" + "\t" + "4. Exit" + "\n" + "\n" + "  >>"))
        if userChoice == 4:
          break
        if userChoice == 1:
          word_settings()
        if userChoice == 2:
          change_settings()
        if userChoice ==3:
          print("Work in progress")



else:
 print("Sorry incorrect credentials entered bozo")