weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/P): ")

if unit == "K":
    weight *= 2.205
    unit = "P"
elif unit == "P":
    weight /= 2.205
    unit = "K"
else:
    print("Invalid unit")
    exit()

print(f"Your weight is {round(weight, 2)} {unit}")