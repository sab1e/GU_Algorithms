# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = 1

array = [random.randint (MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_index = 0
max_index = 0

for i in range(len(array)):
    if array[i] < array[min_index]:
        min_index = i
    if array[i] > array[max_index]:
        max_index = i

summa = 0

if min_index > max_index:
    min_index, max_index = max_index, min_index

for i in range(min_index + 1, max_index):
    summa += array[i]

if summa == 0:
    print('между максимальным и минимальным элементом нет других элементов')
else:
    print(f'Сумма элементов между минимальным и максимальным элементами - {summa}')
