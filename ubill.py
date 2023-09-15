#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator !")

bill = int(input("What was the total bill?$ "))
percentage_tip = int(input("What percent you want to give tip? 10,12 or 15? "))
split = int(input("How many people you want to split the bill? "))

bill_tip = round((bill * percentage_tip)/100,2)

new_bill = bill_tip + bill

new_amount = new_bill/split

print(f"Each person should pay : ${new_amount}")



