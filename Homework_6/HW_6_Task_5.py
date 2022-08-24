# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# indexes = list(map(lambda item: item[0], filter(lambda item: item[1] == word, enumerate(words_list))))

from methods import make_new_random_list_int_numbers as make_list

init_list = make_list(0,10)
mult_list = [init_list[i]*init_list[-1-i] for i in range((len(init_list)+1)//2)]

print (f'Original list {init_list}\nResult list {mult_list}')

