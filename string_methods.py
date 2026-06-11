name = input("Enter your name: ")

length = len(name)
print(f"Your name has {length} characters")

name = name.find(" ")   # returns the index of the first space, -1 if not found
print(name)

name = name.rfind(" ")  # returns the index of the last space
print(name)

name = name.capitalize()
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

name = name.isDigit()
print(name)

name = name.isalpha()
print(name)

name = name.isalnum()   # returns true if the string is alphanumeric
print(name)

phone_number = input("Enter your phone number: ")
print(phone_number.count("-"))

name = name.replace(" ", "")
print(name)

