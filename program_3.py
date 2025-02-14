# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.



def main():
    ######################
    years = int(input("Number of years: "))
    m1 = 0
    for value in range (years):
       for value in range (12):
           month = float(input("Please enter the inches of rainfall from this past month: "))
           m1 =  m1 + month
    months = years * 12
    avg = m1/months
    print ("Total Number of months:", months)
    print ("Total Rainfall =", m1)
    print ("Average rainfall =", avg)






    ######################    


if __name__ == '__main__':
    main()