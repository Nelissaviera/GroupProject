# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:28:47 2022

@author: Nelissa Viera/ Michelle Ruiz / Henry F 
"""

#Funcions

#Function to display the recipe selected
def ingredients_recipe(recipe, quantity):
    
    if(recipe == 1):
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
        fileProcedure = open("Recipes.txt", "r")
        print(fileProcedure.readlines()[0:7])

    elif(recipe == 2):
        print(f' Bread recipe for Baguette for {quantity} is:')
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
        fileProcedure2 = open("Recipes.txt", "r")

        print(fileProcedure2.readlines()[0:7])
        
    elif(recipe == 3):
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
        fileProcedure3 = open("Recipes.txt", "r")
        print()
        print(fileProcedure3.readlines()[8:16])
         
                
    elif(recipe == 4):
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
        #Example to get doc lines
        #fileProcedure = open("Recipes.txt", "r")
        #i =0
        #for line in fileProcedure:
            
            #if(i <=7):
                #print(line)
                #i+=1
        #fileProcedure.close()
        
    elif(recipe == 5):
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
        fileProcedure4 = open("Recipes.txt", "r")
        print(fileProcedure4.readlines()[17:24])

        
    elif(recipe == 6):
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
        fileProcedure = open("Recipes.txt", "r")
        print(fileProcedure.readlines()[25:31])

    else:
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

        
 #Function to display the main menu   
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
       

print("  **** Recipe Program ****")

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
    print("Thanks for use our recipe program")
    SystemExit()
