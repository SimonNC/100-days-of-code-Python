from art import logo
from functions import clean

print(logo)
bidding_finished = False
bids = {}


def find_highest_bidder(bidding_record):
  """Finds the highest bidder from a bidding record"""
  max_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > max_bid:
      max_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${max_bid}")


while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bids[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clean()