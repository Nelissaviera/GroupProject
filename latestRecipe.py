# Group Project
# Class: COP147C - Professor: E Salcedo
# School: Miami Dade College
# Authors: Nelissa Viera / Michelle Ruiz / Henry Fandino
# Last Correction: April 24th - 2022


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

def ingredients_recipe(recipe):

    if recipe == 1:

        quantity = int(input("How many loaves of bread they would like to bake: "))
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
        readFile(0, 11)

    elif recipe == 2:
        quantity = int(input("How many loaves of bread they would like to bake: "))
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
        readFile(11, 19)

    elif recipe == 3:
        quantity = int(input("How many loaves of bread they would like to bake: "))
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
        readFile(19, 28)

    elif recipe == 4:
        quantity = int(input("How many loaves of bread they would like to bake: "))
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

    elif recipe == 5:
        quantity = int(input("How many loaves of bread they would like to bake: "))
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

    elif recipe == 6:
        quantity = int(input("How many loaves of bread they would like to bake: "))
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

    elif recipe == 7:
        quantity = int(input("How many loaves of bread they would like to bake: "))
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

    else:
        print("wrong option, try again")

# menu - function
# This is the main menu function, user is given the option to enter '1' to run the recipe program or any other key
# to exit.
# if user chooses '1' then the next option is to choose a bread recipe, this option (number) will be then
# passed to the recipeOption function

def menu():
    option = int(input("Press 1 to select your favorite bread recipe. \nOr press any key to finish and exit. \nOption: "))
    if(option == 1):
        recipeOption = int(input("Select your favorite bread\n1.Multigrain Bread\n 2.Baguette\n 3.Bagel \n 4.Banana Bread \n 5.Whole Wheat \n 6.Pita Bread \n 7.Corn Bread \n Option:"))
        return recipeOption
    else:
        print("Thanks for using our recipe program")
        exit()

## here we run the cript ##
# We call the function ingredients_recipe and menu
# the ingredients_recipe function will have as an argument the number returned by the menu function.

ingredients_recipe(menu())

print('Would you like to try another recipe? Y/N')
runMenuAgain = input()

while runMenuAgain.lower() == 'y':
    ingredients_recipe(menu())
    print('Would you like to try another recipe? Y/N')
    runMenuAgain = input()
