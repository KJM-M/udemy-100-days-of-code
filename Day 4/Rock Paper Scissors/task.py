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


rps_choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(rps_choices[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{rps_choices[computer_choice]}")

if rps_choices[player_choice] == rock and rps_choices[computer_choice] == scissors:
    print("You win!")
elif rps_choices[player_choice] == rock and rps_choices[computer_choice] == paper:
    print("You lose!")

if rps_choices[player_choice] == paper and rps_choices[computer_choice] == rock:
    print("You win!")
elif rps_choices[player_choice] == paper and rps_choices[computer_choice] == scissors:
    print("You lose!")

if rps_choices[player_choice] == scissors and rps_choices[computer_choice] == paper:
    print("You win!")
elif rps_choices[player_choice] == scissors and rps_choices[computer_choice] == rock:
    print("You lose!")


if rps_choices[player_choice] == rps_choices[computer_choice]:
    print("Draw!")

if player_choice >= 3 or player_choice < 0:
    print("You lose!")
