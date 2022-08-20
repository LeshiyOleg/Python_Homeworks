# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# ```
# 'абвгдейка - это передача' = >" - это передача"
# ```

# функция находит в списке слова, содержащие определенный набор символов

def find_word_in_text (list_to_find:list, word_to_find:str = 'абв') -> list:
    result_list = []
    for i, item in enumerate(list_to_find):
        if len(item)>=len(word_to_find):
            for j in range(len(item)-len(word_to_find)+1):
                flag = False
                if str(item[j:j+len(word_to_find)])==str(word_to_find):
                    flag = True
                    break
            if flag == False:
                result_list.append(item)
        else:
            result_list.append(item)
    return result_list

path = "Homework_5\example_task_1.txt"
file = open (path, 'w', encoding = 'utf-8')
data = file.write('абвгдейка - это передача')
file.close()

file = open(path, 'r', encoding='utf-8')
data = file.read()
list_to_find = data.split()
file.close()

print (" ".join(list_to_find))
print(" ".join(find_word_in_text(list_to_find)))


# Добавил осле просмотра семинара:
# s = 'абвгдейка - это передача'
# def filter_text(text):
#     text = text.split(' ')
#     func = lambda word: 'абв' not in word
#     return ' '.join(list(filter(func, text)))
# print(filter_text(s))

# print(" ".join(list(filter(lambda word: 'абв' not in word, s.split()))))