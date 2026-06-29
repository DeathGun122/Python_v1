# Variable scope
# Global variable -> accessible from anywhere in the program
# Local variable -> accessible from only the function where it is defined

# Scope resolution rule (LEGB)
# Local -> Enclosing -> Global -> Built-in

# def fun1():
#     a = 1
#     print(a)

# def fun2():
#     b = 2
#     print(b)

# fun1()
# fun2()

# def fun1():
#     x = 1

#     def fun2():
#         print(x)

#     fun2()
#     print(x)

# fun1()

# def fun1():
#     print(x)

# def fun2():
#     print(x)

# x = 1
# fun1()
# fun2()

from math import e

def fun1():
    print(e)

# e = 3

fun1()