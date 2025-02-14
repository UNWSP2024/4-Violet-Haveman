# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.
from calendar import different_locale


def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
budget = float(input("Please state your budget: "))
add_expense = True
spent = 0
while add_expense == True:
    expenses = float(input("Please input an expense: "))
    spent = expenses + spent
    answer = input("Is there another expense? (Y/N) ")
    if answer == 'Y':
         add_expense = True
    else:
         add_expense = False
difference = budget - spent
if difference < 0:
    print ("You are over your budget by: $", difference)
elif difference >= 0:
    print ("You are under your budget by: $", difference)



    ######################


if __name__ == '__main__':
    main()