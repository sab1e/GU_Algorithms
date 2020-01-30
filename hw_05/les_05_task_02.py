# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque

hex_1 = list(input('Введите 1-е шестнадцатеричное число: '))
hex_2 = list(input('Введите 2-е шестнадцатеричное число: '))

corr_input = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8,
              '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
corr_output = {v: k for k, v in corr_input.items()}

deq_hex_1 = deque(corr_input[num] for num in hex_1)
deq_hex_2 = deque(corr_input[num] for num in hex_2)

if len(deq_hex_1) != len(deq_hex_2):
    if len(deq_hex_1) < len(deq_hex_2):
        deq_hex_1, deq_hex_2 = deq_hex_2, deq_hex_1
    diff_ = len(deq_hex_1) - len(deq_hex_2)
    for _ in range(diff_):
        deq_hex_2.appendleft(0)

sum_hex = deque()
k = 0
DIGIT = 16
MAX_INDEX = 15

for _ in range(len(deq_hex_1)):
    sum_el = deq_hex_1.pop() + deq_hex_2.pop() + k
    k = 0

    if sum_el > MAX_INDEX:
        sum_el -= DIGIT
        k = 1

    sum_hex.appendleft(sum_el)

if k == 1:
    sum_hex.appendleft(k)

sum_result = [corr_output[item] for item in sum_hex]
print(f'Сумма шестнадцатеричных чисел равна: {sum_result}')
