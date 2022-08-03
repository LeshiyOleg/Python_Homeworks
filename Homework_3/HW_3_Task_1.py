# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# ```
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# ```

import random
from methods import check_value_is_digit_and_return_it as check
from methods import make_new_random_list_numbers as make_list

# функция проверяет на четность индекс элемента списка и находит сумму нечетных элементов
def find_sum_odd_element_positions (list_to_find):
    sum = 0
    for i in range(len(list_to_find)):
        if i%2:
            sum += list_to_find[i]
    return sum

list_to_find = make_list(0, 100)
sum = find_sum_odd_element_positions(list_to_find)
print (f'The sum of list {list_to_find} elements from odd positions is {sum}')