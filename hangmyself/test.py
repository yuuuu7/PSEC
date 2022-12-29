import datetime
import json
import os

def print_report():
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

     # Iterate over the games
     for game in games:
          # Convert the date string to a datetime object
          date = datetime.datetime.strptime(game["date"], "%d-%m-%y")

          print(f"{game['name']}\t{game['points']}\t{game['date']}")
        

     # Print the report footer
     print("------------")


print_report()
