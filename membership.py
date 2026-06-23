word = "APPLE"

letter = input("Guess a letter in the word: ").upper()

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"There is no {letter}")

if letter not in word:
    print(f"There is no {letter}")
else:
    print(f"There is a {letter}")

students = {"Spongebob", "Patrick", "Squidward", "Sandy", "Mr. Krabs"}

student = input("Enter a student name: ")
if student in students:
    print(f"{student} is in the class.")
else:
    print(f"{student} is not in the class.")

print("ABC" not in students) 

grades = {
    "Spongebob": "A",
    "Patrick": "B",
    "Squidward": "C",
    "Sandy": "A",
    "Mr. Krabs": "B"
}

student = input("Enter a student name to get their grade: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"{student} is not in the class.")

email = "test@example.com"

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")