# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# ```
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# ```

import random
from methods import check_value_is_digit_and_return_it as check
from methods import make_new_random_list_numbers as make_list

def get_list_multiply_pairs (list_to_find):
    mult_pairs_list = []
    for i in range (int((len(list_to_find)+1)/2)):
        mult_pairs_list.append (list_to_find[i]*list_to_find[-1-i])
    return mult_pairs_list

list_to_find = make_list(0,10)
mult_pairs_list = get_list_multiply_pairs(list_to_find)

print (f'Original list {list_to_find}\nResult list {mult_pairs_list}')

