# Dictionary -> Key-Value Pair; Ordered, changeable, no duplicates

capitals = {
    "USA" : "Washington D.C.",
    "India": "New Delhi",
    "Russia": "Moscow",
    "China": "Beijing"
}

print(capitals.get("USA"))
if capitals.get("Japan"):
    print("That Capital exists")
else:
    print("That Capital does not exist.")

capitals.update({
    "Germany": "Berlin",
    "USA": "Detroit"
})

print(capitals)

# capitals.pop("China")

# capitals.popitem()
# print(capitals)

# capitals.clear()

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
# Returns an object like a 2d list of tuples of key-value pairs
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")