import random

low = 1
high = 100
options = ("rock", "paper", "scizzors")
cards = ["A", "2", "3", "4", "5", "6", "7"]

# number = random.randint(low, high)
# print(number)

# number = random.random(low, high)
# print(number)

option = random.choice(options)
print(option)
card = random.choice(cards)
print(card)