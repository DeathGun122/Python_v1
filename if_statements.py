age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to vote")
elif age < 0:
    print("You are not yet born")
elif age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Here is your food")
elif response == "N":
    print("No food for you")
else:
    print("Invalid response")

name = input("Enter your name: ")

if name == "":
    print("You did not enter a name")
else:
    print(f"Hello {name}")

# With boolean variables
is_eligible = age >= 18

if is_eligible:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

if not is_eligible:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")