import random
import art
import game_data

score = 0

def print_comparison(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, {a['country']}")
    print(art.vs)
    print(f"Compare B: {b['name']}, {b['description']}, {b['country']}")


while True:
    print(art.logo)

    if score == 0:
        a_compare = random.choice(game_data.data)
        b_compare = random.choice(game_data.data)
        while a_compare['name'] == b_compare['name']:
            b_compare = random.choice(game_data.data)
    else:
        a_compare = b_compare
        b_compare = random.choice(game_data.data)
        print(f"You're right! Current score: {score}")
        print("-----------------------------------")
        while a_compare['name'] == b_compare['name']:
            b_compare = random.choice(game_data.data)


    print_comparison(a_compare, b_compare)
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = a_compare['follower_count']
    b_followers = b_compare['follower_count']
    if a_followers > b_followers and answer == "a":
        score += 1
    elif a_followers < b_followers and answer == "b":
        score += 1
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        print(f"{a_compare['name']} has {a_compare['follower_count']}M followers")
        print(f"{b_compare['name']} has {b_compare['follower_count']}M followers")
        break
