from random import randint
from art import start, end


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check the answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return None


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Function to begin the game
def game():
    print(start)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Choosing a number between 1 and 100.
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0

    # Repeat the guessing functionality if they get it wrong.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")


while input("Do you want to play the game of Number Guessing? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    game()

print("\n" * 20)
print(end)
print("Hope you had fun. See you next time!")
