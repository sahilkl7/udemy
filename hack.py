from collections import Counter

# Read the number of shoes
num_shoes = int(input())

# Read the list of shoe sizes in the shop
shoe_sizes = list(map(int, input().split()))

# Create a Counter to keep track of available shoe sizes
shoe_counter = Counter(shoe_sizes)

# Read the number of customers
num_customers = int(input())

# Initialize the total earnings
total_earnings = 0

for i in  range(num_customers):
    desired_size, price = map(int, input().split())

    if shoe_counter[desired_size] > 0:
        total_earnings += price
        shoe_counter[desired_size] -1
print(total_earnings)
