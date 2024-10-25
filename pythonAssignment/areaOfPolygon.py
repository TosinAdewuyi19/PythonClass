import math
print(input("Input number sides on the polygon: "))
print(input("Input the length of one if the sides: "))
n = 7
s = 6
area = (n * s**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)
