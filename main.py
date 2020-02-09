# CSE 4283 Software Testing and QA Assignment 2
# by Timothy Reaux
# main.py

# command line interface application that can calculate BMI and retirement age based on user input
from BMI import *
from retire import *

# function that starts the CLI
def interface():

    print('Calculate your BMI or the age you will be able to retire!')
    print('To choose an option, enter the number corresponding to what you want to do. You can enter 0 at any time to exit.')

    # input for calculation choice
    while(1):
        print('\t-1- Calculate BMI')
        print('\t-2- Calculate retirement age')
        print('\t-0- Exit')

        choice = input('\nchoice: ')

        if choice == '0':
            break

        elif choice == '1':
            print('\nBMI\n')

            # input for height to go in BMI()
            while(1):
                height = input('height: ')
                if height == '0':
                    break

                try:
                    height = int(height)
                    if height > 0:
                        break
                    else:
                        print('Invalid input, try again.')

                except ValueError:
                    print('Invalid input, try again.')

            if height == '0':
                break

            # input for weight to go in BMI()
            while(1):
                weight = input('weight: ')
                if weight == '0':
                    break

                try:
                    weight = int(weight)
                    if weight > 0:
                        break
                    else:
                        print('Invalid input, try again.')

                except ValueError:
                    print('Invalid input, try again.')

            if weight == '0':
                break

            bmi_list = BMI(height, weight)
            bmi_string = 'Your calculated BMI is ' + str(bmi_list[0]) + '. You are classified as ' + str(bmi_list[1]) + '.\n'
            print(bmi_string)

        elif choice == '2':
            print('\nRetirement age\n')

            # input for age to go in retire()
            while(1):
                age = input('current age: ')
                if age == '0':
                    break

                try:
                    age = int(age)
                    if age > 0:
                        break
                    else:
                        print('Invalid input, try again.')

                except ValueError:
                    print('Invalid input, try again.')

            if age == '0':
                break

            # input for salary to go in retire()
            while(1):
                salary = input('yearly salary: ')
                if salary == '0':
                    break

                try:
                    salary = int(salary)
                    if salary > 0:
                        break
                    else:
                        print('Invalid input, try again.')

                except ValueError:
                    print('Invalid input, try again.')

            if salary == '0':
                break

            # input for percentage to go in retire()
            while(1):
                percentage = input('percentage of salary saved: ')
                if percentage == '0':
                    break

                try:
                    percentage = int(percentage)
                    if percentage > 0 and percentage < 100:
                        break
                    else:
                        print('Invalid input, try again.')

                except ValueError:
                    print('Invalid input, try again.')

            if percentage == '0':
                break

            # input for savings goal to go in retire()
            while(1):
                goal = input('savings goal: ')
                if goal == '0':
                    break

                try:
                    goal = int(goal)
                    if goal > 0:
                        break
                    else:
                        print('Invalid input, try again.')

                except ValueError:
                    print('Invalid input, try again.')

            if goal == '0':
                break

            r_age = retire(age, salary, (percentage / 100), goal)
            print('Assuming you live until 100, you will save that much by age: ')
            r_age = '\t' + str(r_age) + '\n'
            print(r_age)

        else:
            print('\nInvalid input, try again.\n')


interface()
