# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
# vegetables = ["carrot", "potato", "tomato", "cabbage", "spinach", "broccoli"]
# meats = ["beef", "chicken", "pork", "turkey", "lamb", "venison"]

# groceries = [fruits, vegetables, meats]
groceries = [["apple", "banana", "cherry", "date", "elderberry", "fig"],
             ["carrot", "potato", "tomato", "cabbage", "spinach", "broccoli"],
             ["beef", "chicken", "pork", "turkey", "lamb", "venison"]]

# print(fruits)
# print(fruits[0])

# 2D lists
print(groceries)
print(groceries[0])
print(groceries[0][0])

for foods in groceries:
    for food in foods:
        print(food, end="    ")
    print()

# List of tuples or sets of tuples or tuples of tuples possible