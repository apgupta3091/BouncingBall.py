#Anuj Gupta
#lab section m5
#Lab 16
#SimplisticCardDealer.py

#simulate dealing a hand of cards. (may have repeats)

#import library so we can use randrange
from random import randrange


#return a random rank for a card, that is
#returns a random character from "A23456789TJQK"
#Notice the use of T for ten
def chooseRank():
    ranks="A23456789TJQK"
    r=randrange(13)
    return ranks[r]
    


#return a random suit for a card, that is
#return a random chaacter from "CDHS"
def chooseSuit():
    suits="CDHS"
    r=randrange(4)
    return suits[r]
    

#create a hand of 7 cards.

def main():
        
    #initialize hand as an empty list
    hand=[]
    
    #repeat 7 times, once for each card
    for i in range(7):
            
    #pick a random rank and suit
        rank=chooseRank()
        suit=chooseSuit()

    #append a string with that rank and suit
    #to the list hand
        hand.append(rank+suit)

    #print the hand
    print("The hand after 7 cards are chosen at random is as follows"+"\n",hand)

    #sort the hand and print it again
    hand.sort()

main()
