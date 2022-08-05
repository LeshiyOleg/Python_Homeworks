# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# ```
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
# ```

from methods import check_value_is_positive_integer_and_return_it as check

def dec_to_bin (dec_num):
    res_rev = ""
    while dec_num > 0:
        res_rev += str(dec_num % 2)
        dec_num //= 2
    if res_rev != "":
        number = int(res_rev[::-1])
    else:
        number = 0
    return number

dec_num = check ('Input the positive integer decimal number to convert to binary: ')
print(f'The binary representation of a decimal number {dec_num} is --> {dec_to_bin (dec_num)}')
