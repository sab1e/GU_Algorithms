# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MAX_ITEM = 10
MIN_ITEM = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num = array[0]
max_count = 0

for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            count += 1
    if count > max_count:
        max_num = array[i]
        max_count = count

if max_count > 1:
    print(f'число {max_num} встречается {max_count } раз(а)')
else:
    print(f'числа не повторяются')
