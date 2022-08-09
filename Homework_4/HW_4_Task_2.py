# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. Множества не использовать.

from methods import make_new_random_list_int_numbers as new_list

def get_list_of_unique_numb (list_to_get:list) -> list:
    result_list = []
    for item in list_to_get:
        if item not in result_list:
            result_list.append(item)
    return result_list


rand_list_numb = new_list(0, 5)
print (f'Original list: {rand_list_numb}')
print (f'The list with unique elements of original one: {get_list_of_unique_numb(rand_list_numb)}')