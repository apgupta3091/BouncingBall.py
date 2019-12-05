#Anuj Gupta
#lab section m5
#Lab 16
#DiceCounter.py
def main():
    ones=0
    twos=0
    threes=0
    r=0
    counter=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (20):
        red= roll()
        green=roll()
        r=red+green
        print(r, end=" ")
        counter[r]=counter[r]+1
    print()
    print(counter)
        
    print()
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
    
    for i in range(len(counter)):
        
         
        print(i,"\t",counter[i])
          
def roll():
    from random import randrange
    num=randrange(1,7)
    return num

main()
