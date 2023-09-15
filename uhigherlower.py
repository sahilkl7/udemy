import random
import os
from game_data import data
from uart import high_low,vs

os.environ['TERM'] = 'xterm'

print(high_low)

def get_account():
    return random.choice(data)

def format_document(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_guess(guess,follower_count_a,follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
should_continuee = True
account_b = get_account()
while should_continuee:

    account_a = account_b
    account_b = get_account()
    while account_a == account_b:
        account_b == get_account()
    print(f"Compare A: {format_document(account_a)}")
    print(vs)
    print(f"Against B: {format_document(account_b)}")

    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_guess(guess,follower_count_a,follower_count_b)

    os.system('clear')
    print(high_low)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
