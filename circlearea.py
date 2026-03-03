import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


radius_value = float(input("Enter the radius of the circle: "))

circle1 = Circle(radius_value)

print("Area of the circle:", circle1.area())
print("Perimeter of the circle:", circle1.perimeter())