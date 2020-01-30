# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего
# и ниже среднего.

from collections import defaultdict

QR = 4

company_total = defaultdict(list)
total_profit = 0

company_count = int(input('Введите количество предприятий: '))

for _ in range(company_count):
    company_name = input('Введите наименование предприятия: ')
    y_profit = 0
    for i in range(QR):
        q_profit = float(input(f'Введите прибыль за {i + 1}-й квартал: '))
        company_total[company_name].append(q_profit)
        y_profit += q_profit
    company_total[company_name].append(y_profit)
    total_profit += y_profit

avrg = total_profit / company_count
print(f'Средняя прибыль составляет {avrg}')

print('\nКомпании чья прибыль выше среднего: ')
for company_name in company_total:
    if company_total[company_name][4] >= avrg:
        print(company_name)

print('\nКомпании чья прибыль ниже среднего: ')
for company_name in company_total:
    if company_total[company_name][4] < avrg:
        print(company_name)
