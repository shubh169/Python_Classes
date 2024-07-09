import logo
import os
print(logo.logo)
print("Welcome to the Secret Auction program.")

auction_dict={}
def auction(new_name,bid_price):
    auction_dict[new_name]=bid_price
    
def auction_result(new_auction_dict):  
    result=0
    for key in new_auction_dict:
        if new_auction_dict[key]>result:
            result=new_auction_dict[key] 
            winner=key 
    print(f"The winner {winner} is with ${result} bid.")



auction_start=True
while auction_start:
    name=input("What is your name?\n")
    bid=float(input("What is your bid $?\n"))
    auction(name,bid)
    choice=input("Are there any other bidders? type yes or no:\n").lower()
    if os.name == 'nt':
        os.system('cls')

    if choice=='no':
        auction_result(auction_dict)
        auction_start=False
