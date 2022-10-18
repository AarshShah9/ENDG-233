# school_data.py
# Aarsh Shah, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math.
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

# imports numpy and matplotlib libraries.
import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.


class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(
            self.name, self.code))


# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays
# Creates a dictionary for all school names and codes
schools = {'1224': 'Centennial High School',
           '1679': 'Robert Thirsk School',
           '9626': 'Louise Dean School',
           '9806': 'Queen Elizabeth High School',
           '9813': 'Forest Lawn High School',
           '9815': 'Crescent Heights High School',
           '9816': 'Western Canada High School',
           '9823': 'Central Memorial High School',
           '9825': 'James Fowler High School',
           '9826': 'Ernest Manning High School',
           '9829': 'William Aberhart High School',
           '9830': 'National Sport School',
           '9836': 'Henry Wise Wood High School',
           '9847': 'Bowness High School',
           '9850': 'Lord Beaverbrook High School',
           '9856': 'Jack James High School',
           '9857': 'Sir Winston Churchill High School',
           '9858': 'Dr. E. P. Scarlett High School',
           '9860': 'John G Diefenbaker High School',
           '9865': 'Lester B. Pearson High School'
           }

# Creates a list of all key's from the schools dictionary.
school_number = list(schools.keys())
# Creates a list of all value's from the schools dictionary.
school_name = list(schools.values())

# Add your code within the main function. A docstring is not required for this function.


def main():
    # Print statement for the statistics title.
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    # Creates an array from the 2021 school data and stores it in a variable, then prints the array.
    data_2021 = np.genfromtxt(
        'SchoolData_2020-2021.csv', delimiter=',', skip_header=True)
    print(f'Array Data for 2020 - 2021:\n{data_2021}')

    # Creates an array from the 2020 school data and stores it in a variable, then prints the array.
    data_2020 = np.genfromtxt(
        'SchoolData_2019-2020.csv', delimiter=',', skip_header=True)
    print(f'Array Data for 2019 - 2020:\n{data_2020}')

    # Creates an array from the 2019 school data and stores it in a variable, then prints the array.
    data_2019 = np.genfromtxt(
        'SchoolData_2018-2019.csv', delimiter=',', skip_header=True)
    print(f'Array Data for 2018 - 2019:\n{data_2019}')

    # Add request for user input here
    # Creates a while loop that runs until the user inputs a valid school.
    valid = True
    while valid == True:
        # Asks the user to input the school name or code for which they want data on.
        requested_school = str(input(
            'Please enter the high school name or school code: '))
        # Checks to see if the requested school exists within the database of the school names.
        if requested_school in schools.values():
            # Reassigns the requested schools name to there respective code.
            chosen_school_code = school_number[school_name.index(
                requested_school)]
            # Ends loop.
            valid = False
        # Checks to see if the requested school exists within the database of the school codes.
        elif requested_school in school_number:
            # Reassigns the requested school to the chosen school code variable
            chosen_school_code = requested_school
            # Ends loop
            valid = False
        else:
            # If the user doesn't choose a valid school they are prompted to try again.
            print('You must enter a valid school name or code.')

    # Print Statement for the statistics subtitle.
    print("\n***Requested School Statistics***\n")

    # Prints the school name and code using the given class
    school_1 = School(schools.get(chosen_school_code), chosen_school_code)
    school_1.print_all_stats()

    # Add data processing and plotting here

    # Creates empty list that will store all the chosen school's enrollment data.
    data = []
    # Creates a list that stores the arrays of all the school data.
    list_data = [data_2021, data_2020, data_2019]

    # Creates a while loop that runs until the code runs 3 times (for each grade).
    iteration = 1
    while iteration <= 3:
        # Create a for loop that will run for all 3 years of data.
        for year in range(0, 3):
            # Finds the position of the chosen school code in the given years array.
            position = np.where(list_data[year] == int(chosen_school_code))
            # Reassigns the position from tuple format to individual x y coordinates.
            (x, y) = (position[0], position[1])
            # Stores the enrollment data for given school, year, and grade.
            enrollment = list_data[year][x, y + iteration]
            # Adds the enrollment data to the data list
            data.append(enrollment)
        # Tracks how many times the while loop has run.
        iteration += 1

    # Calculates the mean using the data colllected in the above loops and prints them for all the grades.
    print(
        f'Mean enrollment for Grade 10: {int((data[0][0] + data[1][0] + data[2][0])//3)}')
    print(
        f'Mean enrollment for Grade 11: {int((data[3][0] + data[4][0] + data[5][0])//3)}')
    print(
        f'Mean enrollment for Grade 12: {int((data[6][0] + data[7][0] + data[8][0])//3)}')
    # Adds the total number of graduates using the grade 12 data from the above loops and prints out the result.
    print(
        f'Total number of students graduated in past 3 years: {int(data[6][0] + data[7][0] + data[8][0])}')

    # Creates list for the x-axis.
    grades = [10, 11, 12]
    # Plots the 2021 enrollment data for all the grades using blue dots.
    plt.plot(grades, [data[0][0], data[3][0], data[6][0]],
             'bo', label='2021 Enrollment')
    # Plots the 2020 enrollment data for all the grades using green dots.
    plt.plot(grades, [data[1][0], data[4][0], data[7][0]],
             'go', label='2020 Enrollment')
    # Plots the 2019 enrollment data for all the grades using red dots.
    plt.plot(grades, [data[2][0], data[5][0], data[8][0]],
             'ro', label='2019 Enrollment')
    # Creates a legend using the dot colours and labels assigned in the plt.plot's
    plt.legend(loc='upper left')
    # Creates a title, x and y label for the chart.
    plt.title('Grade Enrollment by Year')
    plt.xlabel('Grade Level')
    plt.ylabel('Number of Students')
    # Makes the x-axis of the chart only have 3 values (grade 10, 11, 12).
    plt.xticks(grades)
    # Prints the chart.
    plt.show()

    # Creates list for the x-axis.
    year = [2019, 2020, 2021]
    # Makes a subplot that spans the upper 1/3 of the chart.
    plt.subplot(3, 1, 1)
    # Plots the grade 10 enrollment data using a yellow dashed line chart over the 3 years.
    plt.plot(year, [data[2][0], data[1][0], data[0][0]],
             'y--', label='Grade 10')
    # Creates a title and y label for the chart.
    plt.title('Enrollment by Grade')
    plt.ylabel('Number of Students')
    # Creates a legend using the yellow dashed line and label assigned in the plt.plot's
    plt.legend(loc='upper right')
    # Makes the x-axis of the chart only have 3 values (the years 2019, 2020, 2021).
    plt.xticks(year)

    # Makes a subplot that spans the middle 1/3 of the chart.
    plt.subplot(3, 1, 2)
    # Plots the grade 11 enrollment data using a magenta dashed line chart over the 3 years.
    plt.plot(year, [data[5][0], data[4][0], data[3][0]],
             'm--', label='Grade 11')
    # Creates a y label for the chart.
    plt.ylabel('Number of Students')
    # Creates a legend using the magenta dashed line and label assigned in the plt.plot's
    plt.legend(loc='upper right')
    # Makes the x-axis of the chart only have 3 values (the years 2019, 2020, 2021).
    plt.xticks(year)

    # Makes a subplot that spans the bottom 1/3 of the chart.
    plt.subplot(3, 1, 3)
    # Plots the grade 12 enrollment data using a cyan dashed line chart over the 3 years.
    plt.plot(year, [data[8][0], data[7][0], data[6][0]],
             'c--', label='Grade 12')
    # Creates a x and y label for the chart.
    plt.xlabel('Enrollment Year')
    plt.ylabel('Number of Students')
    # Creates a legend using the cyan dashed line and label assigned in the plt.plot's
    plt.legend(loc='upper right')
    # Makes the x-axis of the chart only have 3 values (the years 2019, 2020, 2021).
    plt.xticks(year)
    # Prints the chart.
    plt.show()


# Runs the main function.
# Do not modify the code below
if __name__ == '__main__':
    main()
