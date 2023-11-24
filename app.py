#create scissors Python minigame 
#the winner of the game is determined by three simple rules Rock beats scissors, Scissors beat paper, Paper beats rock
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#user inputs, should be in lowercase and informing the user if the option is invalid
#the computer will randomly select one of the three options
#Display the player's score at the end of the game.
#the user will be prompted to play again
#the user will be prompted to enter their name

import random
import sys

#function to determine the winner
def winner(user, computer):
    if user == computer:
        return "tie"
    elif user == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "user"
    elif user == "paper":
        if computer == "scissors":
            return "computer"
        else:
            return "user"
    elif user == "scissors":
        if computer == "rock":
            return "computer"
        else:
            return "user"
    else:
        return "invalid"
    
#function to play the game

def play_game():
    #user inputs
    user = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose " + computer + ".")
    #determine the winner
    winner_user = winner(user, computer)
    if winner_user == "tie":
        print("It's a tie!")
        print("Score: 0")
    elif winner_user == "invalid":
        print("Invalid input. Please try again.")
    else:
        print(winner_user + " wins!")
        print("Score: 1")
    #ask user to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")
        sys.exit()

#function to get user name
def get_name():
    name = input("Enter your name: ")
    print("Hello " + name + "!")
    play_game()

#main function
def main():
    print("Welcome to Rock, Paper, Scissors!")
    get_name()

if __name__ == "__main__":  
    main()


