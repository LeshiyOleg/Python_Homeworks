import random

# функция проверки ввода целого числа (положительного или отрицательного)
# со счетчиком неверных попыток ввода и автоматическим закрытием программы
# при их превышении

def check_value_is_digit_and_return_it(input_value:str):
    checking_continue = True
    is_minus = False
    count = 1
    while checking_continue:
        value = input(input_value)
        if value[0] == "-":
            value = value.replace("-","")
            is_minus = True
        if value.isdigit():
            number = int(value)
            if is_minus:
                number *= -1
            checking_continue = False
        elif count < 3:
            print(f"This is not an integer number --> Try again\nYou have {3-count} input attempts left")
            count += 1
        else:
            print("Exceeded number of input attempts. Think what you're doing wrong --> Closing the program")
            exit()
    return number

# Функция создает список из целых чисел
# функция запрашивает на вход мин и макс элементы диапазона рандома.
# Тело функции запрашивает количество элементов в списке, а потом формирует его из рандомных элементов
def make_new_random_list_int_numbers (min_rand:int, max_rand:int):
    elem_number = check_value_is_digit_and_return_it ("Please input number of list elements: ")
    random_list_numbers = []
    for i in range(elem_number):
        random_list_numbers.append(random.randint(min_rand, max_rand))
    return random_list_numbers

# Функция создает список из вещественных чисел
# функция запрашивает на вход мин и макс элементы диапазона рандома.
# Тело функции запрашивает количество элементов в списке, а потом формирует его из рандомных элементов
def make_new_random_list_real_numbers (min_rand:int, max_rand:int):
    elem_number = check_value_is_digit_and_return_it ("Please input number of list elements: ")
    random_list_numbers = []
    for i in range(elem_number):
        random_list_numbers.append(round(((random.random())*random.randint(min_rand, max_rand)), 3))
    return random_list_numbers

# функция счетчика неверных попыток ввода с автоматическим закрытием программы
# при их превышении 
def input_options (
                    opt_inquiry = 'Selection options',
                    opt_1 = 'Option_1 message.\n',
                    opt_2 = 'Option_2 message.\n'):
    
    count = 0
    while count < 3:
        option_value = check_value_is_digit_and_return_it (opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        else:
            print(f'Wrong input. You have {2-count} input attempts left ')
            count +=1
    return option_value

# print(make_new_random_list_real_numbers (0, 100))
