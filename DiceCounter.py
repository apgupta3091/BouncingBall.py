#Anuj Gupta
#lab section m5
#Lab 16
#DiceCounter.py

# Imports randrange from the random library
from random import randrange

# Randomly selects a number in between 1-6 and returns it
def roll():
    num = randrange(1,7)
    return num

#Start the main loop
def main():
    
    #initialize the following variables
    ones = 0
    twos = 0
    threes = 0
    total = 0
    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # For loop 20 times rolling red and green dice randomly and getting the total
    # Adding one to the position of the total to indicate how many times that total was rolled
    # Print the counter
    for i in range (20):
        red = roll()
        green = roll()
        total = red + green
        counter[total] = counter[r] + 1
    print()
    print(counter)
    print()
        
    # Print a table of text indicating the ammount of each total possible and how many times that
    # total was rolled in our test
    print("there are",counter[0],"zeroes when the dice is rolled 30 times")
    print()
    
    print("there are",counter[1],"ones when the dice is rolled 30 times")
    print()
    
    print("there are",counter[2],"two's when the dice is rolled 30 times")
    print()
    
    print("there are",counter[3],"threes when the dice is rolled 30 times")
    print()
    
    print("there are",counter[4],"fours when the dice is rolled 30 times")
    print()
    
    print("there are",counter[5],"fives when the dice is rolled 30 times")
    print()
    
    print("there are",counter[6],"six's when the dice is rolled 30 times")
    print()
    
    print("there are",counter[7],"sevens when the dice is rolled 30 times")
    print()
    
    print("there are",counter[8],"eights when the dice is rolled 30 times")
    print()
    
    print("there are",counter[9],"nines when the dice is rolled 30 times")
    print()
    
    print("there are",counter[10],"tens when the dice is rolled 30 times")
    print()
    
    print("there are",counter[11],"elevens when the dice is rolled 30 times")
    print()
    
    print("there are",counter[12],"twelves when the dice is rolled 30 times")
    print()  
# End the main loop
main()
