# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# ```
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# ```

def find_factorial (number):
    if number == 1:
        result = 1
    else:
        result = number * find_factorial(number-1)
    return result

count = 1
while True:
    number_N = input("Input a number N to calculate the multiplication from 1 to N: ")
    if number_N.isdigit():
        number_N = int(number_N)
        lst_to_print = []
        for i in range(number_N):
            lst_to_print.append(find_factorial(i+1))
        print(f'Factorials of numbers from 1 to {number_N}: {lst_to_print}')
        break
    elif count < 3:
        print("This is not an integer number --> Try again")
        count +=1
    else:
        print("Exceeded number of input attempts. Think what you're doing wrong --> Closing the program")
        break
