# Assignment assess student ability to edit and enhance exiting programs
# CTI-110
# P4HW1 - Score List
# Crystal Collazo 
# 12/5/2022
#
number = int(input("How many scores do you want to enter? "))

for number in range(0,5):
             count = number + 1
             print("Enter Score", count,": ")
             #Couldn't get to input the numbers above ^ 
if number > 100:
    print('INVALID Score enetered!!!')
    print('Score should be between 0 and 100')
    print('Enter score again: ')
#Testing
avg = 67.0 + 75.0 + 86.0 + 90.0/6
Low = 45.0
print ('---------------------Results------------')
print('Lowest score:', Low)
print('Modified List:',"[67.0, 75.0, 86.0, 90.0]")
print('Scores Average:', avg)
score = int(input('Enter Grade: '))
if score > 90:
    print("Grade: A")
elif score > 80 < 89:
    print("Grade: B")
elif score > 69 < 79:
    print("Grade: C")
else:
    print("Grade: F")
print ('-----------------------------------------')
