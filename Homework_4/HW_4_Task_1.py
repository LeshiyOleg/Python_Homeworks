# Вычислить число ПИ=3,1415926535 c заданной точностью d. Число Пи не просто обрезать с math.pi, 
# а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# ```
# Пример:
# при d = 0.001, π = 3.141.    10^(-10) ≤ d ≤ 10^(-1)
# ```

from methods import check_value_is_positive_integer_and_return_it as check_input

# функция рассчитывает число ПИ с помощью ряда Нилаканта, в качестве аргумента 
# передается порядковый знак после запятой
def find_pi_approx (round_pos:int) -> float:
    result_pi = 3
    for i in range (2,3000,4):
        result_pi += 4/(i*(i+1)*(i+2)) - 4/((i+2)*(i+3)*(i+4))
    return round(result_pi, round_pos)

rounding_position = check_input ("Input digit's position to the right after decimal point: ")

print(f'PI number with rounding to the {rounding_position} digit after decimal point: {find_pi_approx (rounding_position)}')