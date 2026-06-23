'''
*args -> Pass non-key arguments to a function
**kwargs -> Pass keyword arguments to a function
* is the unpacking operator
'''

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print() 

display_name("John", "Doe", "is", "a", "developer")

def print_address(**kwargs):
    for key, value in kwargs.items():
            print(f"{key}: {value}")

print_address(street="123 Main St", city="New York", state="NY", zip="10001")