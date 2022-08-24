# Сформировать список из  N членов последовательности.
# ```
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# ```

from methods import check_value_is_positive_integer_and_return_it as check
import math

number_N = check('Input the number of elements in sequence: ')
print ([int(math.pow(-3, i)) for i in range (number_N)])