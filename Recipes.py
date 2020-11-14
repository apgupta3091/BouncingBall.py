#Function for getting/creating the recipe created by a user
def getRecipe2():
    total=1
    weight=0
    grams=0
    name=input("Enter the name of the ingredient:")
    grams=int(input("Enter the weight of the ingredient in grams:"))
    weight=weight+grams
    moreData='yes'
    #While loop for if there is more data/ingredients in the recipe
    while moreData=='yes':
        x=input("Enter the name of the ingredient:")
        y=int(input("Enter the weight of the ingredient in grams:"))
        total=total+1
        weight=weight+grams
        # If user enters 'yes' then while loop continues, if enters 'no' then loop ends
        moreData=input("Do you have more ingredients:(yes or no?)")
    print("the total amount of ingredients is:",total)
    print("The total weight of the ingredients in grams is:",(weight))
getRecipe2()
