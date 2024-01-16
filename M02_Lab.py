# Name: Kobe Hillman
# File Name: M02_Lab.py
# This program accepts student names and GPAs and tests if the student qualifies for the Dean's List or the Honor Roll.

while True:
    lastName = input('Enter last name: ')
    if lastName == 'ZZZ':
        break
    else:
        firstName = input('Enter first name: ')
        userGPA = float(input('Enter GPA: '))

        if userGPA >= 3.50:
            print("This student has made the Dean's List.")
        if 3.25 <= userGPA < 3.50:
            print("This student has made the Honor Roll.")
        elif userGPA < 3.25:
            print("You did not qualify for the Dean's List or the Honor Roll.")