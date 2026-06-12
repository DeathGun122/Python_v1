for i in range(1, 11):
    print(i)

for i in reversed(range(1, 11, 2)):  # start, stop, step
    print(i)

print("Happy New Year")

credit_card_number = "1234-5678-9012-3456"

for i in credit_card_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        continue    # skip 13
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        break       # exit the loop
    print(i)