'''
Author: Bobby Jones
Date: 11/30/2023
Description: Allows user to play an adaptive computer in rock paper scissors with two added elements: lizard and spock. 
Challenges: User errors addressed, game count displayed, score limit, two extra weapons, and computer will adapt to repetive weapon being played by the user and move to counter it (kinda computer strategy).
Bugs: None
Sources: https://www.w3schools.com/python/python_operators.asp, https://www.w3schools.com/python/python_lists.asp, https://www.w3schools.com/python/python_conditions.asp
'''



import random  # Import the 'random' module to generate random choices for the computer.
from collections import Counter  # Import the 'Counter' class to count occurrences in a list efficiently.

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors/Spock/lizard): ").lower()
        # Prompt the user for input and convert it to lowercase for case-insensitivity.
        if user_choice in ["rock", "paper", "scissors", "spock", "lizard"]:
            return user_choice  # Return the valid user choice.
        else:
            print("Invalid choice. Please enter rock, paper, scissors, Spock, or lizard.")  # Notify the user of an invalid choice.

def get_computer_choice(player_choices):
    if len(player_choices) >= 5:
        # Predict the player's move if used over 80% of the time
        count = Counter(player_choices)  # Count the occurrences of each choice made by the player.
        most_common_choice, most_common_count = count.most_common(1)[0]
        # Identify the most common choice and its count.
        if most_common_count / len(player_choices) > 0.8:
            counter = determine_counter(most_common_choice)
            # If the player's choice is predictable (used more than 80% of the time), determine the counter choices and notify the user. 
            print(f"Computer predicts you'll choose {most_common_choice}. It counters with {counter[0]} or {counter[1]}.")
            return random.choice(counter)  # Return a random counter choice.
    # Random choice for the first four rounds or if prediction is not triggered
    return random.choice(["rock", "paper", "scissors", "spock", "lizard"])
    # If the prediction condition is not met, make a random choice for the computer.

def determine_winner(player, computer):
    rules = {
        "rock": ["scissors", "lizard"], #rock beats scissors and lizard
        "paper": ["rock", "spock"], #paper beats rock and spock
        "scissors": ["paper", "lizard"], #scissors beat paper and lizard
        "spock": ["rock", "scissors"], #spock beats rock and scissors 
        "lizard": ["paper", "spock"] #lizard beats paper and spock 
    }
    if player == computer:
        return "It's a tie!"  # Return a tie result if the choices are the same.
    elif computer in rules[player]:
        return "You win!"  # Return a user win result if the user's choice beats the computer's choice.
    else:
        return "Computer wins!"  # Return a computer win result if the computer's choice beats the user's choice.

def determine_counter(most_common_choice):
    # Determine the counter choices based on the player's most common choice
    if most_common_choice == "rock":
        return ["paper", "spock"]  # If the player commonly chooses rock, counter with paper or spock.
    elif most_common_choice == "paper":
        return ["scissors", "lizard"]  # If the player commonly chooses paper, counter with scissors or lizard.
    elif most_common_choice == "scissors":
        return ["rock", "spock"]  # If the player commonly chooses scissors, counter with rock or spock.
    elif most_common_choice == "spock":
        return ["paper", "lizard"]  # If the player commonly chooses spock, counter with paper or lizard.
    elif most_common_choice == "lizard":
        return ["rock", "scissors"]  # If the player commonly chooses lizard, counter with rock or scissors.

def play_game():
    user_score = 0  # Initialize the user's score to 0.
    computer_score = 0  # Initialize the computer's score to 0.
    ties = 0  # Initialize the number of ties to 0.
    games_played = 0  # Initialize the number of games played to 0.
    score_limit = 10  # Set a score limit for each player

    player_choices = []  # Create an empty list to store the user's choices.

    while user_score < score_limit and computer_score < score_limit:
        print("\nGame", games_played + 1)  # Print the current game number.
        user_choice = get_user_choice()  # Get the user's choice for the current round.
        player_choices.append(user_choice)  # Add the user's choice to the list of player choices.
        computer_choice = get_computer_choice(player_choices)  # Get the computer's choice for the current round.

        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")  # Display the user and computer choices.
        result = determine_winner(user_choice, computer_choice)  # Determine the winner for the current round.
        print(result)  # Print the result of the current round.

        if "You win!" in result:
            user_score += 1  # Increment the user's score if they win the round.
        elif "Computer wins!" in result:
            computer_score += 1  # Increment the computer's score if it wins the round.
        else:
            ties += 1  # Increment the number of ties if the round is a tie.

        games_played += 1  # Increment the total number of games played.
        print(f"\nUser Score: {user_score}, Computer Score: {computer_score}, Ties: {ties}")  # Display the current scores.

    print("\nGame Over!")  # Print a message indicating that the game is over.
    print(f"Final Score: User {user_score} - {computer_score} Computer - Ties {ties}")  # Display the final scores.
    print("Thanks for playing!")  # Print a closing message.

if __name__ == "__main__":
    play_game()  # Start the game if the script is run as the main module.


