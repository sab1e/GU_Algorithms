# Определить, является ли год, который ввел пользователь, високосным
# или не високосным.

y = int(input("Введите год для определения високосный он или нет: "))

if y % 4 == 0:
    if y % 100 != 0:
        print("Год високосный")
    elif y % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")
else:
    print("Год не високосный")
