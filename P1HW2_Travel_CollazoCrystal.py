#Create a program that allows user to enter the name and cost of an expense.
#10/10/2022
#CTI-110 P1HW2 - Travel Expense
#Crystal Collazo
#
#Input
budget = 1200
gascos = 250
accomcos = 300
foodcos = 200
expense = gascos + accomcos + foodcos
balance = budget - expense
tax = balance * 0.6
peryear = tax * 12
#Process
print ('Enter Budget:',budget)
print ('Gas cost:',gascos)
print ('Accomodation:',accomcos)
print ('Food cost:',foodcos)
print ('Total expense:',expense)
print ('Remaining Balance:',balance)
print ('Tax:',tax)
print ('Cost Per Year:',peryear)
#Output
