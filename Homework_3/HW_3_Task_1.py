# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# ```
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# ```

import random
from methods import check_value_is_digit_and_return_it

# функция запрашивает количество элементов в списке, а потом формирует его из рандомных элементов
def make_new_random_list_numbers ():
    elem_number = check_value_is_digit_and_return_it ("Please input number of list elements: ")
    random_list_numbers = []
    for i in range(elem_number):
        random_list_numbers.append(random.randint(0, 100))
    return random_list_numbers

def find_sum_odd_element_positions (list_to_find):
    sum = 0
    for i in range(len(list_to_find)):
        if i%2:
            sum += list_to_find[i]
    return sum

list_to_find = make_new_random_list_numbers()
sum = find_sum_odd_element_positions(list_to_find)
print (f'The sum of list {list_to_find} elements from odd positions is {sum}')