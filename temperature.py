unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "F"
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C"
else:
    print("Invalid unit")
    exit()

print(f"The temperature is {temp} {unit}")