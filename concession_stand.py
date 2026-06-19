menu = {
    "pizza": 10.99,
    "burger": 8.99,
    "fries": 3.99,
    "soda": 2.99,
    "nachos": 6.99,
    "icecream": 4.99,
    "lemonade": 2.99,
    "popcorn": 3.99
}

cart = []
total = 0

print("------------MENU------------")
for key, value in menu.items():
    print(f"{key.capitalize():10}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR CART------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")