""" Prompt 8 & 9 """

print('Task 8')
slope = 2

y: complex = (0,-2)

x = 2/2
x_intercept = (x, 0)

print("Slope (m):", slope)
print("Y-intercept:", y)
print("X-intercept:", x_intercept)
print('--------------------------')

print('Task 9')
x: complex = (2,2)
y: complex = (6,10)

q1: int = 2
p1: int = 2

q2: int = 6
p2: int = 10

m: float = (p2 - p1) / (q2 - q1)

e: float = ((q2 - q1) ** 2) + ((p2 - p1) ** 2)
sqrt_q: float = e ** 0.5

print(f'Slope is {m} and Euclidean is {sqrt_q}')
print(m == slope)
