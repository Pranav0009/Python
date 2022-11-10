w = float(input('Enter the Width of a Rectangle: '))
h = float(input('Enter the Height of a Rectangle: '))
Area = w * h

Perimeter = 2 * (w + h)
print("\n Area of a Rectangle is: %.2f" %Area)
print(" Perimeter of Rectangle is: %.2f" %Perimeter)

import math as math
r=float(input("Enter r of sphere:\n"))
volume=4/3*math.pi*pow(r,3)
print("volume of sphere is %.2f"% volume )

a = int(input('length of first side : '))
b = int(input('length of second side : '))
c = int(input('length of third side : '))

if a == b == c:
    print('Equilateral Triangle')
elif a == b or b == c or a == c:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')