# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:28:47 2022

@author: Nelissa Viera/ Michelle Ruiz / Henry F 
"""

#Constant section

#Funcions

#Function to display the recipe selected
def ingredients_recipe(recipe, quantity):
    if(recipe == 1):
        print(f' Bread recipe for Multigrain for {quantity} is:')
    elif(recipe == 2):
        print(f' Bread recipe for Baguette for {quantity} is:')
    elif(recipe == 3):
        print(f' Bread recipe for Bagel for {quantity} is:')
    elif(recipe == 4):
        print(f' Bread recipe for Banana bread for {quantity} is:')
    elif(recipe == 5):
        print(f' Bread recipe for Whole Wheat for {quantity} is:')
    elif(recipe == 6):
        print(f' Bread recipe for Pita Bread for {quantity} is:')
    else:
        print(f' Bread recipe for Corn Bread for {quantity} is:')
        
 #Function to display the main menu   
def menu():
    option = int(input("1. Select a favorite bread recipe \n2. Exit \nOption: "))
    if(option == 1):
        recipeOption = int(input("Select your favorite bread\n1.Multigrain Bread\n 2.Baguette\n 3.Bagel \n 4.Banana Bread \n 5.Whole Wheat \n 6.Pita Bread \n 7.Corn Bread \n Option:"))
        quantity = int(input("How many loaves of bread they would like to bake: "))
        return recipeOption,quantity
    else:
        return option
        SystemExit()


print("  **** Recipe Program ****")

option = 'Y'
option_main_menu = 0

while (option =='Y' or option =='y') and option_main_menu ==0:
    #Call menu function
    menuRecipe = menu()
    
    #Display recipe ingredients when the option is 1 otherwise exit the program
    
    if(type(menuRecipe) is tuple):
        ingredients_recipe(menuRecipe[0], menuRecipe[1])
        option = input("Do you want to select another recipe? Y or N : ")
    else:
        option_main_menu = menuRecipe
        #Display error message when the option is not in the menu
        if(option_main_menu != 1 or  option_main_menu != 2):
            print("Invalid option. ")
        
if(option !='Y' or option !='y'):
    print("Thanks for use our recipe program")
    SystemExit()
