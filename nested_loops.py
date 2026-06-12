for x in range(1, 10):
    print(x, end="")

for i in range(3):
    for j in range(1, 10):
        print(j, end="")
    print()

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()