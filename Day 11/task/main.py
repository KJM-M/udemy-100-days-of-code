import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



player_hand = []
computer_hand = []


def starting_cards():
    for i in range(2):
        card = random.choice(cards)
        player_hand.append(card)
    for i in range(2):
        card = random.choice(cards)
        computer_hand.append(card)

def player_hit():
    for i in range(1):
        card = random.choice(cards)
        player_hand.append(card)

def computer_hit():
    for i in range(1):
        card = random.choice(cards)
        computer_hand.append(card)

def print_player_stats():
    print(f"Your cards: {player_hand}, your current hand: {player_score}")

def print_computer_stats():
    print(f"Computer cards: {computer_hand}, computer current hand: {computer_score}")

def print_both_stats():
    print(f"Your cards: {player_hand}, your current hand: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")

def new_game():
    global game_live
    game_live = False
    start_game_input = input("--------------------\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("--------------------")
    if start_game_input.lower() == "y":
        player_hand.clear()
        computer_hand.clear()
        game_live = True

    elif start_game_input.lower() == "n":
        exit()


computer_turn = False
new_game()

while game_live:
        starting_cards()
        player_score = sum(player_hand)
        computer_score = sum(computer_hand)
        print_both_stats()
        player_turn = True

        while player_turn:
            take_more = input("type 'y' to get another card, type 'n' to pass: ").lower()

            if take_more == "n":
                player_turn = False
                computer_turn = True

            if take_more == "y":
                player_hit()
                if player_score > 21 and 11 in player_hand:
                    ace_index = player_hand.index(11)
                    player_hand[ace_index] = 1
                player_score = sum(player_hand)
                print_both_stats()

        while computer_turn:
            if computer_score < 17:
                computer_hit()
                if computer_score > 21 and 11 in computer_hand:
                    ace_index = computer_hand.index(11)
                    computer_hand[ace_index] = 1
            computer_score = sum(computer_hand)

            if computer_score >= 17:
                computer_turn = False


        if player_score > 21:
            print("--------------------\nYou lose\n--------------------")
            print_player_stats()
            print_computer_stats()
        elif computer_score > 21:
            print("--------------------\nYou win\n--------------------")
            print_player_stats()
            print_computer_stats()
        elif player_score > computer_score:
            print("--------------------\nYou win\n--------------------")
            print_player_stats()
            print_computer_stats()
        elif player_score < computer_score:
            print("--------------------\nYou lose\n--------------------")
            print_player_stats()
            print_computer_stats()
        else:
            print("--------------------\nDraw\n--------------------")
            print_player_stats()
            print_computer_stats()

        start_game_input = input("--------------------\nDo you want to play again? Type 'y' or 'n': ").lower()
        print("--------------------")
        if start_game_input == "y":
            player_hand.clear()
            computer_hand.clear()
            game_live = True
        elif start_game_input == "n":
            exit()