# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# ```
# *Пример:
# [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564
# ```

from methods import make_new_random_list_real_numbers as make_list

def find_diff_max_min_fract_part (list_to_find):
    max = min = (list_to_find[0] - int(list_to_find[0]))
    for i in range (1,len(list_to_find)):
        if (list_to_find[i] - int(list_to_find[i])) > max:
            max = (list_to_find[i] - int(list_to_find[i]))
        elif (list_to_find[i] - int(list_to_find[i])) < min:
            min = (list_to_find[i] - int(list_to_find[i]))
    # print (round(max,3))
    # print(round(min,3))
    return (max - min)

new_list = make_list(0, 10)
diff_max_min = round(find_diff_max_min_fract_part(new_list), 3)

print (f'The difference between max and min fractional parts of elements in list {new_list} is {diff_max_min}') 