'''
Author: Bobby Jones
Date: 5/2/2024
Description: 
    This code contains three parallel arrays: (1) websites and their (2) usernames and (3) passwords. 
    It prompts the user to enter websites and their usernames and passwords to store in the parallel arrays above. 
    It allows the user to print out the list of websites along with their usernames and passwords, to access a specific website's username and password, and to end the program.
Challenges:
    Allow the user to retroactively add more usernames and passwords
    Allow the user to change usernames and passwords
    Store the list of websites with usernames and passwords in an excel spreadsheet
Bugs: None so far
Sources: https://docs.python.org/3/library/csv.html 
'''

import csv

def display_menu():
    '''
    Display the menu options.
    '''
    print("\nPassword Keeper Menu:")
    print("1. Add website, username, and password")
    print("2. Print list of websites with usernames and passwords")
    print("3. Access specific website's username and password")
    print("4. Exit")

def add_website_info(websites, usernames, passwords):
    '''
    Add website, username, and password to the respective lists.

    Args:
        websites (list): List of websites.
        usernames (list): List of usernames.
        passwords (list): List of passwords.
    Returns:
        None
    '''
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
    print("Website, username, and password added successfully!")

def print_entries(websites, usernames, passwords):
    '''
    Print the list of websites with their respective usernames and passwords.

    Args:
        websites (list): List of websites.
        usernames (list): List of usernames.
        passwords (list): List of passwords.
    Returns:
        None
    '''
    print("\nList of websites with usernames and passwords:")
    for i in range(len(websites)):
        print("Website:", websites[i])
        print("Username:", usernames[i])
        print("Password:", passwords[i])
        print()

def access_entry(websites, usernames, passwords):
    '''
    Access specific website's username and password.

    Args:
        websites (list): List of websites.
        usernames (list): List of usernames.
        passwords (list): List of passwords.
    Returns:
        None
    '''
    website = input("Enter website to access: ")
    if website in websites:
        index = websites.index(website)
        print("\nWebsite:", websites[index])
        print("Username:", usernames[index])
        print("Password:", passwords[index])
    else:
        print("Website not found!")

def save_to_csv(websites, usernames, passwords):
    '''
    Save the website info to a CSV file.

    Args:
        websites (list): List of websites.
        usernames (list): List of usernames.
        passwords (list): List of passwords.
    Returns:
        None
    '''
    with open('password_keeper.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Websites', 'Usernames', 'Passwords'])
        for i in range(len(websites)):
            writer.writerow([websites[i], usernames[i], passwords[i]])
    print("Data saved to password_keeper.csv successfully!")

def main():
    '''
    Main function to manage the password keeper program.
    '''
    websites = []
    usernames = []
    passwords = []
    add_website_info(websites, usernames, passwords) # Initially add a website entry

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_website_info(websites, usernames, passwords)
        elif choice == '2':
            print_entries(websites, usernames, passwords)
        elif choice == '3':
            access_entry(websites, usernames, passwords)
        elif choice == '4':
            save_to_csv(websites, usernames, passwords)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()



