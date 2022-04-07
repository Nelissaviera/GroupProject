# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:28:47 2022

@author: 
"""
def ingredients_recipe(recipe, quantity):
    if(recipe == 1):
        print(f' Bread recipe for Multigrain for {quantity} is:')
    elif(recipe == 2):
        print(f' Bread recipe for Baguette for {quantity} is:')
    elif(recipe == 3):
        print(f' Bread recipe for Bagel for {quantity} is:')
    elif(recipe == 3):
        print(f' Bread recipe for Banana bread for {quantity} is:')
    elif(recipe == 3):
        print(f' Bread recipe for Whole Wheat for {quantity} is:')
    elif(recipe == 3):
        print(f' Bread recipe for Pita Bread for {quantity} is:')
    else:
        print(f' Bread recipe for Corn Bread for {quantity} is:')
    
def menu():
    option = int(input("1. Select a favorite bread recipe \n2. Exit \nOption: "))
    if(option == 1):
        recipeOption = int(input("Select your favorite bread\n1.Multigrain Bread\n 2.Baguette\n 3.Bagel \n 4.Banana Bread \n 5.Whole Wheat \n 6.Pita Bread \n 7.Corn Bread \n Option:"))
        quantity = int(input("How many loaves of bread they would like to bake: "))
        return recipeOption,quantity
    else:
        print("Thanks for use our recipe program")
        SystemExit()

print("  **** Recipe Program ****")
#Call menu function

recipeParameters = menu()
ingredients_recipe(recipeParameters[0], recipeParameters[1])

option = input("Do you want to select another recipe? Y or N : ")
while option =='Y' or option =='y':
    menuRecipe = menu()
    ingredients_recipe(recipeParameters[0], recipeParameters[1])
