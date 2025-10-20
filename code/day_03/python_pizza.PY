print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
cost_of_pizza = 0

if size == "S":
    cost_of_pizza += 15
elif size == "M":
    cost_of_pizza += 20
elif size == "L":
    cost_of_pizza += 25
else:
    print("You have ordered a wrong size")

if pepperoni == "Y":
    if size == "S":
        cost_of_pizza += 2
    else:
        cost_of_pizza += 3

if extra_cheese == "Y":
    cost_of_pizza += 1

print(f"Your final bill is: ${cost_of_pizza}.")
