'''
Author: Bobby Jones
Date: 4/23/2024
Description: This program contains a function that is made of the following:
Two functions to reduce the number of print statements needed to “sing” a song (checkpoint)
Takes two numbers and prints their sum
Takes a list and prints every element in that list individually (vertically)
Takes a list and an element and returns a boolean determined by whether the element is in the list
Takes in a parameter and returns a boolean determined by whether that parameter is an integer
Prompts the user for two numbers and prints a random number between the two. 
Takes a string and two characters, then replaces every instance in the string of the first character with the second


Challenges:
Reorganize functions #5 and 6 to improve their efficiency
Takes a string and reverses it
Takes a string and checks whether it is a palindrome
Takes a name and returns the initials

Bugs: None so far


'''


# Function to sing a song with a repeated chorus
def chorus_one():
    print("Don't worry about a thing")
    print("'Cause every little thing is gonna be alright")
    print("Singing, 'Don't worry about a thing")
    print("Cause every little thing is gonna be alright!'")

def chorus_two():
    print("Rise up this mornin'")
    print("Smiled with the risin'sun")
    print("Three little birds")
    print("Pitch by my doorstep")
    print("Singin' sweet songs")
    print("Of melodies pure and true")
    print("Sayin'this is my message to you")

def sing():
    chorus_one()
    chorus_two()
    chorus_one()
    chorus_two()
    chorus_one()
    chorus_one()

import random

# Function to print the sum of two numbers
def add(num1, num2):
    
    # Takes two numbers and prints their sum.
    
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    addition = num1 + num2
    return addition
#Function to print every element in a list vertically
def print_list(list1):
    
    # Takes a list and prints every element in that list individually (vertically).
    
    for item in list1:
        print(item)

# Function to check if an element is in a list
def test_list(list1, element1):
    
    # Takes a list and an element and returns a boolean determined by whether the element is in the list.
    
    return element1 in list1

# Function to check if a parameter is an integer
def is_integer(param):
    
    # Takes in a parameter and returns a boolean determined by whether that parameter is an integer.
    
    return isinstance(param, int)

# Function to print a random number between two numbers
def random_number(num1, num2):
    
    # Prompts the user for two numbers and prints a random number between the two.
    
    return random.randint(num1, num2)

# Function to replace every instance of a character in a string
def replace_char(input_str, char1, char2):
    
    # Takes a string and two characters, then replaces every instance in the string of the first character with the second.
    
    result = ""
    for char in input_str:
        if char == char1:
            result += char2
        else:
            result += char
    return result

# Function to reverse a string
def reverse_string(input_str):
    
    # Takes a string and reverses it.
    
    return input_str[::-1]

# Function to check if a string is a palindrome
def is_palindrome(input_str):
    
    # Takes a string and checks whether it is a palindrome.
    
    return input_str == input_str[::-1]

# Function to get initials from a name
def get_initials(name):
    
    # Takes a name and returns the initials.
    
    words = name.split()
    initials = "".join(word[0] for word in words)
    return initials


# Main function to call other functions
def main():
    
  #Main function to call other functions.
    
    # Test function 1
    sing()

    print("-----------------")
    # Test function 2
    print("Sum:", add(5, 10))
    
    print("-----------------")
    
    # Test function 3
    print("Printing list:")
    print_list(["apple", "banana", "cherry"])
    
    print("-----------------")
    
    # Test function 4
    cities = ["New York", "Tokyo", "Los Angeles", "Berlin", "Miami", "Paris"]
    print("Is 'New York' in the list?", test_list(cities, "New York"))
    print("Is 'Greenwich' in the list?", test_list(cities, "Greenwich"))
    
    print("-----------------")
    
    # Test function 5
    print("Is 'apple' an integer?", is_integer("apple"))
    print("Is 5 an integer?", is_integer(5))
    
    print("-----------------")
    
    # Test function 6
    print("Random number between 1 and 10:", random_number(1, 10))
    
    print("-----------------")
    
    # Test function 7
    print(replace_char("hello world", "l", "a"))
    
    print("-----------------")
    
    # Test function 8
    print(reverse_string("hello world"))
    
    print("-----------------")
    
    # Test function 9
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    
    print("-----------------")
    
    # Test function 10
    print(get_initials("John Doe"))
    
    print("-----------------")


# Call the main function
main()

