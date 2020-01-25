# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный
# отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = -100

array = [random.randint (MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative_index = -1

for i in range(len(array)):
    if array[i] < 0 and (max_negative_index == -1 or
                         array[i] > array[max_negative_index]):
        max_negative_index = i

if max_negative_index == -1:
    print('отрицательных элементов нет')
else:
    print(f'Максимальный отрицательный элемент: {array[max_negative_index]} '
          f'с индексом: {max_negative_index}')
