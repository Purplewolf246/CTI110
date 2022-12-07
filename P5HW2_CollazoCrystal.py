# Use of loops, functions and module import to complete assignments
# 12/5/2022
# CTI-110 P5HW2 - Math Quiz
# Crystal Collazo
#
def display_menu(): #need prompt to show up
    print('Welcome to Math Quiz')
    print()
    print('MAIN MENU')
    print('------------------')
    pick_choices()
def pick_choices(): #Need user to select (not sure how yet)
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    input('Please choose one of the menu options: ')
    Exit_program = False
enter = input
display_menu()
guess = []
#If statements (not working?)
if display_menu(1):
    import random
number = random.randint(1,10)
print(number)
print('+',number)
print()
print("Enter Answer.")
int(input(' '))
if display_menu(2):
    import random
number = random.randint(1,10)
print(number)
print('-',number)
print()
print("Enter Answer.")
int(input(' '))
if display_menu(3):
    print("Thank you for playing...")
    print("Bye!!")
    Exit_program = True
#Guessing commands (Not working?)
if guess < number + number:
    print("Sorry, guess is too low.")
    print()
    print("Try again: ")
if guess > number + number:
    print("Sorry, guess is too high.")
    print()
    print("Try again: ")
if guess == number + number:
    print("Congratulations!!!! Your answer is correct..")
    print("Number of guesses:", guess)
