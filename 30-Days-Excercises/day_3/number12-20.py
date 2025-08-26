""" Prompt 12 """

print('dragon and python')

x = len('dragon')
y = len('python')

print(x)
print(y)
print( x != y)

# 13.
print('on in python and dragon', 'on' in 'python' and 'on' in 'dragon')

# 14.
print('I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')

# 15.
print('on is not in python and dragon', 'on' not in 'python' + 'dragon')

# 16.
x = len('python')
print('The length of python is: ', x)
print('This is a', type(x))
print('It is now a', type(float(x)))
print('It is now a', type(str(x)))

# 17.
i: int = 10
if i % 2 == 0:
    print(True)
else:
    print(False)

# 18.

i: float = int(2.7)
if 7 // 3 == i:
    print(True)
else:
    print(False)

# 19.

x: str = '10'
y: int = 10

print(x == y)

# 20.

i: int = 9.8
j: int = 10

print(i == j)
