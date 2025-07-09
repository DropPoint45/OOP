import math
class Shape:
    def area(self):
        return 0
    def perimetr(self):
        return 0

class Rectangle(Shape):
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height

    def area(self):
        return self.widht * self.height

    def perimetr(self):
        return 2 * (self.height + self.widht)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def  perimetr(self):
        return 2 * math.pi * self.radius

def area_perimtr(shape):
    print(shape.area(), shape.perimetr())

shapes = [Rectangle(2, 4), Circle(3)]
for shape in shapes:
    area_perimtr(shape)







