# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

SIZE_M = 5
SIZE_N = 4

matrix = []

for i in range(SIZE_M):
    sum_line = 0
    matrix.append([])
    for j in range(SIZE_N - 1):
        matrix[i].append(int(input(f'Введите элемент - {j + 1} строки - {i + 1}: ')))
        sum_line += matrix[i][j]
    matrix[i].append(sum_line)

# или как на занятии отдельными циклами посчитать сумму строк
# for line in matrix:
#     sum_line = 0
#     for item in line:
#         sum_line += item
#     line.append(sum_line)

print(*matrix, sep='\n')
