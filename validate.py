username = input("Enter your username: ")

if len(username) > 12:
    print("Username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username can only contain letters")
else:
    print(f"Welcome {username}")