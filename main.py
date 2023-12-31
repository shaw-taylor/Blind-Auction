from replit import clear
from art import logo
print(logo)

bids = {}
continue_loop = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
        

while continue_loop:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    question = input("Are there any other bidders? Type 'yes' or 'no'. \n ").lower()
    
    bids[name] = price
    if question == "no":
        continue_loop = False
        find_highest_bidder(bids)
        
    elif question == "yes":
        clear()
    