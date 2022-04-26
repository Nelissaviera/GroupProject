# -*- coding: utf-8 -*-
# Group Project
# Class: COP147C - Professor: E Salcedo
# School: Miami Dade College
# Authors: Nelissa Viera / Michelle Ruiz / Henry Fandino
# Last Correction: April 25th - 2022


# FUNCTIONS

# readFile - function
# The readFile function reads the respective lines from the Recipe.txt file
# The Recipe.txt file most be located in the same directory as this file.
# This functions takes 2 integers, these are the lines to be pulled from the Recipe.txt and to be printed out.

def readFile(a, b):
    with open('Recipes.txt') as f:
        mylist = f.read().splitlines()
        for n in range(a, b):
            print(mylist[n])
 
# ingredients_recipe -function
# This function takes one argument, this is an integer and it indicates the bread recipe chosen by the user
# if the user chose 3, for example, then this function will print out the respective ingredient list and instructions
# for that specific bread recipe.
            
def ingredients_recipe(recipe, quantity):
    
    if(recipe == 1):
        print()
        print(f'Bread recipe for Multigrain for {quantity} is:')
        TotalFlour = 100.00
        RedWheat = 120.00
        WhiteWheat = 25.00
        Rye = 15.00
        BreadFlour = 300.00
        Salt = 10.00
        Water = 275.00

        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(0, 11)

    elif(recipe == 2):
        print()
        print(f'Bread recipe for Baguette for {quantity} is:')
        TotalFlour = 50.00
        RedWheat = 125.00
        WhiteWheat = 25.00
        Rye = 5.00
        BreadFlour = 180.00
        Salt = 10.00
        Water = 250.00

        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(11, 19)
        
    elif(recipe == 3):
        print()
        print(f'Bread recipe for Bagel for {quantity} is:')
        TotalFlour = 75.00
        RedWheat = 80.00
        WhiteWheat = 20.00
        Rye = 8.00
        BreadFlour = 190.00
        Salt = 8.00
        Water = 250.00

        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(19, 28)
         
    elif(recipe == 4):
        print()
        print(f'Bread recipe for Banana bread for {quantity} is:')
        TotalFlour = 40.00
        RedWheat = 125.00
        WhiteWheat = 25.00
        Rye = 10.00
        BreadFlour = 250.00
        Salt = 5.00
        Water = 225.00
 
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(28, 37)
        
    elif(recipe == 5):
        print()
        print(f'Bread recipe for Whole Wheat for {quantity} is:')
        TotalFlour = 75.00
        RedWheat = 111.00
        WhiteWheat = 22.00
        Rye = 8.00
        BreadFlour = 120.00
        Salt = 7.00
        Water = 225.00

        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(38, 46)

        
    elif(recipe == 6):
        print()
        print(f'Bread recipe for Pita Bread for {quantity} is:')
        TotalFlour = 90.00
        RedWheat = 125.00
        WhiteWheat = 15.00
        Rye = 1.00
        BreadFlour = 20.00
        Salt = 10.00
        Water = 175.00

        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(46, 53)

    else:
        print()
        print(f'Bread recipe for Corn Bread for {quantity} is:')
        TotalFlour = 80.00
        RedWheat = 120.00
        WhiteWheat = 10.00
        Rye = 15.00
        BreadFlour = 200.00
        Salt = 4.00
        Water = 75.00

        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
        print()
        readFile(53, 60)

# mainMenu - function
# This is the main menu function, user is given the option to enter '1' to run the recipe program or any other key
# to exit.
# if user chooses '1' then the next option is to choose a bread recipe, this option (number) will be then
# passed to the recipeOption function
 
def mainMenu():
    recipeOption = input("Select your favorite bread\n 1.Multigrain Bread\n 2.Baguette\n 3.Bagel \n 4.Banana Bread \n 5.Whole Wheat \n 6.Pita Bread \n 7.Corn Bread \n 8.Exit\nOption: ")
               
    while(not recipeOption.isnumeric()):
        print("\033[31m The value entered must be number \033[0m")       
        recipeOption = input("Select your favorite bread\n 1.Multigrain Bread\n 2.Baguette\n 3.Bagel \n 4.Banana Bread \n 5.Whole Wheat \n 6.Pita Bread \n 7.Corn Bread \n 8.Exit\n Option: ") 
              
    #Convert values to int  
    if(recipeOption.isnumeric()):
        recipeOption = int(recipeOption)
        if(recipeOption != 8 and recipeOption <8):
            quantity = input("How many loaves of bread they would like to bake: ")
            while(not quantity.isnumeric()):
                print("\033[31m The value entered must be number \033[0m")
                quantity = input("How many loaves of bread they would like to bake: ")
        
            quantity = int(quantity)
            
        if(recipeOption ==1 or recipeOption ==2 or recipeOption ==3 or recipeOption ==4 or recipeOption ==5 or recipeOption ==6 or 
           recipeOption ==7):
            return recipeOption,quantity
        else:
           return recipeOption 

    else:
        print("\033[31m The values entered must be numbers \033[0m")
        SystemExit()
       
# Here we call the function ingredients_recipe and mainMenu
# the ingredients_recipe function will have as an argument the number returned by the menu function
# and in some cases the number of loaves.
print("**** Recipe Program ****")

option = 'y'
close_option = 0
while option.lower() =='y' and close_option == 0:
    #Call menu function
    menuRecipe = mainMenu()
    
    if(type(menuRecipe) is tuple):
        ingredients_recipe(menuRecipe[0], menuRecipe[1])
        option = input("\033[32m Do you want to select another recipe?\n Press Y to continue or another keyword to exit : \033[0m")
    else:
        if(menuRecipe == 8):
            close_option = option
            print("Thanks for use our recipe program")
            SystemExit()
            
        #Display error message when the option is not in the menu
        elif(menuRecipe != 1 or menuRecipe != 2 or menuRecipe != 3 or menuRecipe != 4 or menuRecipe != 5 or menuRecipe != 6 or menuRecipe != 7 or menuRecipe != 8):
            print("\033[31m Wrong choice. \033[0m")

     
if(option.lower() != 'y' or close_option== 8):
    print()
    print("Thanks for use our recipe program")
    SystemExit()