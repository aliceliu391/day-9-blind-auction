from replit import clear

#Print starting art
from art import logo

print(logo)

#Checks if there are other bidders
other_bidders = True

#Creates dictionary to keep track of names and bids
bidding = {}

while(other_bidders):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    #Adds a new entry for the bidder with their name and bid
    bidding[name] = bid

    #Checks for additional bidders
    others = input("Are there any other bidders? Type 'yes' or 'no'. ")
    
    if others == "no":
        other_bidders = False
        
    clear()

highest_bid = 0
highest_bidder = ""

for bidder in bidding:
    #If the new bid is higher than the highest bid, it becomes the new highest bid
    if bidding[bidder] > highest_bid:
        highest_bid = bidding[bidder]
        highest_bidder = bidder
        
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
