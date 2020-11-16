#Anuj Gupta
#lab section m5
#Lab 16
#SimplisticCardDealer.py
#simulate dealing a hand of cards. (may have repeats)

#import randrange from random library
from random import randrange

#return a random rank for a card
#returns a random character from "A23456789TJQK" as the rank
def chooseRank():
    ranks="A23456789TJQK"
    r=randrange(13)
    return ranks[r]
   
#return a random suit for a card
#return a random chaacter from "CDHS" as the suit
def chooseSuit():
    suits="CDHS"
    r=randrange(4)
    return suits[r]
    
#creates a hand of 7 cards.
def main():     
    #initialize hand as an empty list
    hand=[]
    # for loop to create the random 7 cards and append them to the hand
    for i in range(7):       
        rank=chooseRank()
        suit=chooseSuit()
        hand.append(rank+suit)
    print("The hand after 7 cards are chosen at random is as follows"+"\n",hand)
    #sort the hand 
    hand.sort()
main()
