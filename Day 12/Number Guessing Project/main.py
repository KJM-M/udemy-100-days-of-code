from random import randint
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

computer_number = randint(1, 100)
game_live = False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
    game_live = True
elif difficulty == "hard":
    lives = 5
    game_live = True
else:
    print("Typo. Better luck next time!")
    game_live = False

while game_live:
    print(f"You have {lives} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if computer_number == guess:
        print("You got it!")
        break
    elif guess < computer_number:
        print("Too low.\nGuess again.")
    elif guess > computer_number:
        print("Too high.\nGuess again.")

    lives -= 1

    if lives == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        break
