# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


n = int(input("Введите количество элементов ряда чисел 1, -0.5, 0.25, "
              "-0.125,…: "))

summa = 0
a = 1
i = 0

while i < n:
    summa += a
    a = a / -2
    i += 1

print(f'Сумма чисел ряда 1, -0.5, 0.25, -0.125,… из {n} элементов равна {summa}')
