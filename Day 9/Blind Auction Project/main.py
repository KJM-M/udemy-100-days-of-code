from art import logo

print(logo)
bidders = {}
highest_bid = 0
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bidders[name] = int(bid_amount)

    if bid_amount > highest_bid:
        highest_bid = bid_amount

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == "no":
        print("\n" * 20)
        winner = max(bidders, key=bidders.get)
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
        break

    print("\n" * 20)






# from art import logo
# print(logo)
#
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
#
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)
