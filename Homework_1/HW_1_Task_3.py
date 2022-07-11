# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# ```
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# ```

coord_x = input('Введите значение координаты X = ')
coord_y = input('Введите значение координаты Y = ')

try:
    float(coord_x) and float(coord_y)
    if float(coord_x) > 0 and float(coord_y) > 0:
        print('Точка находится в 1-й четверти')
    elif float(coord_x) < 0 and float(coord_y) > 0:
        print('Точка находится во 2-й четверти')
    elif float(coord_x) < 0 and float(coord_y) < 0:
        print('Точка находится в 3-й четверти')
    elif float(coord_x) > 0 and float(coord_y) < 0:
        print('Точка находится в 4-й четверти')
    else:
        print('Введите значения X и Y не равные нулю')
except ValueError:
    print('Введите корректное значение координат')
