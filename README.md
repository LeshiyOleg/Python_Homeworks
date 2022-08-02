# Условия задач для домашних заданий

## Домашнее задание № 1. Знакомство с Python

### HW_1_Task_1
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
```
Пример:
6 -> да
7 -> да
1 -> нет
```

### HW_1_Task_2
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

### HW_1_Task_3
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
```
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
```
### HW_1_Task_4
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

### HW_1_Task_5
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
```
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
```
--------------------------------------------------------

# Домашнее задание № 2. Знакомство с Python (Продолжение)

### HW_2_Task_1
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
```
Пример:
6782 -> 23
0,56 -> 11
```

### HW_2_Task_2
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
```
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
```
### HW_2_Task_3
Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
```
Пример:
Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
```
### HW_2_Task_4
Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

--------------------------------------------------------

# Домашнее задание № 3. Данные, функции и модули в Python

Домашнее задание оформляйте в виде возвращающих функций. Помните: то, что выдает ваша функция, может быть использовано в дальнейшем или выведено куда-то кроме консоли.

### HW_3_Task_1
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
```
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
```

### HW_3_Task_2
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

```
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
```

### HW_3_Task_3
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
```
*Пример:
[1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564
```

### HW_3_Task_4
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
```
Пример:
45 -> 101101
3 -> 11
2 -> 10
```

### HW_3_Task_5
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
```
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)
```