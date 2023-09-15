import uart

print(uart.adventure)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

d1 = input(print("You are at a cross road.Where do you want to go? Type 'left' or 'right'\n")).lower()

if d1 == 'left':
    d2 = input(print(
        "You came to a lake. There is an island iin the middle of the lake.Type 'wait' to wait for the boat.Type "
        "'swim' to swim across")).lower()
    if d2 == 'wait':
        d3 = input(print(
            "You arrive at the island unharmed.There is a house with 3 doors.One red, one blue and one green. Which "
            "do you want to choose?")).lower()
        if d3 == 'blue':
            print("You entered a room full of beasts.Game Over!")
        elif d3 == 'red':
            print("You entered a room full of fire.Game Over!")
        else:
            print("You found the treasure.You won!")
    else:
        print("You were crocodile's meal.Game Over!")
else:
    print("You fell into a hole.Game Over!")
