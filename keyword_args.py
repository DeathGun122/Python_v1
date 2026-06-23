def hello(greeting, title, first, last):
    print(f"{greeting}, {title} {first} {last}!")

hello("Hello", "Dr.", "John", "Doe")
hello(title="Dr.", greeting="Hello", first="John", last="Doe")
hello("Hello", "Dr.", first="John", last="Doe")

for i in range(1, 11):
    print(i, end=" ")
    # end is also a keyword argument

print("1", "2", "3", sep="-")  # sep is a keyword argument