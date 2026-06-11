# ternary operation
# x if condition else y

num = 5 
print("Positive" if num > 0 else "Negative")

num = 6
is_even = "Even" if num % 2 == 0 else "Odd"
print(is_even)

a = 6
b = 7
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

temp = 30
weather = "Hot" if temp > 20 else "Cold"
print(weather)

user_role = "Admin"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)