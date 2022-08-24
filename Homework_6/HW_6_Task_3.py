# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math

def is_coords_ok (coords_input:list):
    if len(coords_input) == 2:
        return coords_input
    else:
        print ("Try again. You need two digits!")
        exit()

def pow_of_diff (coord_list):
    return (int(coord_list[0]) - int(coord_list[1]))**2

def find_sqrt_of_sum (list_to_find):
    sum = 0
    for item in list_to_find:
        sum += item
    return round(math.sqrt(sum),2)

coords_a = [int(item) for item in input('Input coordinates X1 and Y1 of point А using [SPACETAB]: ').split() if item.isdigit()]
is_coords_ok (coords_a)
coords_b = [int(item) for item in input('Input coordinates X2 and Y2 of point B using [SPACETAB]: ').split() if item.isdigit()]
is_coords_ok (coords_b)
pows_list = list(map(lambda item: pow_of_diff(item), zip(coords_a, coords_b)))

print(f'\nThe distance between points A and B is {find_sqrt_of_sum(pows_list)}')

