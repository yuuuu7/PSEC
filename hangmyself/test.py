import datetime
import json

def print_report():
     # Read in the start and end dates from the user
     start_date_str = input("Enter the start date (DD-MM-YY): ")
     end_date_str = input("Enter the end date (DD-MM-YY): ")

     # Convert the date strings to datetime objects
     start_date = datetime.datetime.strptime(start_date_str, "%d-%m-%y")
     end_date = datetime.datetime.strptime(end_date_str, "%d-%m-%y")

     # Open the file containing the game data
     with open("game_logs.txt") as f:
          # Read in the contents of the file and parse the JSON data
          games = json.loads(f.read())

     # Sort the games by date
     games.sort(key=lambda x: x["date"])

     # Print the report header
     print("Game Report")
     print("------------")

     # Iterate over the games
     for game in games:
          # Convert the date string to a datetime object
          date = datetime.datetime.strptime(game["date"], "%d-%m-%y")

          # If the game date is within the specified range, print the game data
          if start_date <= date <= end_date:
               print(f"{game['name']}\t{game['points']}\t{game['date']}\n")
          elif start_date >= date >= end_date:
               print(f"{game['name']}\t{game['points']}\t{game['date']}\n")

     # Print the report footer
     print("------------")


print_report()