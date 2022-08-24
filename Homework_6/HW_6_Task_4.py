# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# ```
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# ```

def is_second_entry(indexes):
    if len(indexes)>1:
        return indexes[1]
    else:
        return 'There is not the 2nd entry((('

words_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
word = "йцу"

indexes = list(map(lambda item: item[0], filter(lambda item: item[1] == word, enumerate(words_list))))

print(is_second_entry(indexes))







# list_for_checking = ['oleg', 'ksu', 'matvey', 'olegd', 'oleg']

# word_to_find = input('Input a word for searching in the list: ')

# def find_word_in_list (word, list_for_search):
#     count = 0
#     flag = False
#     for i in range(len(list_for_search)):
#         if list_for_search[i] == word:
#             count +=1
#             if count == 2:
#                 flag = True
#                 break
#     if flag == True:
#         print(f'The 2nd entry of "{word}" in list {list_for_search} has index [{i}]')
#     else:
#         print(f'There is not the 2nd entry of "{word}" in list {list_for_search}')

# find_word_in_list(word_to_find, list_for_checking)