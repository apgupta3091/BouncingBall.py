# Start the main loop
def main():
    
    # Takes the user inputted String and grabs the first two letters to figure out which month was inputted 
    months=("JanFebMarAprMayJunJulAugSepOctNovDec")
    date=input("Enter the date in mm/dd/yy format:")
    month=int(date[0:2])
    
    #Grabs the abbreviation from the months var based on the postion of month var
    pos=(month-1)*3
    monthsAbbrev=months[pos:pos+3]
    
    #Grabs the day from the user inputted String
    day=int(date[3:5])
    
    #Grabs the Year from the user inputted String
    year=(date[6:])
    
    # Prints the Month + day + year in a new format then what the user entered (mm/dd/yy)        
    print(monthsAbbrev+".",day,"20"+year)
    
#Closes the main loop
main()
