principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle amount must be greater than zero")

# while rate <= 0:
#     rate = float(input("Enter the rate of interest: "))
#     if rate <= 0:
#         print("Rate of interest must be greater than zero")

# while time <= 0:
#     time = float(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time must be greater than zero")

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than zero")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be greater than zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero")
    else:
        break

compound_interest = principle * (1 + (rate / 100)) ** time
print(f"Principle amount: {principle:,.2f}")
print(f"Rate of interest: {rate}")
print(f"Time: {time}")
print(f"The compound interest is {compound_interest:,.2f}")