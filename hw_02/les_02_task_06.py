# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.


import random

MAX_COUNT = 10


def guess(answer, count=1):
    if count > MAX_COUNT:
        return f"Количество попыток закончилось. Правильный ответ {answer}"

    num = int(input("Введите ответ: "))
    if answer == num:
        return "Вы угадали!"

    if answer > num:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    return guess(answer, count + 1)


answer = random.randint(0, 100)
result = guess(answer)
print(result)
