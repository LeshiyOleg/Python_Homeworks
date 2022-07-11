# 5- Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# ```
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# ```

import math

coord_x_1 = input('Введите координату X1 точки А: ')
coord_y_1 = input('Введите координату Y1 точки А: ')
coord_x_2 = input('Введите координату X2 точки B: ')
coord_y_2 = input('Введите координату Y2 точки B: ')

try:
    float(coord_x_1) and float(coord_y_1) and float(
        coord_x_2) and float(coord_y_2)
    coord_x_1 = float(coord_x_1)
    coord_y_1 = float(coord_y_1)
    coord_x_2 = float(coord_x_2)
    coord_y_2 = float(coord_y_2)
    print (f'Расстояние между точками A и B равняется {round(math.sqrt((coord_x_1-coord_x_2)**2+(coord_y_1-coord_y_2)**2),2)}')
except ValueError:
    print('Введите корректное значение координат')
