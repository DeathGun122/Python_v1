# input("What is your name?") # input will always return a string
name = input("What is your name?\n")
print(f"Hello {name}")

age = input("How old are you?\n")
print(f"You are {age} years old")

age = int(age) + 1
print("Happy Birthday!")
print(f"You are {age} years old")