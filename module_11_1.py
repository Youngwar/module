import matplotlib.pyplot as plt
import numpy as np
import math

list_y = []
list_x = []
for t in  range(0, int(20*math.pi)):
    x=6.2*(math.cos(t) - math.cos(3.1*t)/3.1)
    y=6.2*(math.sin(t) - math.sin(3.1*t)/3.1)
    list_x.append(x)
    list_y.append(y)

fig, ax = plt.subplots()
# задается название оси x
ax.set_xlabel('название переменной x')
# задается название оси y
ax.set_ylabel('название переменной y')
# задается название диаграмы
ax.set_title('Эпициклоида \n (почти)')
# генерирует диаграму
ax.plot(list_x, list_y)
# открывает графическое отображение диаграммы
plt.show()

fig, ax = plt.subplots(figsize=(5, 2.7))
# задается легенда для точек на диаграмме
ax.plot(list_x, list_y, 'o', label='data1')
plt.show()
ax.legend()