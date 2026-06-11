name = input("Enter your name: ")

# if name == "":
#     print("You did not enter a name")
# else:
#     print(f"Hello {name}")

while name == "":
    print("You did not enter a name")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("You are not yet born")
    age = int(input("Enter your age: "))
else:
    print(f"You are {age} years old")

food = input("Enter your favorite food(q to quit): ")

while not food == "q":
    print("You did not enter a favorite food")
    food = input("Enter your favorite food: ")
else:
    print("You did not enter a favorite food")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print("You did not enter a number between 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))

print(f"You entered {num}")