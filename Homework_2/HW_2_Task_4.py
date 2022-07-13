# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time
import math

# метод находит рандомное число из диапазона разрядности (1: от 0 до 9, 2: от 0 до 99 ... 6: - от 0 до 999999)
def find_rand (dec_place): 
    rand_1 = int(time.time()*1000000%math.pow(10, dec_place))
    rand_2 = int(time.time()*10000%math.pow(10, dec_place))
    return int(math.fabs(rand_1-rand_2))

# метод находит рандомное число из диапазона разрядности (1: от -9 до 9, 2: от -99 до 99 ... 6: от -999999 до 999999)
def find_rand_includ_negat (dec_place): 
    rand_1 = int(time.time()*1000000%math.pow(10, dec_place))
    rand_2 = int(time.time()*10000%math.pow(10, dec_place))
    return int(rand_1-rand_2)
    

print(find_rand(3))
print(find_rand_includ_negat(3))

