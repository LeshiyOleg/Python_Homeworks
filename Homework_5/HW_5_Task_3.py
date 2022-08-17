# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ```
# ['python', 'c#']
# [1,2]
# ```
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# ```
# [(1,'PYTHON'), (2,'C#')]
# ```
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков 
# слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж 
# остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# ```
# [(1,'PYTHON'), (102,'C#')]
# ```
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

def take_data_from_file_and_make_lines_list (file_name:str)-> list: 
    file = open(file_name, 'r', encoding = 'utf-8')
    data = file.read().splitlines()
    file.close()
    return data

def get_tuple_order_num_big_letters_lang (lang_list: list) -> tuple:
    res_tuple = [item.upper() for item in lang_list]
    res_tuple = list(enumerate(res_tuple, start = 1))
    return res_tuple

def find_sum_letters_values (lang_tuple:tuple) -> tuple:
    lang_tuple = list(lang_tuple)
    res_list = []
    for item in lang_tuple:
        item = list(item)
        # print (item)
        chars = list(item[1])
        sum = 0
        for j in range (len(chars)):
            sum += ord (chars[j])
        # print (sum)
        if sum%item[0] == 0:
            item[0] = sum
            res_list.append(item)
    return (res_list)

file_name = 'Homework_5\example_task_3.txt'
lang_list = take_data_from_file_and_make_lines_list(file_name)
lang_tuple = get_tuple_order_num_big_letters_lang(lang_list)
print (f'The list of languages: {lang_tuple}')
print(f'The result list: {find_sum_letters_values(lang_tuple)}')
