class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
r = Rectangle(length, width)
print("The area of the rectangle is:", r.area())