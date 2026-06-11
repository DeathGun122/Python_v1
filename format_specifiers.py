price1 = 3.14159
price2 = -987.65
price3 = 12.34

# Print the prices with two decimal places
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# Space padding
print(f"Price 1 is ${price1:10.2f}")
print(f"Price 2 is ${price2:10.2f}")
print(f"Price 3 is ${price3:10.2f}")

# Zero padded
print(f"Price 1 is ${price1:010.2f}")
print(f"Price 2 is ${price2:010.2f}")
print(f"Price 3 is ${price3:010.2f}")

# Left justified
print(f"Price 1 is ${price1:<10.2f}")
print(f"Price 2 is ${price2:<10.2f}")
print(f"Price 3 is ${price3:<10.2f}")

# Right justified (default)
print(f"Price 1 is ${price1:>10.2f}")
print(f"Price 2 is ${price2:>10.2f}")
print(f"Price 3 is ${price3:>10.2f}")

# Centered
print(f"Price 1 is ${price1:^10.2f}")
print(f"Price 2 is ${price2:^10.2f}")
print(f"Price 3 is ${price3:^10.2f}")

# Sign
print(f"Price 1 is ${price1:+10.2f}")
print(f"Price 2 is ${price2:+10.2f}")
print(f"Price 3 is ${price3:+10.2f}")

# Sign
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

# Comma
price1 = 1000000.985415245
print(f"Price 1 is ${price1:,.2f}")  # Mixing flags
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")