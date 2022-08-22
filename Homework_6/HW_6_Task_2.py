# Найти сумму чисел списка стоящих на нечетной позиции

import random

list_of_numbers = []
for i in range(1,10):
    list_of_numbers.append(random.randint(1,10))

result = 0
for i, item in enumerate(list_of_numbers):
    if i%2:
        result += item
print (f'The sum of odd indexes elements of the list {list_of_numbers} is {result}')