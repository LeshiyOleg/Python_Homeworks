# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# ```
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
# ```

from methods import take_data_from_file_and_make_words_list as take_data

# функция находит в списке слов слова без цифр и заносит их в новый список
def get_string_without_digits_in_words(words_list: list) -> list:
    new_list = []
    for item in words_list:
        digit_in_item = False
        for i in range(len(item)):
            if item[i].isdigit():
                digit_in_item = True
        if digit_in_item == False:
            new_list.append(item)
    return new_list

words_list = take_data("Homework_4\example_file_1.txt")
print(words_list)

words_without_digits = get_string_without_digits_in_words (words_list)

print(words_without_digits)
