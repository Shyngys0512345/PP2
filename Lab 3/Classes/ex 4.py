import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point({self.x}, {self.y})")
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
dx = int(input("Enter dx value to move: "))
dy = int(input("Enter dy value to move: "))

p1 = Point(x, y)
p2 = Point(x + dx, y + dy)

p1.show()
p2.show()

p1.move(dx, dy)
p2.move(dx, dy)

p1.show()
p2.show()

print("The distance between two points is:", p1.dist(p2))