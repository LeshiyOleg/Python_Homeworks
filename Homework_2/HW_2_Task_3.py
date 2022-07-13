# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# ```
# Пример:
# Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
# ```

# elem_number = int(input('Введите число n элементов последовательности 3n + 1 : '))
# dictionary = dict()
# for i in range(1,elem_number+1):
#     temp = 3*i +1
#     dictionary[i] = temp
# print (dictionary)

count = 1
while True:
    number_N = input("\nInput a number N to make a sequence from 1 to N with values (1+1/N)**N: ")
    if number_N.isdigit():
        number_N = int(number_N)
        dict_to_print = {}
        sum = 0
        for i in range(1, number_N+1):
            dict_to_print[i] = round((1+1/i)**i, 2)
            sum += dict_to_print[i]
        print(f'\nFor N = {number_N} the sequence is: {dict_to_print}')
        print(f'The sum of sequence elements: {sum}')
        break
    elif count < 3:
        print("This is not an integer number --> Try again")
        count +=1
    else:
        print("Exceeded number of input attempts. Think what you're doing wrong --> Closing the program")
        break