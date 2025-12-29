#comprehension
# list comprehension
#[expression for item in iterable if condition]
# numbers = [1,2,3,4,5]
# # squares = [x*x for x in numbers ]
# # print(squares)
# even_numbers = [x % 2 == 0 for x in numbers]
# print(even_numbers)#[False, True, False, True, False]
# even_numbers = [x for x in numbers if x%2==0]
# print(even_numbers)#[2, 4]
# # https://youtu.be/WnqWVToL9jM?t=29714
# even_numbers = [x for x in range(10) if x%2==0]
# print(even_numbers)#[0, 2, 4, 6, 8]

# words = ['hello','world','python']
# uppercassed = [word.upper() for word in words]
# print(uppercassed)#['HELLO', 'WORLD', 'PYTHON']

#nested loops
# pairs = [(x, y) for x in range(2) for y in range(4)]
# print(pairs)

# dictionary comprehension
#[key_expression: value_expression for item in iterable if condition]

#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
filtered_dict = {x: x**2 for x in range(10) if x%2==0}
print(filtered_dict)#{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
# https://youtu.be/WnqWVToL9jM?t=30185