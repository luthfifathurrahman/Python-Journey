from art import logo
from os import system

def find_higher_bidder(dict):
    higher_bid = 0
    winner = ""
    for key in dict:
        if dict[key] > higher_bid:
            higher_bid = dict[key]
            winner = key
        elif dict[key] == higher_bid:
            winner += " and " + key
    if "and" in winner:
        print(f"it is a draw between {winner}")
    else:
        print(f"The winner is {winner} with ${higher_bid} bid")


blind_auction_dict = {}

auction_over = False
while not auction_over:
    print(logo)
    print("welcome to the secret auction program")
    name = input("what is your name? ")
    bid = float(input("what is your bid? $"))
    blind_auction_dict[name] = bid

    add_user = False
    while not add_user:
        additional_user = input("is there any user who want to bid? (Y/N): ").lower()
        if additional_user == "n":
            system("cls")
            add_user = True
            auction_over = True
            print("Auction over")
            find_higher_bidder(blind_auction_dict)
        elif additional_user == "y":
            add_user = True
            system("cls")
        else:
            system("cls")
            print("wrong input")
