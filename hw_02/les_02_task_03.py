# Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите целое число: '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)

# num = input("Введите натурально число: ")
#
# num_reverse = ''
#
# for i in num:
#     num_reverse = i + num_reverse
#
# print(f'Обратное по порядку числа {num} будет {num_reverse}')
