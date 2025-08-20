""" Day 3 """

age:int = 21
height:float = 165.1 # Converted to cm
com: complex = 2 + 3j

print('Calculate the area of a Triangle')
x: float = float(input('Enter base: '))
y: float = float(input('Enter height: '))
area: float = 0.5 * x * y

print('The area of this Triangle is: ', area)
print('--------------------------------------')

print('Now to calculate for the perimeter')
a: int = int(input('Enter for the first side: '))
b: int = int(input('Enter for the second side: '))
c: int = int(input('Enter for the third side: '))
perimeter = a + b + c

print('The perimeter for the Triangle is: ', perimeter)
print('--------------------------------------')

print('Rectangle')
length: int = int(input('Length: '))
width: int = int(input('Width:'))
rect_area = length + width
rect_perimeter = 2 * rect_area

print('Area and Perimeter', rect_area, rect_perimeter)
