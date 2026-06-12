# List
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits)
print(fruits[0])    # Indexing
print(fruits[-1])   # Negative Indexing
print(fruits[1:4])  # Slicing
print(fruits[::2])  # Step

for fruit in fruits:
    print(fruit)

# print(dir(fruits))  # Methods
# print(help(fruits))  # Documentation

print(len(fruits))

# in
print("apple" in fruits)
print("kiwi" in fruits)

# list methods
fruits.append("kiwi")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

# fruits.clear()
# print(fruits)