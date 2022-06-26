"""
Program: Dice Throwing Game

Author: Olamide Adu

"""
# This code programs the Dice Throwing Game

# import from the random module in Python
import random
print("Welcome to the Dice throwing game")
print('--------------------------------------')
print()
# User enters how many marbles they want in their bag initially
bag_marbles = int(input("Enter how many marbles you have in your bag initially > "))
# User enters how many marbles they want to bet
no_marbles = int(input("Enter number of marbles you are going to bet > "))
# User must enter positive values greater than zero, otherwise user gets another chance to re-enter values
while (bag_marbles <= 0) or (no_marbles <= 0):
    print("Please enter a number; minimum = 1")
    bag_marbles = int(input("=> Enter how many marbles you have in your bag initially > "))
    no_marbles = int(input("=> Enter number of marbles you are going to bet > "))
# User must enter a lucky number ranging from 2 to 12, otherwise user gets another chance to re-enter their lucky number
lucky_number = int(input("Enter your lucky number (2-12) > "))
while (lucky_number < 2 or lucky_number > 12):
    print("Your lucky number must be a number from 2 to 12.")
    lucky_number = int(input("=> Please enter your lucky number (2-12) > "))

print()
# If there are not enough marbles in the bag to bet, the game automatically ends
if bag_marbles < no_marbles:
    print("Not enough marbles to bet")
    print("Game over")
else:
    # Game starts, with the number of rounds initialized to zero 
    no_rounds = 0
    print("--Throwing dice. You bet", no_marbles, "marble(s) on number", lucky_number)
    remaining_marbles = bag_marbles - no_marbles
    # The two dice are thrown; the program does this by generating random numbers for both dice, ranging from 1 to 6
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    # The sum of the faces of the dice are added
    dice_total = die1 + die2
    no_1 = "-----"
    no_2 = "|   |"
    no_3 = "| 0 |"
    no_4 = "|0  |"
    no_5 = "|  0|"
    no_6 = "|0 0|"
    # The faces of the dice are represented visually
    if (die1 == 1):
        if (die2 == 1):
            print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_2+"\n"+no_3+"\t"+no_3+"\n"+no_2+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 2):
            print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_4+"\n"+no_3+"\t"+no_2+"\n"+no_2+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 3):
            print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_4+"\n"+no_3+"\t"+no_3+"\n"+no_2+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 4):
            print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_6+"\n"+no_3+"\t"+no_2+"\n"+no_2+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 5):
            print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_6+"\n"+no_3+"\t"+no_3+"\n"+no_2+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 6):
            print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_6+"\n"+no_3+"\t"+no_6+"\n"+no_2+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
    elif (die1 == 2):
        if (die2 == 1):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_2+"\n"+no_2+"\t"+no_3+"\n"+no_5+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 2):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_2+"\t"+no_2+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 3):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_2+"\t"+no_3+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 4):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_2+"\t"+no_2+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()  
        elif (die2 == 5):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_2+"\t"+no_3+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 6):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_2+"\t"+no_6+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
    elif (die1 == 3):
        if (die2 == 1):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_2+"\n"+no_3+"\t"+no_3+"\n"+no_5+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
            print()        
        elif (die2 == 2):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_3+"\t"+no_2+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 3):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_3+"\t"+no_3+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 4):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_3+"\t"+no_2+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()  
        elif (die2 == 5):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_3+"\t"+no_3+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 6):
            print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_3+"\t"+no_6+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
    elif (die1 == 4):
        if (die2 == 1):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_2+"\n"+no_2+"\t"+no_3+"\n"+no_6+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 2):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_2+"\t"+no_2+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 3):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_2+"\t"+no_3+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 4):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_2+"\t"+no_2+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()  
        elif (die2 == 5):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_2+"\t"+no_3+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 6):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_2+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
    elif (die1 == 5):
        if (die2 == 1):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_2+"\n"+no_3+"\t"+no_3+"\n"+no_6+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 2):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_3+"\t"+no_2+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 3):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_3+"\t"+no_3+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 4):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_3+"\t"+no_2+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()  
        elif (die2 == 5):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_3+"\t"+no_3+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 6):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_3+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
    elif (die1 == 6):    
        if (die2 == 1):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_2+"\n"+no_6+"\t"+no_3+"\n"+no_6+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 2):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_6+"\t"+no_2+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 3):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_6+"\t"+no_3+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 4):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_2+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()  
        elif (die2 == 5):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_3+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()
        elif (die2 == 6):
            print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
            print()   
    
    print("--Dice:", die1, "and", die2)
    print("--Lucky number:", dice_total)
        
    # If the sum of the faces of the dice happens to be the user's lucky number,
    # then they win 10 times the marbles they bet and the marbles
    # that they bet are returned to the user.
    # Otherwise, the user loses the marbles they bet.
    if (dice_total == lucky_number):
        marbles_won = no_marbles + (no_marbles * 10)
        total_marbles = remaining_marbles + marbles_won
        print("--You won",marbles_won, "marble(s) and have a total of", total_marbles, "marble(s) in your bag.")
        no_rounds += 1
    else:
        total_marbles = remaining_marbles
        print("--You won 0 marble(s) and have a total of", total_marbles, "marble(s) in your bag.")
        no_rounds += 1
        
    def getVal(minval,maxval):
        select_option = int(input("option >"))
        while ((select_option < minval) or (select_option > maxval)):
            select_option = int(input("Re-select option ("+str(minval)+".."+str(maxval)+"): "))
        return select_option
    
    print()
    choice=0
    # The user selects what option they would like in the game
    while (choice !=5):
        print("Select option:")
        print("1. Change my bet")
        print("2. Change my lucky number")
        print("3. Count my bag of marbles")
        print("4. Play for marbles!")
        print("5. Take my bag of marbles and run!")    
        choice = getVal(1,5)
        print()
        # User can select option 1 to change the number of marbles they want to bet
        if (choice == 1):
            no_marbles = int(input("Enter number of marbles you are going to bet > "))
            print()
        # Or they can select option 2 to change their lucky number, still ranging from 2 to 12
        elif (choice == 2):
            lucky_number = int(input("Enter your lucky number (2-12) > "))
            while (lucky_number < 2 or lucky_number > 12):
                print("Your lucky number must be a number from 2 to 12.")
                lucky_number = int(input("=> Please enter your lucky number (2-12) > "))
            print()
        # Or user can select option 3 to find out the number of marbles in their bag
        elif (choice == 3):
            print("You have", total_marbles, "marbles in your bag.")
            print()
        # User can choose option 4 to play another round, if there are enough marbles in the bag to bet in the game
        elif (choice == 4):
            if (no_marbles > total_marbles):
                print("--Not enough marbles to play for marbles.")
                no_rounds += 1
                print()
            else:
                print("--Throwing dice. You bet", no_marbles, "marble(s) on number", lucky_number)
                total_marbles = total_marbles - no_marbles
                die1 = random.randint(1,6)
                die2 = random.randint(1,6)
                dice_total = die1 + die2
                if (die1 == 1):
                    if (die2 == 1):
                        print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_2+"\n"+no_3+"\t"+no_3+"\n"+no_2+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 2):
                        print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_4+"\n"+no_3+"\t"+no_2+"\n"+no_2+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 3):
                        print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_4+"\n"+no_3+"\t"+no_3+"\n"+no_2+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 4):
                        print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_6+"\n"+no_3+"\t"+no_2+"\n"+no_2+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 5):
                        print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_6+"\n"+no_3+"\t"+no_3+"\n"+no_2+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 6):
                        print(no_1+"\t"+no_1+"\n"+no_2+"\t"+no_6+"\n"+no_3+"\t"+no_6+"\n"+no_2+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                elif (die1 == 2):
                    if (die2 == 1):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_2+"\n"+no_2+"\t"+no_3+"\n"+no_5+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 2):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_2+"\t"+no_2+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 3):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_2+"\t"+no_3+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 4):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_2+"\t"+no_2+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()  
                    elif (die2 == 5):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_2+"\t"+no_3+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 6):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_2+"\t"+no_6+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                elif (die1 == 3):
                    if (die2 == 1):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_2+"\n"+no_3+"\t"+no_3+"\n"+no_5+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
                        print()        
                    elif (die2 == 2):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_3+"\t"+no_2+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 3):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_4+"\n"+no_3+"\t"+no_3+"\n"+no_5+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 4):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_3+"\t"+no_2+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()  
                    elif (die2 == 5):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_3+"\t"+no_3+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 6):
                        print(no_1+"\t"+no_1+"\n"+no_4+"\t"+no_6+"\n"+no_3+"\t"+no_6+"\n"+no_5+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                elif (die1 == 4):
                    if (die2 == 1):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_2+"\n"+no_2+"\t"+no_3+"\n"+no_6+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 2):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_2+"\t"+no_2+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 3):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_2+"\t"+no_3+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 4):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_2+"\t"+no_2+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()  
                    elif (die2 == 5):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_2+"\t"+no_3+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 6):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_2+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                elif (die1 == 5):
                    if (die2 == 1):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_2+"\n"+no_3+"\t"+no_3+"\n"+no_6+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 2):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_3+"\t"+no_2+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 3):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_3+"\t"+no_3+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 4):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_3+"\t"+no_2+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()  
                    elif (die2 == 5):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_3+"\t"+no_3+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 6):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_3+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                elif (die1 == 6):    
                    if (die2 == 1):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_2+"\n"+no_6+"\t"+no_3+"\n"+no_6+"\t"+no_2+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 2):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_6+"\t"+no_2+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 3):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_4+"\n"+no_6+"\t"+no_3+"\n"+no_6+"\t"+no_5+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 4):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_2+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()  
                    elif (die2 == 5):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_3+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()
                    elif (die2 == 6):
                        print(no_1+"\t"+no_1+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_6+"\t"+no_6+"\n"+no_1+"\t"+no_1+"\n")
                        print()               
                
                print("--Dice:", die1, "and", die2)
                print("--Lucky number:", dice_total)
                if (dice_total == lucky_number):
                    marbles_won = no_marbles + (no_marbles * 10)
                    total_marbles = total_marbles + marbles_won
                    print("--You won",marbles_won, "marble(s) and have a total of", total_marbles, "marble(s) in your bag.")
                else:
                    print("--You won 0 marble(s) and have a total of", total_marbles, "marble(s) in your bag.")
                no_rounds += 1
                print()
    # If user selects option 5, they end the game and the number of rounds played is displayed
    # along with the number of marbles in the bag and the initial number of marbles in the bag
    if (choice == 5):
        print("Thanks for playing.")
        print("After", no_rounds, "rounds you have", total_marbles, "marble(s) in your bag.")
        print("You started with", bag_marbles, "marble(s) in your bag.")
            
        
        




