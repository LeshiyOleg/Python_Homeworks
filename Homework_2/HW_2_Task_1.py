# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# ```
# Пример:
# 6782 -> 23
# 0,56 -> 11
# ```

while True:
    number_to_sum = input("Input a number to calculate the sum of its digits: ")
    try:
        float(number_to_sum)
        if True:
            sum = 0
            for i in range(len(number_to_sum)):
                if number_to_sum[i].isdigit():
                    sum += int(number_to_sum[i])
            print (f'\n The sum of number {number_to_sum} digits is {sum}')
            break
    except ValueError:
        print("This is not a number --> Try again")
        