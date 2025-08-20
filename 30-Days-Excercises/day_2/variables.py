""" Day 2 """

# Day 2: 30 Days of python programming

# Excersize 1
first_name:  str = 'Matthew'
last_name: str = 'Publico'
full_name: str = first_name + ' ' + last_name
country: str = 'USA'
city: str = 'San Francisco'
age: int = 21
year: int = 2025
is_married: bool = False
is_true: bool = True
is_light_on: bool = False
num, fruit, is_false, deci = 21, 'apple', True, 3.14

# Excersize 2
print(type(first_name))
print(type(full_name))
print(type(age))
print(type(is_married))

print(len(first_name))
print(len(last_name))
print(len(first_name) == len(last_name))

num_one: int = 5
num_two: int = 4

# Addition
x: int = num_one + num_two
print(x)

# Subtraction
y: int = num_two - num_one
print(y)

# Multiplication
z: int = num_one * num_two
print(z)

# Division
w: int = num_one / num_two
print(w)

# Modulus
i: int = num_two % num_one
print(i)

# Exponential
j: int = num_one ** num_two
print(j)

# Integer Division
k: int = num_one // num_two
print(k)

print('-------------------------------------------')
r = float(input('Enter the radius of the circle: '))
pi: float = 3.14159

area_of_circle: float = pi * r ** 2
print('The area of the circle is', area_of_circle)

circum_of_circle: float = 2 * pi * r
print('The circumference of the circle is', circum_of_circle)
print('-------------------------------------------')

print('Please Input Information')
first_name = input('First Name: ')
last_name = input('Last Name: ')
country = input('country: ')
print(f'Hello! {first_name} {last_name}. You are from {country}. Bye Bye!')

help('keywords')
