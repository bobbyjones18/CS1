'''
Author: Bobby Jones
Date: 11/5/2023
Description: Allows user to interact with a series of prompts which recreates my morning routine
Challenges: User errors addressed via while loops and input string conversions to lowercase
Bugs:
None
Sources:
https://stackoverflow.com/questions/12719586/how-to-let-python-recognize-both-lower-and-uppercase-input
https://stackoverflow.com/questions/19408087/how-to-do-user-input-error-handling-in-python
https://www.w3schools.com/python/python_while_loops.asp
'''

# Function to get user input with error handling
def get_user_input(prompt, valid_inputs):
    while True:  # Continuously loop until valid input is provided
        user_input = input(prompt).lower()  # Get user input and convert it to lowercase
        if user_input in valid_inputs:  # Check if the input is in the list of valid inputs
            return user_input  # Return the valid user input
        else:
            print("Invalid input. Please try again.")  # Display an error message

# Step 1: Wake up
input("You wake up. Press Enter to continue...")  # Display a message and wait for user to press Enter

# Step 2: Check the weather
while True:  # Continuously loop until valid weather is provided
    weather = input("Is it sunny or rainy outside? ").lower()  # Get user input about the weather and convert it to lowercase
    
    if weather == "sunny":  # If it's sunny
        print("It's a beautiful sunny day!")  # Display a message about the weather
        break  # Exit the loop
    elif weather == "rainy":  # If it's rainy
        print("It's raining. Don't forget your umbrella!")  # Display a message about the weather
        break  # Exit the loop
    else:
        print("Please enter 'sunny' or 'rainy'.")  # Display an error message for invalid input

# Step 3: Get dressed
while True:  # Continuously loop until valid clothing choice is provided
    clothes = input("Are you wearing something casual or formal? ").lower()  # Get user input about clothing and convert it to lowercase

    if clothes == "casual":  # If casual clothing
        print("You choose a casual outfit.")  # Display a message about clothing choice
        break  # Exit the loop
    elif clothes == "formal":  # If formal clothing
        print("You decide to dress formally today.")  # Display a message about clothing choice
        break  # Exit the loop
    else:
        print("Please enter 'casual' or 'formal'.")  # Display an error message for invalid input

# Step 4: Brush your teeth
while True:  # Continuously loop until valid toothbrush choice is provided
    toothbrush = input("Do you want to use an electric toothbrush or a regular toothbrush? ").lower()  # Get user input about toothbrush choice and convert it to lowercase

    if toothbrush == "electric":  # If electric toothbrush
        print("You use an electric toothbrush for a thorough clean.")  # Display a message about toothbrush choice
        break  # Exit the loop
    elif toothbrush == "regular":  # If regular toothbrush
        print("You stick with a regular toothbrush for a quick brush.")  # Display a message about toothbrush choice
        break  # Exit the loop
    else:
        print("Please enter 'electric' or 'regular'.")  # Display an error message for invalid input

# Step 5: Have breakfast
print("Time for a delicious breakfast!")  # Display a message
while True:  # Continuously loop until valid breakfast choice is provided
    breakfast_choice = input("What do you want to have for breakfast, cereal or pancakes? ").lower()  # Get user input about breakfast choice and convert it to lowercase

    if breakfast_choice == "cereal":  # If cereal
        print("You have a quick and healthy bowl of cereal.")  # Display a message about breakfast choice
        break  # Exit the loop
    elif breakfast_choice == "pancakes":  # If pancakes
        print("You make fluffy pancakes with maple syrup.")  # Display a message about breakfast choice
        break  # Exit the loop
    else:
        print("Please enter 'cereal' or 'pancakes'.")  # Display an error message for invalid input

# Step 6: Check your tasks
while True:  # Continuously loop until valid choice is provided
    tasks = input("Do you want to check your to-do list? (yes/no) ").lower()  # Get user input about checking tasks and convert it to lowercase

    if tasks == "yes":  # If user wants to check tasks
        print("You review your tasks for the day.")  # Display a message about checking tasks
        break  # Exit the loop
    elif tasks == "no":  # If user doesn't want to check tasks
        print("You decide to trust your memory for now.")  # Display a message about not checking tasks
        break  # Exit the loop
    else:
        print("Please enter 'yes' or 'no'.")  # Display an error message for invalid input

# Step 7: Grab your backpack
while True:  # Continuously loop until valid choice is provided
    backpack = input("Do you have everything you need in your backpack? (yes/no) ").lower()  # Get user input about checking the backpack and convert it to lowercase

    if backpack == "yes":  # If everything is in the backpack
        print("You have all your essentials in your backpack.")  # Display a message about having everything in the backpack
        break  # Exit the loop
    elif backpack == "no":  # If something is missing in the backpack
        print("You double-check your backpack to make sure you have everything.")  # Display a message about checking the backpack
        break  # Exit the loop
    else:
        print("Please enter 'yes' or 'no'.")  # Display an error message for invalid input

# Step 8: Leave for school or work
print("You head out the door to begin your day. Have a great day!")  # Display a message

# End of the program



