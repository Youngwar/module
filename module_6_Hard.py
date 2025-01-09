import math


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled = True):
        self.sides = __sides
        self.color = __color
        self.filled = filled

    def get_color(self):
        a = []
        for i in self.color:
            a.append(i)
        return a

    def __is_valid_color(self, _color):
        k = True
        for i in _color:
            if 0 <= i <= 255:
                k = True
            else:
                k = False
                break
        return k

    def set_color(self, r, g, b):
        self._color = (r, g, b)
        a = Figure.__is_valid_color(self, self._color)

        if a == True:
            self.color = self._color
    def __is_valid_sides(self, *args):
        sides = args
        for i in sides:
            isinstance(i, int)

    def get_sides(self):
        return self.sides

    def __len__(self):
        isinstance(self.sides, int)
        if True:
            p = self.sides
        else:
            p = sum(self.sides)
        return p

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.sides = []
            self.sides.append(*new_sides)


class Circle(Figure):

    def __init__(self, __color, __sides):
        self.sides_count = 1.

        isinstance(__sides, int)
        if True:
            self.sides = 1

        elif len(__sides) == self.sides_count:
            self.sides = __sides
        __radius = self.sides/(2*math.pi)






    def get_square(self):
        s = self.sides**2/(4*math.pi)
        return s


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        Figure.__len__(self.sides)
        s = ((p/2)*((p/2)-self.sides[0])*((p/2)-self.sides[1])*((p/2)-self.sides[2]))**0.5
        return s

class Cube(Figure):

    def __init__(self, __color, __sides):
        sides_count = 12
        self.sides = [__sides]
        self.color = __color
        for i in range (1, sides_count):
            self.sides.append(__sides)

    def get_volume(self):
        v = self.sides[0]**3
        return v

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
circle2 = Circle((200, 200, 100), 20)  # (Цвет, стороны)

# print(len(circle2))

cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(*circle1.sides)
# Проверка объёма (куба):
print(cube1.get_volume())
