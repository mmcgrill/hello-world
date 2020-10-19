#import the math and random modules to allow for the ensuing calculations

import math

import random

#define a function computer_choice() that takes a random number from a random generator between 1 and 3 and returns a corresponding value
# of rock paper or scissors

def computer_choice():
    random_num = random.randint(1,3)

    if random_num == 1:
        return 'rock'
    elif random_num == 2:
        return 'paper'
    else:
        return 'scissors'

#define a function user_choice_valid(choice) to return the users choice and store the value

def user_choice_valid(choice):
    return choice == 'rock' or choice == 'paper' or choice == 'scissors'

# define a function new_user_choice(choice) to check whether the user inputted a valid choice for the game

def new_user_choice(choice):
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        print('That is not a valid choice. ')
        choice = input('Enter rock, paper, or scissors: ')
    return choice

#define a function that computes who wins between the choices of the computer and the user

def win(player, computer):
    if player == 'rock' and computer == 'scissors':
        return True
    elif player == 'scissors' and computer == 'paper':
        return True
    elif player == 'paper' and computer == 'rock':
        return True
    else:
        return False

# assign computer_choice() to the variable user_choice to call the function defined earlier

computer_choice = computer_choice()
user_choice = input("Enter rock, paper, or scissors: ")
#if the user's initial choice was invalid, assign user choice to their new user choice of rock paper or scissors
if not user_choice_valid(user_choice):
    user_choice = new_user_choice(user_choice)

#when the user choice is the same as the computer choice, the match is a tie

while user_choice == computer_choice:
    print("Computer's choice: " + str(computer_choice) + " Your choice: " + str(user_choice))
    print("You have tied, choose again.")

# assigns the computer choice function to a variable, asking for input if the initial choice is not valid

    computer_choice = computer_choice()
    user_choice = input("Choose rock, paper, or scissors")

    if not user_choice_valid(choice):
        user_choice = new_user_choice(user_choice)

# tells the player he wins

if win(user_choice, computer_choice):
    print("Computer's choice: " + str(computer_choice) + " Your choice: " + str(user_choice))
    print("Congrate! You win.")

# tells the player he lost
    
else:
    print("Computer's choice: " + str(computer_choice) + " Your choice: " + str(user_choice))
    print("Too bad. Better luck next time.")
