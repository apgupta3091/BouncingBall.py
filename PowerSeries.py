# Official Name: Anuj Gupta
#Lab section:M5
#email:apgupta@syr.edu
#Assignment 3, problem 1
#Date: 9/19/2019
#PowerSeries.py

#Main program that asks for the number of terms, then uses that
#number of terms to compute a series with user inputed denominator
#that finally subtracts the last num in series-1 to see how close
#series gets to 1.

#Main loop begins
def main():

    #Initialize k and the sum
    k = 0
    sum = 0

    #Ask for the user input of the denominator as well as the number of terms
    den,terms = eval(input("Enter the denominator and then the number of terms:"))

    #Create a loop that computes the series with the given denominator
    #and for the given amount of terms provided by the user
    #This series is =1/denominator**1+1/denominator**2...
    for i in range (1,(terms+1)):
        k=k+1
        serie=1/den**k
        
        #Get the sum for each term and print it
        sum = serie + sum
        print(k, sum)

    #print the final sum outside of the loop
    print("sum = ",sum)
    
    #Calculate (1/(denominator-1)-sum) and print it
    print("(1/",den-1,")-sum =",1/(den-1)-sum)

#Close the main program.
main()
