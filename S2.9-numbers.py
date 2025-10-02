import math

print (math.factorial(5))
print (math.ceil(2.2))

print ("This program is going to calculate the area and circumference of a circle given the radius.")
radius = float ( input ("Enter the circle's radius: ") )

area = math.pi * ( radius**2 )
circumference = 2 * math.pi * radius

print ("A circle of radius", radius, "has a circumference of", round(circumference, 2), "and an area of", round(area, 2))
