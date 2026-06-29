import random

def spin_row():
    symbols = ["🍒", "🍉",  "🍋",  "🔔",  "⭐"]

    return [ random.choice(symbols) for x in symbols ]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def payout(row, bet):

    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20

    return 0

def main():
    balance = 100

    print()
    print("******* Welcome to the slot machine! *******")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print()

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid bet amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("Bet amount must be greater than zero")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        payout_amount = payout(row, bet)
        
        if payout_amount > 0:
            print(f"You won ${payout_amount}!")
        else:
            print("You lost")
            
        balance += payout_amount

        play_again = input("Play again? (y/n): ").lower()

        if play_again != "y":
            break

    print(f"Game over. Final balance: ${balance}")


if __name__ == "__main__":
    main()