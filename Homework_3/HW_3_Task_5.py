# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# ```
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)
# ```

import math
from methods import check_value_is_positive_integer_and_return_it as check

def fibonacci(number):
    if number in (1, 2):
        result = 1
    else:
        result = fibonacci(number - 1) + fibonacci(number - 2)   
    return result

#def negafib(number):

def list_negafib_0_fibonacci (number:int):
    result_list = []
    for i in range(number):
        result_list.append(int(math.pow(-1, number-i+1) * fibonacci(number-i)))
    result_list.append(0)
    for i in range(number):
        result_list.append(fibonacci(i+1))

    print(f'{result_list}')

number = check ('Input the positive integer number to show Negafibonacchi row: ')
list_negafib_0_fibonacci(number)
