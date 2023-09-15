

import os

os.environ['TERM'] = 'xterm'
# HINT: You can call clear() to clear the output in the console.
import uart

print(uart.logo_bidding)

def find_highest_bid(bidding_reocrd):
    highest_bidding = 0
    for i in bidding_reocrd:
        bidding_amount = bidding_reocrd[i]
        if bidding_amount > highest_bidding:
            highest_bidding = bidding_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bidding}")


dict = {}
should_continue = False
while not should_continue:
    os.system('clear')
    name = input("What's your name ?: ")
    bid = int(input("How much do you want to bid?: $"))

    dict[name] = bid
    restart = input("Are there any bidders left? Type yes to continue or no to exit\n")
    if restart == "no":
        should_continue = True
find_highest_bid(dict)


