import math
# Arithmetic Operators
# +, -, *, /, //, %

friends = 0
friends = friends + 1
print(friends)

# Augmented Assignment Operator
friends = 0
friends += 1
print(friends)

friends -= 1
print(friends)

friends *= 2
print(friends)

friends /= 2    # float division
print(friends)

friends //= 2  # floor division (returns integer)
print(friends)

friends %= 2    # remainder
print(friends)

friends **= 2   # power / exponent
print(friends)

# Math Functions

x = 3.14
y = 4
z = 5

print(round(x))
print(abs(x))
print(max(x, y, z))
print(min(x, y, z))
print(pow(x, y))
print(pow(x, y, z))  # pow(base, exponent, modulo)


print(math.pi)
print(math.e)
print(math.sqrt(4))

print(math.ceil(x))     # rounds up
print(math.floor(x))    # rounds down

print(math.log(x))
print(math.log10(x))
print(math.log2(x))