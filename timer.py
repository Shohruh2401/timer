"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""
# This program is timer that counts down
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 
# Importing the random library to be able to choose a random player as the winner.
import random

# get_players() is a function to make sure the number of players being entered by the user is an integer and more than 0.
def get_players():
  while True:
    try:
      player_count = int(input("Please mention the number of Players in the game: "))
      if player_count <= 0:
        print("Please enter a valid number of players or exit the program.")
      else:
        return player_count
    except ValueError: 
      print("Invalid entry. The number must be an integer.")

# Ending image we will show when time is up.
im = Image.open("times-up.jpeg")

# Compiling a list of players by naming each one Player 1, Player 2, Player 3, etc.
players = [f"Player {i+1}" for i in range(get_players())]

# Just waiting for 2 seconds for a better UX
print("Launching...")
time.sleep(2)

# The game starts by all users standing.
print("Players stand\n\n")

# Asks user to enter the end time.
set_time = int(input("Please set your timer in seconds: "))

time.sleep(set_time)

im.show()

last_to_sit = random.choice(players)

print(f'\nCongratulations, {last_to_sit} is the Winner!\n")

