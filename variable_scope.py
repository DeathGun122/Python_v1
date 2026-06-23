# Variable scope
# Global variable -> accessible from anywhere in the program
# Local variable -> accessible from only the function where it is defined

# Scope resolution rule (LEGB)
# Local -> Enclosing -> Global -> Built-in

def fun1():
    a = 1
    print(a)

def fun2():
    b = 2
    print(b)

fun1()
fun2()