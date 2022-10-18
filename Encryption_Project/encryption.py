# encryption.py
# Aarsh Shah, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

import string


def secondary_menu(userchoice):
    """
    The secondary_menu is called from the main menu and asks the user to input their message and cyhper.
    In addition it does a series of checks to determine if: the message is alphabetical and removes 
    any spaces, and to check if the cypher is alphanumerical and removes any duplicate values. If the inputs
    pass the checks it calles the encode or decode function depending on what the user chose in the main menu.
    
    Parameters: 
        userchoice: the value associated with if the user chose to encode or decode.
    
    Returns:
        None
    """

    # Stores the alphabet in a variable from the string module
    alphabet = string.ascii_lowercase

    # Asks the user to input the message they want to be encoded/decoded
    message = str(input('Please enter the text to be processed: ').lower())
    # Removes any spaces that are in the inputted messsage
    message = message.replace(' ', '')

    # Checks if the user wants to encode and if the message is alphabetical
    if userchoice == '1':
        if message.isalpha() == True:
            # Asks the user to input their 26 character cipher
            cipher_text = str(
                input(
                    'Please enter the cipher text (alpha-numerical only, 26 characters): '
                ).lower())
        # If it isn't alphabetical it prompts the user to try again
        else:
            print('The provided message is not valid please try again')
            secondary_menu(userchoice)
    # Checks if the user wants to decode and if the message is alphanumerical
    elif userchoice == '2':
        if message.isalnum() == True:
            # Asks the user to input their 26 character cipher
            cipher_text = str(
                input(
                    'Please enter the cipher text (alpha-numerical only, 26 characters): '
                ).lower())
        # If it isn't alphanumerical it prompts the user to try again
        else:
            print('The provided message is not valid please try again')
            secondary_menu(userchoice)

    # Checks to see if the inputted cipher is alpha-numerical
    if cipher_text.isalnum() == True:
        # Removes any duplicate values from the inputted cipher
        cipher_text_no_dup = ''.join(dict.fromkeys(cipher_text))
        # Checks to see if the cipher inputted after removing duplicate values is 26 characters
        if len(cipher_text_no_dup) == 26:
            print('Your cipher is valid.')
            # Calls encode function passing the message, cipher and alphabet if user wanted to encode
            if userchoice == '1':
                encode(message, cipher_text_no_dup, alphabet)
            # Calls decode function passing the message, cipher and alphabet if user wanted to decode
            elif userchoice == '2':
                decode(message, cipher_text_no_dup, alphabet)
        # If the cipher wasn't 26 characters then it allows the user to renter their message and cipher
        else:
            print('The provided cipher is not 26 characters please try again')
            secondary_menu(userchoice)
    # If the cipher wasn't alpha-numerical then it allows the user to renter their message and cipher
    else:
        print('The provided cipher is not alpha-numerical please try again')
        secondary_menu(userchoice)


def encode(message, cipher_text_no_dup, alphabet):
    """
    The encode function takes the users inputted message and reassigns each character with an
    alphanumerical value according to the cipher using a for loop. It then prints out the encoded message.

    Parameters:
        message (str): passes the message inputted from the user in secondary_menu
        cipher_text_no_dup (str): passes the cipher text (with no duplicates) from secondary_menu
        alphabet (str): passes the alphabet string

    Returns:
        None
    """

    # Creates an empty dictionary that will store the key-value pairs for the cipher and alphabet
    new_dic = {}
    # Creates a new variable for the number of iterations that the proceeding for loop has gone through
    iteration = 0

    # For loop that takes every character in the alphabet and assigns it to i
    for i in alphabet:
        # Takes every charcter in the alphabet and assigns it with the cipher in a dictionary
        new_dic[i] = cipher_text_no_dup[iteration]
        # Adds 1 to the iteration value a.k.a. the key value number in the cipher
        iteration += 1

    # Creates empty string that will store the new encoded messsage
    new_msg = ''
    # For loop that takes every character in the message and assigns it to i
    for i in message:
        # Calls the key value from the dictionary and adds each value to the new_msg string
        new_msg += new_dic[i]

    # Prints the new message and calls the main menu function
    print(f'Your output is: {new_msg}\n')
    main_menu()


def decode(message, cipher_text_no_dup, alphabet):
    """
    The decode function takes the users inputted message and reassigns each character with an
    alphanumerical value according to the cipher using a for loop. It then prints out the decoded message.

    Parameters:
        message (str): passes the message inputted from the user in secondary_menu
        cipher_text_no_dup (str): passes the cipher text (with no duplicates) from secondary_menu
        alphabet (str): passes the alphabet string

    Returns:
        None
    """

    # Creates an empty dictionary that will store the key-value pairs for the cipher and alphabet
    new_dic = {}
    # Creates a new variable for the number of iterations that the proceeding for loop has gone through
    iteration = 0
    # For loop that takes every character in the cypher and assigns it to i
    for i in cipher_text_no_dup:
        # Takes every charcter in the cipher and assigns it with the alphabet in a dictionary
        new_dic[i] = alphabet[iteration]
        # Adds 1 to the iteration value a.k.a. the key value number in the alphabet
        iteration += 1

    # Creates empty string that will store the new decoded messsage
    new_msg = ''
    # For loop that takes every character in the message and assigns it to i
    for i in message:
        # Calls the key value from the dictionary and adds each value to the new_msg string
        new_msg += new_dic[i]

    # Prints the new message and calls the main menu function
    print(f'Your output is: {new_msg}\n')
    main_menu()


def main_menu():
    """
    The function main menu asks the user if they would like encode or decode a message, or quit the program.
    Then according to the users choice it wil call the corresponding function (and if its to encode or decode it will
    pass the userchoice value to the secondary_menu function)

    Parameters:
        None

    Returns:
        None
    """

    # Asks the user what they would like to do and stores it in a variable
    user_choice = str(
        input(
            'Would you like to: Encode your text (1), Decode your text (2), End the program (0):\n'
        ))
    # If the user chooses 1 or 2 the function secondary_menu will be called while also passing the userchoice value
    if user_choice == '1':
        secondary_menu(user_choice)
    elif user_choice == '2':
        secondary_menu(user_choice)
    # If the user chooses to quit the program will print a thank you statement then end
    elif user_choice == '0':
        print('Thank you for using the encryption program.')
        quit()
    # If the user inputs any value other than 1, 2 or 3 they will be prompted to try again
    else:
        print('Invalid input, try again')
        main_menu()


# Prints the welcome sentence and calls the main menu function
print("ENDG 233 Encryption Program")
main_menu()
