
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
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    elif(recipeOption == 2):
        TotalFlour = 60.00
        RedWheat = 100.00
        WhiteWheat = 20.00
        Rye = 5.00
        BreadFlour = 200.00
        Salt = 11.00
        Water = 275.00
        print(f' Bread recipe for Baguette for {quantity} is:')
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour:', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    elif(recipeOption == 3):
        TotalFlour = 60.00
        RedWheat = 100.00
        WhiteWheat = 20.00
        Rye = 5.00
        BreadFlour = 200.00
        Salt = 11.00
        Water = 275.00
        print(f' Bread recipe for Bagel for {quantity} is:')
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour:', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    elif(recipeOption == 4):
        TotalFlour = 60.00
        RedWheat = 100.00
        WhiteWheat = 20.00
        Rye = 5.00
        BreadFlour = 200.00
        Salt = 11.00
        Water = 275.00
        print(f' Bread recipe for Banana bread for {quantity} is:')
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour:', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    elif(recipeOption == 5):
        TotalFlour = 60.00
        RedWheat = 100.00
        WhiteWheat = 20.00
        Rye = 5.00
        BreadFlour = 200.00
        Salt = 11.00
        Water = 275.00
        print(f' Bread recipe for Whole Wheat for {quantity} is:')
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour:', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    elif(recipeOption == 6):
        TotalFlour = 60.00
        RedWheat = 100.00
        WhiteWheat = 20.00
        Rye = 5.00
        BreadFlour = 200.00
        Salt = 11.00
        Water = 275.00
        print(f' Bread recipe for Pita Bread for {quantity} is:')
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour:', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    elif(recipeOption == 7):
        TotalFlour = 60.00
        RedWheat = 100.00
        WhiteWheat = 20.00
        Rye = 5.00
        BreadFlour = 200.00
        Salt = 11.00
        Water = 275.00
        print(f' Bread recipe for Corn Bread for {quantity} is:')
        print('Total Flour:', TotalFlour * quantity)
        print('RedWheat:', RedWheat * quantity)
        print('WhiteWheat:', WhiteWheat * quantity)
        print('Rye:', Rye * quantity)
        print('Bread Flour:', BreadFlour * quantity)
        print('Salt:', Salt * quantity)
        print('Water:', Water * quantity)
    else:
        print("Wrong choice, try again")

mainMenu()

print('Would you like to try another recipe? Y/N')
runMenuAgain = input()

while runMenuAgain.lower() == 'y':
    mainMenu()
    print('Would you like to try another recipe? Y/N')
    runMenuAgain = input()

