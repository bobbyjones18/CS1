'''
Author: Bobby Jones
Date: 3/29/2024
Description: This program generates menus for a restaurant offering sushi and hibachi dishes. It prompts users to select their preferred cuisine and specify the number of menu items. The program then randomly selects items, displays their names, prices, and descriptions, calculates the total cost, and presents it to the user.
Challenges:
1. Implementing parallel arrays for menu items, prices, and descriptions.
2. Generating costs for each item and calculating the total.
3. Handling user input validation and preventing duplicates.
4. Ensuring user-friendly prompts and instructions.

Bugs: User may ask for too many items. 
Sources: https://www.youtube.com/watch?v=PMgdtUEH2lk
https://www.w3schools.com/python/python_arrays.asp
https://www.w3schools.com/python/python_for_loops.asp

'''



# Food-o-Matic: A Restaurant Menu Generator

import random  # Importing the random module for generating random menu items

# Welcome message
print("Welcome to Food-o-Matic - Your Restaurant Menu Generator!\n")

# Initialize parallel arrays for menu items and their descriptions for sushi (raw bar)
sushi_items = [
    "Nigiri Sushi", "Maki Roll", "Sashimi", "California Roll",
    "Dragon Roll", "Rainbow Roll"
]

sushi_prices = [
    8.99, 10.99, 12.99, 11.99, 13.99, 14.99
]

sushi_descriptions = [
    "Slices of fish or seafood on top of a small bed of rice",
    "Sushi rolled in seaweed with various fillings",
    "Thinly sliced raw fish or seafood",
    "Sushi roll with crab, avocado, and cucumber",
    "Sushi roll with eel and avocado, topped with avocado slices",
    "Sushi roll with assorted fish and avocado slices on top"
]

# Initialize parallel arrays for menu items and their descriptions for hibachi (cooked food)
hibachi_items = [
    "Hibachi Chicken", "Hibachi Shrimp", "Hibachi Steak", "Hibachi Vegetables", "Hibachi Tofu"
]

hibachi_prices = [
    15.99, 17.99, 19.99, 14.99, 13.99
]

hibachi_descriptions = [
    "Grilled chicken cooked with vegetables and served with rice",
    "Grilled shrimp cooked with vegetables and served with rice",
    "Grilled steak cooked with vegetables and served with rice",
    "Assorted vegetables grilled and served with rice",
    "Grilled tofu cooked with vegetables and served with rice"
]

# Function to calculate total cost
def calculate_total_cost(menu, num_items):
    total_cost = 0
    for _ in range(num_items):
        total_cost += menu_prices[random.randint(0, len(menu) - 1)]
    return total_cost

# Get the type of cuisine from the user
while True:
    cuisine_choice = input("Would you like to see the sushi (Raw Bar) menu or the Hibachi (Cooked Food) menu? ").lower()
    if cuisine_choice == "sushi" or cuisine_choice == "hibachi":
        break
    else:
        print("Please enter 'sushi' or 'hibachi'.")

# Select menu items based on the user's choice
if cuisine_choice == "sushi":
    menu_items = sushi_items
    menu_prices = sushi_prices
    menu_descriptions = sushi_descriptions
elif cuisine_choice == "hibachi":
    menu_items = hibachi_items
    menu_prices = hibachi_prices
    menu_descriptions = hibachi_descriptions

# Get the number of menu items from the user
while True:
    try:
        num_items = int(input("How many menu items do you need? "))
        if num_items < 1 or num_items > len(menu_items):
            raise ValueError
        break
    except ValueError:
        print("Please enter a number between 1 and", len(menu_items))

# Initialize list to keep track of selected items to avoid duplicates
selected_items = []

# Generate the specified number of menu items
print("\nHere are your menu items:")
for _ in range(num_items):
    while True:
        # Randomly select a menu item index
        item_index = random.randint(0, len(menu_items) - 1)
        # Check if the item has already been selected
        if item_index not in selected_items:
            selected_items.append(item_index)
            # Print the selected item and its description
            print(menu_items[item_index] + " - $" + str(menu_prices[item_index]) + " - " + menu_descriptions[item_index])
            break

# Calculate total cost
total_cost = calculate_total_cost(menu_items, num_items)
print("\nTotal cost for all items: $" + str(total_cost))

# Thank you message
print("\nEnjoy your meal at Food-o-Matic!")


