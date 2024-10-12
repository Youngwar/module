
first = 'Мама мыла раму'
second = 'Рамена мало было'

i = list(map(lambda x, y: x == y, first, second))
print(i)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        i = open(file_name, 'a', encoding = 'utf-8')
        for k in data_set:
            i.write(f'{str(k)}\n')
        i.close()
        return i
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        i = choice(self.words)
        return i



from random import choice
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())