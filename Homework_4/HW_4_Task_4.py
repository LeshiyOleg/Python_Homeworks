# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# ```
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
# ```

from methods import take_data_from_file_and_make_words_list as take_data
from methods import write_string_in_file as input_data

# функция находит в списке слов (аргумент_1) слова без цифр, заносит их в новый список, 
# потом новый список записывает в файл (аргумент_2)
def get_string_without_digits_in_words(words_list: list, file_name:str) -> list:
    new_list = []
    for item in words_list:
        digit_in_item = False
        for i in range(len(item)):
            if item[i].isdigit():
                digit_in_item = True
        if digit_in_item == False:
            new_list.append(item)
    file = open(file_name, 'w', encoding = 'utf-8')
    file.write(" ".join(new_list))
    file.close()
    return new_list

# эту функцию использую только для более удобного ввода фразы для проверки задания,
# т.к. по условию фразу берем из файла
input_data("Homework_4\example_file_1.txt") # Мама сшила м0не штаны и7з бере9зовой кор45ы 893.

words_list = take_data("Homework_4\example_file_1.txt")
print(words_list)

words_without_digits = get_string_without_digits_in_words (words_list, "Homework_4\example_file_1.txt")
print(words_without_digits)
