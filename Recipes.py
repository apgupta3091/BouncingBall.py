#Function for getting/creating the recipe created by a user
def getRecipe2():
    
    #Initialize variables in the function
    total=1
    weight=0
    grams=0
    
    # Get the user input for the name/weight of their items and add grams to the weight variable
    name=input("Enter the name of the ingredient:")
    grams=int(input("Enter the weight of the ingredient in grams:"))
    weight= weight + grams
    
    #initialize moreData var
    moreData = 'yes'
    
    #While loop for if there is more data/ingredients in the recipe to repeat the earlier processes
    while moreData=='yes':
        x=input("Enter the name of the ingredient:")
        y=int(input("Enter the weight of the ingredient in grams:"))
        total = total+1
        weight = weight + grams
        
        # If user enters 'yes' then while loop continues, if enters 'no' then loop ends
        moreData=input("Do you have more ingredients:(yes or no?)")
        
    print("the total amount of ingredients is:",total)
    print("The total weight of the ingredients in grams is:",(weight))

#calls the function
getRecipe2()
