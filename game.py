# game.py
import random
import os
from dotenv import load_dotenv

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the "python-dotenv" package docs for more info
USER_NAME = os.getenv("USER_NAME", default="Player One")

print("Rock, Paper, Scissors, Shoot!")
print(f"Welcome to my game player {USER_NAME}!")

user_choice = input("Choose 'rock', 'paper', or 'scissors':  ")

if user_choice in ["rock","paper","scissors"]: 
    print("You chose:", user_choice)
else:
    print("Your choice is invalid. Capital case matters! Please Try Again!")
    exit()


options = ["rock", "paper", "scissors"]
comp_choice = random.choice(options)
print("The computer chose:", comp_choice)

if user_choice == "rock" and comp_choice == "rock":
    print("You drew")
elif user_choice == "rock" and comp_choice == "paper":
    print("Oh the computer won. Maybe nexttime.")
elif user_choice == "rock" and comp_choice == "scissors": 
    print("Congratulations! You won!")
elif user_choice == "paper" and comp_choice == "paper":
    print("You drew")
elif user_choice == "paper" and comp_choice == "scissors":
    print("Oh the computer won. Maybe nexttime.")
elif user_choice == "paper" and comp_choice == "rock": 
    print("Congratulations! You won!")
elif user_choice == "scissors" and comp_choice == "scissors":
    print("You drew")
elif user_choice == "scissors" and comp_choice == "rock":
    print("Oh the computer won. Maybe nexttime.")
else: 
    print("Congratulations! You won!")

print(f"Thanks for playing {USER_NAME}! Please play again!")

