import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
user_choice = game_list[user]
print(f"You chose: \n {user_choice}")
computer_choice = random.choice(game_list)
print(f"Computer chose: \n {computer_choice}")

if user == 0:
    if computer_choice == game_list[0]:
        print("Draw!")
    elif computer_choice == game_list[1]:
        print("You lose!")
    else:
        print("You win!")
elif user == 1:
    if computer_choice == game_list[0]:
        print("You win!")
    elif computer_choice == game_list[1]:
        print("Draw!")
    else:
        print("You lose!")
elif user == 2:
    if computer_choice == game_list[0]:
        print("You lose!")
    elif computer_choice == game_list[1]:
        print("You win!")
    else:
        print("Draw!")
else:
    print("You typed an invalid number. You lose!")
