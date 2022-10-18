# calculator.py
# Aarsh Shah, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical operator containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#


# Asks user to input the first integer variable and stores it in a variable.
user_num1 = int(input('Enter the first value: '))
# Asks user to input the first operator and stores it in a variable.
user_oper1 = input('Enter the first operator (Use: *, /, +, -): ')
# Asks user to input the second integer variable and stores it in a variable.
user_num2 = int(input('Enter the second value: '))
# Asks user to input the second operator and stores it in a variable.
user_oper2 = input('Enter the second operator (Use: *, /, +, -): ')
# Asks user to input the third integer value and stores it in a variable.
user_num3 = int(input('Enter the third value: '))


# Checks if operator 1 and 2 is multiplication or division.
if user_oper1 == '*' or user_oper1 == '/':
    if user_oper2 == '*' or user_oper2 == '/':
        # Checks if operator 1 is multiplication.
        if user_oper1 == '*':
            # Multiplies 1st number by the 2nd number.
            answer1 = user_num1 * user_num2
        # Checks if operator 1 is division.
        elif user_oper1 == '/':
            # Divides the 1st number by the 2nd number.
            answer1 = user_num1 // user_num2
        # Checks if operator 2 is multiplication.
        if user_oper2 == '*':
            # Multiplies the answer to the previous operator by the 3rd number.
            final_answer = answer1 * user_num3
        # Checks if operator 2 is division.
        elif user_oper2 == '/':
            # Divides the answer to the previous operator by the 3rd number.
            final_answer = answer1 // user_num3


# Checks if operator 1 and 2 are addition or subtraction.
if user_oper1 == '+' or user_oper1 == '-':
    if user_oper2 == '+' or user_oper2 == '-':
        # Checks if operator 1 is addition.
        if user_oper1 == '+':
            # Adds the 1st number with the 2nd number.
            answer1 = user_num1 + user_num2
        # Checks if operator 1 is subtraction.
        elif user_oper1 == '-':
            # Subtracts the 1st number with the 2nd number.
            answer1 = user_num1 - user_num2
        # Checks if operator 2 is addition.
        if user_oper2 == '+':
            # Add answer to the previous operator with the 3rd number.
            final_answer = answer1 + user_num3
        # Checks if operator 2 is subtraction.
        elif user_oper2 == '-':
            # Subtracts answer to the previous operator with the 3rd number.
            final_answer = answer1 - user_num3


# Checks operator 1 is multiplication or division.
if user_oper1 == '*' or user_oper1 == '/':
    # Checks if operator 2 is addition or subtraction.
    if user_oper2 == '+' or user_oper2 == '-':
        # Checks if operator 1 is multiplication.
        if user_oper1 == '*':
            # Multiplies 1st number by the 2nd number.
            answer1 = user_num1 * user_num2
        # Checks if operator 1 is division.
        elif user_oper1 == '/':
            # Divides 1st number by the 2nd number.
            answer1 = user_num1 // user_num2
        # Checks if operator 2 is addition.
        if user_oper2 == '+':
            # Adds the answer to the previous operator with the 3rd number.
            final_answer = answer1 + user_num3
        # Checks if operator 2 is subtraction.
        elif user_oper2 == '-':
            # Subtracts the answer to the previous operator with the 3rd number.
            final_answer = answer1 - user_num3


# Checks if operator 1 is addition or subtraction.
if user_oper1 == '+' or user_oper1 == '-':
    # Checks if operator 1 is multiplication or division.
    if user_oper2 == '*' or user_oper2 == '/':
        # Checks if operator 2 is multiplication.
        if user_oper2 == '*':
            # Multiplies 2nd number by the 3rd number.
            answer1 = user_num2 * user_num3
        # Check if operator 2 is division.
        elif user_oper2 == '/':
            # Divides the 2nd number by the 3rd number.
            answer1 = user_num2 // user_num3
        # Checks if operator 1 is addition.
        if user_oper1 == '+':
            # Adds the 1st number with the answer of the previous operator.
            final_answer = user_num1 + answer1
        # Checks if operator 1 is subtraction.
        elif user_oper1 == '-':
            # Subtracts the 1st number with the answer of the previous operator.
            final_answer = user_num1 - answer1


# Prints the full expression entered by the user while converting the variables to strings.
print('Entered expression:', str(user_num1), str(user_oper1),
      str(user_num2), str(user_oper2), str(user_num3))
# Prints the final answer of the calculations while converting it to a string.
print('Your final answer =', (str(final_answer)))
