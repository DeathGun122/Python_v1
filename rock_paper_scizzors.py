import random

options = ("rock", "paper", "scizzors")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scizzors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie")
    elif player == "rock" and computer == "scizzors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scizzors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play Again? (y/n) ").lower() == "y":
        running = False

print("Thanks for playing!")