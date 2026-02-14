import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 8

print(logo)

chosen_word = random.choice(word_list)

placeholder = len(chosen_word) * "_"
print("\nWord to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"**************************** {lives}/8 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You've already guessed this letter: " + guess.upper())

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess.upper()}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"Correct words was: {chosen_word.upper()}")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
