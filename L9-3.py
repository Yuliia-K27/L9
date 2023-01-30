class Parallelogram:
    def __init__(self, width, length):
        self.width = width  # ширина
        self.length = length  # довжина

    def great_area(self):
        return self.width * self.length  # площа паралелограма

Parallelogram1 = Parallelogram(3, 10)
print(Parallelogram1.great_area())

class Square(Parallelogram):
    def great_area2(self):
        return self.length**2

Square1 = Square(3, 10)
print(Square1.great_area2())
