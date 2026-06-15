menu = {
    "Pizza": 10.99,
    "Burger": 8.99,
    "Fries": 3.99,
    "Soda": 2.99,
    "Nachos": 6.99,
    "Ice Cream": 4.99,
    "Lemonade": 2.99,
    "Popcorn": 3.99
}

cart = []
total = 0

print("------------MENU------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ")