# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit
import cProfile
import sys

sys.setrecursionlimit(10000)

# Вариант 1
def get_min_max_items(array):
    min_index = 0
    max_index = 0

    for i in range(len(array)):
        if array[i] < array[min_index]:
            min_index = i
        if array[i] > array[max_index]:
            max_index = i

    return min_index, max_index


def get_summa(array, min_index, max_index):
    summa = 0

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    for i in range(min_index + 1, max_index):
        summa += array[i]

    return summa


def main(min_item, max_item, size):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    min_index, max_index = get_min_max_items(array)
    sum_ = get_summa(array, min_index, max_index)

print(timeit.timeit('main(1, 1000, 500)', number=100, globals=globals()))  # 0.06226069200056372
print(timeit.timeit('main(1, 1000, 1000)', number=100, globals=globals()))  # 0.09703129700028512
print(timeit.timeit('main(1, 1000, 2000)', number=100, globals=globals()))  # 0.20239450999906694
print(timeit.timeit('main(1, 1000, 4000)', number=100, globals=globals()))  # 0.391203471001063
print(timeit.timeit('main(1, 1000, 8000)', number=100, globals=globals()))  # 0.7411381490001077

cProfile.run('main(1, 1000, 500)')
cProfile.run('main(1, 1000, 1000)')
cProfile.run('main(1, 1000, 2000)')
cProfile.run('main(1, 1000, 4000)')
cProfile.run('main(1, 1000, 8000)')
# 1    0.001    0.001    0.001    0.001 les_04_task_01.py:13(get_min_max_items)
# 1    0.000    0.000    0.000    0.000 les_04_task_01.py:26(get_summa)
# 1    0.000    0.000    0.017    0.017 les_04_task_01.py:38(main)
# 1    0.002    0.002    0.016    0.016 les_04_task_01.py:39(<listcomp>)


# Вариант 2
# def get_min_item(array):
#     min_index = 0
#
#     for i in range(len(array)):
#         if array[i] < array[min_index]:
#             min_index = i
#
#     return min_index
#
#
# def get_max_item(array):
#     max_index = 0
#
#     for i in range(len(array)):
#         if array[i] < array[max_index]:
#             max_index = i
#
#     return max_index
#
#
# def get_summa(array, min_index, max_index):
#     summa = 0
#
#     if min_index > max_index:
#         min_index, max_index = max_index, min_index
#
#     for i in range(min_index + 1, max_index):
#         summa += array[i]
#
#     return summa
#
#
# def main(min_item, max_item, size):
#     array = [random.randint(min_item, max_item) for _ in range(size)]
#     min_index = get_min_item(array)
#     max_index = get_max_item(array)
#     sum_ = get_summa(array, min_index, max_index)
#
# print(timeit.timeit('main(1, 1000, 500)', number=100, globals=globals()))  # 0.061474029998862534
# print(timeit.timeit('main(1, 1000, 1000)', number=100, globals=globals()))  # 0.09614332799901604
# print(timeit.timeit('main(1, 1000, 2000)', number=100, globals=globals()))  # 0.1932959679998021
# print(timeit.timeit('main(1, 1000, 4000)', number=100, globals=globals()))  # 0.37120865599899844
# print(timeit.timeit('main(1, 1000, 8000)', number=100, globals=globals()))  # 0.7344178319999628
#
# cProfile.run('main(1, 1000, 8000)')
# 1    0.001    0.001    0.001    0.001 les_04_task_01.py:57(get_min_item)
# 1    0.000    0.000    0.000    0.000 les_04_task_01.py:67(get_max_item)
# 1    0.000    0.000    0.000    0.000 les_04_task_01.py:77(get_summa)
# 1    0.000    0.000    0.015    0.015 les_04_task_01.py:89(main)
# 1    0.002    0.002    0.014    0.014 les_04_task_01.py:90(<listcomp>)


# Вариант 3
# def get_min_max_items(array, count=0, min_index=0, max_index=0):
#     if count == len(array):
#         return min_index, max_index
#
#     if array[count] < array[min_index]:
#         min_index = count
#     if array[count] > array[max_index]:
#         max_index = count
#
#     return get_min_max_items(array, count + 1, min_index, max_index)
#
#
# def get_summa(array, min_index, max_index):
#     summa = 0
#
#     if min_index > max_index:
#         min_index, max_index = max_index, min_index
#
#     for i in range(min_index + 1, max_index):
#         summa += array[i]
#
#     return summa
#
#
# def main(min_item, max_item, size):
#     array = [random.randint(min_item, max_item) for _ in range(size)]
#     min_index, max_index = get_min_max_items(array)
#     sum_ = get_summa(array, min_index, max_index)

# print(timeit.timeit('main(1, 1000, 500)', number=100, globals=globals()))  # 0.06747861999974702
# print(timeit.timeit('main(1, 1000, 1000)', number=100, globals=globals()))  # 0.11109554399990884
# print(timeit.timeit('main(1, 1000, 2000)', number=100, globals=globals()))  # 0.25267395099945134
# print(timeit.timeit('main(1, 1000, 4000)', number=100, globals=globals()))  # 0.5517925109998032
# print(timeit.timeit('main(1, 1000, 8000)', number=100, globals=globals()))  # 1.1635526110003411
#
# cProfile.run('main(1, 1000, 500)')  #501/1    0.002    0.000    0.002    0.002 les_04_task_01.py:109(get_min_max_items)
# cProfile.run('main(1, 1000, 1000)') # 1001/1    0.001    0.000    0.001    0.001 les_04_task_01.py:109(get_min_max_items)
# cProfile.run('main(1, 1000, 2000)') # 2001/1    0.002    0.000    0.002    0.002 les_04_task_01.py:109(get_min_max_items)
# cProfile.run('main(1, 1000, 4000)') # 4001/1    0.004    0.000    0.004    0.004 les_04_task_01.py:109(get_min_max_items)
# cProfile.run('main(1, 1000, 8000)') # 8001/1    0.007    0.000    0.008    0.008 les_04_task_01.py:109(get_min_max_items)


# Вывод: первый вариант отрабатывает за линейное время, самое узкое место, кроме генерации списка - перебор списка для поиска макс. и мин. элементов.
# В варианте 2 разделил поиск макс. и мин. элемента на 2 отделные функции, но время выполнения почти не поменялось.
# 3-й вариант работает через рекурсию и показывает самое долгое время выполнения.