# Secrect Auction 
# Author >>> Yago Goltara

from os import system
from art import logo
from time import sleep

auction_dic = {}
want_continue = True

def secret_auction(name, bid_price):
        auction_dic[name] = bid_price

def biggest(bid_dictionary):
    biggest_bid = 0
    for key in auction_dic:
        if biggest_bid < auction_dic[key]:
            biggest_bid = auction_dic[key]
            bigname = key
    print(f"The biggest bid price was ${biggest_bid} by {bigname}.")

while want_continue == True:
    print(logo,"\nWelcome to the Bid Auction!")
    name = input("Type your name: ")
    bid = int(input("Type the bid price: $"))
    
    secret_auction(name = name, bid_price = bid)

    opt = input("Do you want to continue? ").lower()
    system('cls')
    if opt == "no":
        want_continue = False
        print(logo)
        biggest(bid_dictionary = auction_dic)

sleep(4)