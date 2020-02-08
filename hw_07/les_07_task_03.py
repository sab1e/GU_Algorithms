# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его
# на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).


import random


def median_search(array):
    for i in range(len(array)):
        lt_pivot = 0
        gt_pivot = 0
        eq_pivot = 0
        for j in range(len(array)):
            if i != j:
                if array[j] > array[i]:
                    gt_pivot += 1
                elif array[j] < array[i]:
                    lt_pivot += 1
                else:
                    eq_pivot += 1

        if eq_pivot != 0:
            if lt_pivot > gt_pivot:
                lt_pivot, gt_pivot = gt_pivot, lt_pivot

            diff = gt_pivot - lt_pivot

            if diff <= eq_pivot:
                eq_pivot -= diff
                lt_pivot += diff

        if lt_pivot == gt_pivot or lt_pivot == gt_pivot == eq_pivot:
            return array[i]

    return 'not found'


M = 5
START_ITEM = 0
END_ITEM = 100

items = 2 * M + 1

array = [random.randint(START_ITEM, END_ITEM) for _ in range(0, items)]
random.shuffle(array)
print(array)
print(f'медиана: {median_search(array)}')
