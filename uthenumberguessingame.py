# Number Guessing Game Objectives:
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_approax(make_guess):
    if make_guess > answer:
        print("Too high!")
    else:
        print("Too Less!")


def check_guess():
    if mode == 'easy':
        guess = 10
    elif mode == 'hard':
        guess = 5
    print(f"You have {guess} attempts remaining to guess the number.")
    for i in range(guess):
        make_guess = int(input("Make a guess: "))
        if answer == make_guess:
            print(f"You got it! The answer was {answer}.")
            break
        elif answer != make_guess:
            guess -= 1
            check_approax(make_guess)
            print("Guess again!")
            print(f"You have {guess} attempts remaining to guess the number.")
            if guess == 0:
                print("You run out of guesses!. You lose!")


# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
import uart

print(uart.number_guess)
print("Welcome to the number guessing name! ")
print("I'm thinking of a number between 1 to 100")
mode = input("Choose a difficulty.Type 'easy' or 'hard': ")

# Allow the player to submit a guess for a number between 1 and 100.
answer = randint(1, 100)
print(f"The correct answer is {answer}")

check_guess()
