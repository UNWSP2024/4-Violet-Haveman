# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.
from operator import truediv


def main():
    ######################
    print ("Movie Options:", "|","Leo","|", "Moana","|", "Lion King","|", "Gladiator", "|")

    buying_tickets = True
    while buying_tickets == True:
        movie = input("Please state which movie you would like to see: ")
        if movie == "Leo":
         ticket = 8
        elif movie == "Moana":
            ticket = 10
        elif movie == "Lion King":
             ticket = 7
        elif movie == "Gladiator":
            ticket = 12
        else:
            print ("That is not an option")
            buying_tickets = False
        movie_ticket = int(input("How many tickets would you like?" ))
        total = movie_ticket*ticket
        answer = input("Would you like to purchase other tickets? (Y/N)")
        if answer == "Y":
            buying_tickets = True
        else:
            buying_tickets = False
    print ("Your total is: $", total)
    ######################


if __name__ == '__main__':
    main()