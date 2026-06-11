# or
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is not cancelled")

# and
temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny outside")
elif temp <= 0 and is_sunny:
    print("It is sunny outside")
    print("It is cold outside")
elif 0 < temp < 28 and is_sunny:        # 0 < x < y
    print("It is sunny outside")
    print("It is neither hot nor cold outside")
else:
    print("It is neither hot nor cold outside")

# not -> negation / inverse
is_raining = True
is_sunny = not is_raining
print(is_sunny)