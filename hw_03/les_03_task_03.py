# массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

import random

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_index = 0
max_index = 0

for i in range(len(array)):
    if array[i] < array[min_index]:
        min_index = i
    if array[i] > array[max_index]:
        max_index = i

min_num = array[min_index]

array[min_index] = array[max_index]
array[max_index] = min_num

print(array)
