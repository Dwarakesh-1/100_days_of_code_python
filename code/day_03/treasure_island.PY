print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Do you want to go right or left? ").lower()

if direction == 'left':
    # game will continue
    print("You took left")
    # next choice to survive the game
    option = input("Do you want to swim or wait? ").lower()
    if option == 'wait':
        # game will continue
        print("You choose to wait")
        door = input("Choose one door red or blue or yellow? ").lower()
        # next choice to survive the game
        if door == 'red':
            #wrong choice that ends the game
            print("Burned by fire. Game Over.")
        elif door == 'yellow':
            # correct choice to win the game
            print("You Win!")
        elif door == 'blue':
            # wrong choice that ends the game
            print("Eaten by beasts. Game Over.")
        else:
            # game will end
            print("Game Over.")
    else:
        # game will end
        print("Attacked by trout. Game Over.")
else:
    # game will end
    print("Fall into a hole. Game Over.")
