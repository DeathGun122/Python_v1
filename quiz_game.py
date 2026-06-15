questions = ("What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the smallest planet in our solar system?",
    "What is the largest mammal in the world?",
    "What is the smallest mammal in the world?")

options = (("A. Paris", "B. Rome", "C. London", "D. Madrid"),
           ("A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Elephant", "B. Lion", "C. Giraffe", "D. Whale"),
           ("A. Bat", "B. Mouse", "C. Rat", "D. Squirrel"))

answers = ("A", "A", "A", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter choice(A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score:.2f}%")