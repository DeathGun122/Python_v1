# Lists
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" ")

# Tuples
numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number, end=" ")

# Sets -> Not reversible, but can be iterated over
numbers = {1, 2, 3, 4, 5}

for number in numbers:
    print(number, end=" ")

# Strings
name = "John Doe"

for char in name:
    print(char, end=" ")
print()

# Dictionaries
my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

for key, value in my_dict.items():
    print(f"{key} = {value}")