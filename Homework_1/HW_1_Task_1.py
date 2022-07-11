# 1- Напишите программу, которая принимает на вход
#  цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# ```
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет
# ```

count = 0
attempts = 3
while True:
    if count == attempts:
        print('\n Вы превысили максимальное количество попыток ввода!')
        break
    input_number = input('Введите номер дня недели от 1 до 7: ')
    if not input_number.isdigit():
        count = count + 1
        print(
            f'\n Вы ввели не число. Попробуйте снова. У вас осталось {attempts-count} попыток.')
    elif not 1 <= int(input_number) <= 7:
        count = count + 1
        print(
            f'\n Ваше число не соответствует запросу. Попробуйте снова. У вас осталось {attempts-count} попыток.')
    else:
        if 1 <= int(input_number) <= 5:
            print('это рабочий день')
        else:
            input_number == 6 or input_number == 7
            print('это выходной')
        break
