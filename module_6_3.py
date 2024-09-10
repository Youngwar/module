class Horse:

    x_distance = 0
    sound = "Frrr"

    def __init__(self, dx = 0):
        self.dx = dx
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy = 0):
        self.y_distance += dy

class Pegasus(Eagle, Horse):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        return print(self.sound)


p1 = Pegasus()
print(Pegasus.mro())

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
