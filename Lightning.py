def main():

    #Gather user input on how many lines they want the table to be
    lines=eval(input("How many lines do you want in your table?"))

    print("Seconds/Distance Table for each .5 seconds that Lightning waves Travel")

    #Print the labels time, distance, and distance as the variables of the table
    print("Time","\t","Distance","\t","Distance")

    #Print the units that each variable uses below
    print("seconds","  ","feet","\t","miles")

    #set seconds = to 0.0 outside of the loop
    seconds=0.0
    
    #Loop to get calculations for each .5 seconds,of the feet, and miles
    #that the lightning sound waves travel
    for i in range (0,lines):
        seconds= i/2
        feet=seconds*1100
        miles=feet/5280
        
        #Print the calculations made, under the correct variables in the table
        print(seconds,"\t",str(feet)+"\t\t"+str(miles))
        
#close the main
main()
