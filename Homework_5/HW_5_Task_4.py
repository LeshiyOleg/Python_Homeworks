# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

from methods import write_in_file as wr_in_file
from methods import take_data_from_file_and_make_chars_list as take_fr_file

# функция забирает список символов и реализует RLE сжатие, результат возвращает в виде строки
def make_rle_compression (list_to_compress:list)-> str:
    list_to_compress.append('1')
    if list_to_compress[-1] == list_to_compress[-2]:
        list_to_compress.pop()
        list_to_compress.append('2')
    count = 1
    result_string = ''
    for i in range(len(list_to_compress)-1):
        if list_to_compress[i] == list_to_compress[i+1]:
            count += 1
        else:
            result_string += str(count) + str(list_to_compress[i])
            count = 1
    return result_string

# функция забирает список символов и реализует RLE восстановление данных, результат возвращает в виде строки
def make_rle_decompression (list_to_decompress:list)-> str:
    count = ''
    result_string = ''
    for i in range(len(list_to_decompress)):
        if list_to_decompress[i].isdigit():
            count += list_to_decompress[i]
        else:
            result_string += list_to_decompress[i]*int(count)
            count = ''
    return result_string

compressed_str = make_rle_compression(take_fr_file ('Homework_5\example_task_4_input.txt'))
wr_in_file(compressed_str, 'Homework_5\example_task_4_output.txt')

decompressed_str = make_rle_decompression (take_fr_file ('Homework_5\example_task_4_output.txt'))
print (decompressed_str)