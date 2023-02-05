class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

length = int(input("Enter the length of the square: "))
s = Square(length)
print("The area of the square is:", s.area())