# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_ITEM = 2
END_ITEM = 100
START_ITEM_DIV = 2
END_ITEM_DIV = 10
N = 8

count = [0] * N

for i in range(START_ITEM, END_ITEM):
    for j in range(START_ITEM_DIV, END_ITEM_DIV):
        if i % j == 0:
            count[j - 2] += 1

for i, item in enumerate(count):
    print(f'{i + 2} - {item}')
