# checks if file code must be executed

def favorite_food(food):
    print(f"My favorite food is {food}")

def main():
    print("Hello World")
    favorite_food("Pizza")
    print(__name__) # returns the name of the file

if __name__ == "__main__":
    main()