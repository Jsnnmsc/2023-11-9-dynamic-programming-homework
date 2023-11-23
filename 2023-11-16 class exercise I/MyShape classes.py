import math


class MyShape:

    def __init__(self, square_side, length, width, radius):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def __str__(self):
        return f"Rectangle_area: {self.get_rectangle_area()}, Square_area: {self.get_square_area()}, Circle_area: {self.get_circle_area()}"

    def get_rectangle_area(self):
        return self.length * self.width

    def get_square_area(self):
        return self.square_side**2

    def get_circle_area(self):
        return (self.radius ** 2) * math.pi


shp = MyShape(2, 3, 4, 5)
print(shp)
