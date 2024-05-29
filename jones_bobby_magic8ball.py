'''
Author: Bobby Jones
Date: 11/13/2023
Description: Magic 8 ball code that allows the user to ask a question and gives a random response 
Challenges: Uses a while loop & asks the user their name and incorporates it in response 
Bugs: None
Sources: https://www.pythonforbeginners.com/code-snippets-source-code/magic-8-ball-written-in-python 
https://www.w3resource.com/projects/python/python-projects-5.php
'''
import random #brings in the random library for reference

print('Hello, I am the Magic 8 Ball') #tells the computer to display 'Hello, I am the Magic 8 Ball'
name = input('What is your name? ') #tells computer to display/ask 'What is your name?' and stores the users response as a variable titled 'name' 
print('Hello ' + name) #tells computer to display 'Hello' and the user's name taken as a variable from the previous response 

answers = ["Yes", "No", "Maybe", "Ask Again Later", "Only Time Will Tell"] #creates a list of different answers 

while True: #continuously loop until valid input is provided
    question=input("Ask me, the magic 8 ball a question: (press enter to quit) ") #Display question that asks user to input their own question

    if question=="": #If user presses enter 
        print("Stopping the Game.") #tells computer to display 'Stopping the Game'
        break #ends while loop and program

    print(random.choice(answers)) #tells computer to display an answer takes at random from 'answers' list
 

