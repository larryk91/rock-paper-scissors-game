# game.py
import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Choose 'rock', 'paper', or 'scissors':  ")

if user_choice in ["rock","paper","scissors"]: 
    print("You chose:")
    print(user_choice)
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
    print("Congratulation! You won!")
elif user_choice == "paper" and comp_choice == "paper":
    print("You drew")
elif user_choice == "paper" and comp_choice == "scissors":
    print("Oh the computer won. Maybe nexttime.")
elif user_choice == "paper" and comp_choice == "rock": 
    print("Congratulation! You won!")
elif user_choice == "scissors" and comp_choice == "scissors":
    print("You drew")
elif user_choice == "scissors" and comp_choice == "rock":
    print("Oh the computer won. Maybe nexttime.")
else: 
    print("Congratulation! You won!")

print("Thanks for playing! Please play again!")

