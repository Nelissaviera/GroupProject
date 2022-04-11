
def mainMenu():
    print("Select your favorite bread\n1.Multigrain Bread\n 2.Baguette\n 3.Bagel \n 4.Banana Bread \n 5.Whole Wheat \n 6.Pita Bread \n 7.Corn Bread \n Option:")
    recipeOption = int(input())

    print("How many loaves of bread they would like to bake? ")
    quantity = int(input())

    if(recipeOption == 1):
        TotalFlour = 100.00
        RedWheat = 120.00
        WhiteWheat = 25.00
        Rye = 15.00
        BreadFlour = 300.00
        Salt = 10.00
        Water = 275.00
        print(f' Bread recipe for Multigrain for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    elif(recipeOption == 2):
        TotalFlour = 50.00
        RedWheat = 125.00
        WhiteWheat = 25.00
        Rye = 5.00
        BreadFlour = 180.00
        Salt = 10.00
        Water = 250.00
        print(f' Bread recipe for Baguette for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    elif(recipeOption == 3):
        TotalFlour = 75.00
        RedWheat = 80.00
        WhiteWheat = 20.00
        Rye = 8.00
        BreadFlour = 190.00
        Salt = 8.00
        Water = 250.00
        print(f' Bread recipe for Bagel for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    elif(recipeOption == 4):
        TotalFlour = 40.00
        RedWheat = 125.00
        WhiteWheat = 25.00
        Rye = 10.00
        BreadFlour = 250.00
        Salt = 5.00
        Water = 225.00
        print(f' Bread recipe for Banana bread for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    elif(recipeOption == 5):
        TotalFlour = 75.00
        RedWheat = 111.00
        WhiteWheat = 22.00
        Rye = 8.00
        BreadFlour = 120.00
        Salt = 7.00
        Water = 225.00
        print(f' Bread recipe for Whole Wheat for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    elif(recipeOption == 6):
        TotalFlour = 90.00
        RedWheat = 125.00
        WhiteWheat = 15.00
        Rye = 1.00
        BreadFlour = 20.00
        Salt = 10.00
        Water = 175.00
        print(f' Bread recipe for Pita Bread for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    elif(recipeOption == 7):
        TotalFlour = 80.00
        RedWheat = 120.00
        WhiteWheat = 10.00
        Rye = 15.00
        BreadFlour = 200.00
        Salt = 4.00
        Water = 75.00
        print(f' Bread recipe for Corn Bread for {quantity} is:')
        print(f'Total Flour: {TotalFlour * quantity}g.')
        print(f'RedWheat: {RedWheat * quantity}g.')
        print(f'WhiteWheat: {WhiteWheat * quantity}g.')
        print(f'Rye: {Rye * quantity}g.')
        print(f'Bread Flour {BreadFlour * quantity}g.')
        print(f'Salt: {Salt * quantity}g.')
        print(f'Water: {Water * quantity}ml.')
    else:
        print("Wrong choice, try again")

mainMenu()

print('Would you like to try another recipe? Y/N')
runMenuAgain = input()

while runMenuAgain.lower() == 'y':
    mainMenu()
    print('Would you like to try another recipe? Y/N')
    runMenuAgain = input()

