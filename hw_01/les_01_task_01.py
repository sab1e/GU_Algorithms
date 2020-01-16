# https://drive.google.com/file/d/1HOhB3jMGJm0DOq4D3HBFfwRh3iuEkCAJ/view?usp=sharing


# Найти сумму и произведение цифр трехзначного числа, которое вводит
# пользователь.

a = int(input('Введите трехзначное число: '))

a1 = a // 100
a2 = (a // 10) % 10
a3 = a % 10

sum = a1 + a2 + a3
mult = a1 * a2 * a3

print(f'Сумма цифр числа {a} равна {sum}')
print(f'Произведение цифр числа {a} равна {mult}')
