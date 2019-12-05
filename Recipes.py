def getRecipe2():
    total=1
    weight=0
    grams=0
    name=input("Enter the name of the ingredient:")
    grams=int(input("Enter the weight of the ingredient in grams:"))
    weight=weight+grams
    moreData='yes'
    while moreData=='yes':
        x=input("Enter the name of the ingredient:")
        y=int(input("Enter the weight of the ingredient in grams:"))
        total=total+1
        weight=weight+grams
        moreData=input("Do you have more ingredients:(yes or no?)")
    print("the total amount of ingredients is:",total)
    print("The total weight of the ingredients in grams is:",(weight))
getRecipe2()
