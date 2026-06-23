# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)

# [expression for item in iterable if condition]
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

triples = [y * 3 for y in range(1, 11)]
print(triples)

squares = [z ** 2 for z in range(1, 11)]
print(squares)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)


numbers = [1, -5, 3, -2, 0, 4, -1]
positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)
negative_numbers = [n for n in numbers if n < 0]
print(negative_numbers)

even_numbers = [n for n in numbers if n % 2 == 0 and n != 0]
print(even_numbers)

grades = [85, 42, 73, 90, 67, 88, 95, 24, 32, 100]
new_grades = [grade for grade in grades if grade >= 60]
print(new_grades)

grace_marks = [grade + 10 for grade in grades if grade < 60]
print(grace_marks)