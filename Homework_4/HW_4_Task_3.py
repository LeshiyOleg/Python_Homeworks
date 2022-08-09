# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# ```
# Пример: при N = 12 -> [2, 3]
# ```

from methods import check_value_is_positive_integer_and_return_it as check_input

# функция выдает список простых чисел от 2 до N (вводится как аргумент)
def find_primes_till_N (number_to_find:int)->list:
    primes_list = [2]
    for i in range (3, number_to_find+1):
        flag = True
        while flag == True:
            for j in range (2, i):
                if i % j == 0:
                    flag = False
            if flag == True:
                primes_list.append(i)
                break
    return primes_list

def find_list_of_prime_multipliers (number_N:int)->list:
    primes_list = find_primes_till_N (number_N//2)
    multipliers_list = []
    for item in primes_list:
        while number_N % item == 0:
            multipliers_list.append(item)
            number_N /= item
    if len(multipliers_list) == 0:
        print(f'The number {number_N} is prime')
        quit()
    return list(set(multipliers_list)) 

number_N = check_input('Input number N to find the list of its prime dividers: ')

print(find_list_of_prime_multipliers(number_N))
