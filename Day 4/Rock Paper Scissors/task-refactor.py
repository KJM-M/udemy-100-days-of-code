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


image = [rock, paper, scissors]
player_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
computer_chose = random.randint(0,2)

if player_chose >= 3 or player_chose < 0:
    print("Invalid Number. You lose")
    exit()

print(image[player_chose])
print("Computer chose:")
print(image[computer_chose])

if player_chose == computer_chose:
    print("Draw")
elif player_chose == 0 and computer_chose == 2:
    print("You Win")
elif player_chose == 1 and computer_chose == 0:
    print("You Win")
elif player_chose == 2 and computer_chose == 1:
    print("You Win")
else:
    print("You Lose")





