# import math
# # import math as m
# # from math import pi

# print(math.pi)

# a, b, c, d = 1, 2, 3, 4
# print(a * math.e)
# print(b * math.e)
# print(c * math.e)
# print(d * math.e)

import personal_module as pm

result = pm.pi
print(result)

result = pm.square(5)
print(result)

result = pm.cube(5)
print(result)

result = pm.area(5)
print(result)

result = pm.circumference(5)
print(result)