# Indexing [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[:4])     # 1234, 0 is default
print(credit_number[5:9])   # 5678
print(credit_number[10:14])  # 9012
print(credit_number[15:])   # 3456

# Reverse Indexing
print(credit_number[-1])

# Step
print(credit_number[::3])
last_four = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_four}")

# Reverse String
print(credit_number[::-1])  # Negative step reverses the string