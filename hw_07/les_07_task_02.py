# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    arr_left = merge_sort(array[:mid])
    arr_right = merge_sort(array[mid:])

    return merge_array(arr_left, arr_right)


def merge_array(arr_left, arr_right):
    merged_array = []
    while len(arr_left) > 0 and len(arr_right) > 0:
        if arr_left[0] < arr_right[0]:
            merged_array.append(arr_left.pop(0))
        elif arr_left[0] > arr_right[0]:
            merged_array.append(arr_right.pop(0))
        else:
            merged_array.append(arr_left.pop(0))
            merged_array.append(arr_right.pop(0))

    merged_array.extend(arr_left) if len(
        arr_left) > 0 else merged_array.extend(arr_right)

    return merged_array


ITEMS = 10

array = [random.uniform(0, 50) for _ in range(ITEMS)]
print(array)
print(merge_sort(array))
