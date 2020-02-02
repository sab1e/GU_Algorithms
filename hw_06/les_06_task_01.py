import sys


def show(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    mem = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                mem += show(key)
                mem += show(value)
        elif not isinstance(x, str):
            for item in x:
                mem += show(item)
    return mem


def version_1(SIZE_M, SIZE_N):
    mem = 0
    matrix = []
    for i in range(SIZE_M):
        sum_line = 0
        matrix.append([])
        mem += show(i)
        for j in range(SIZE_N - 1):
            # matrix[i].append(int(input(f'Введите элемент - {j + 1} строки - {i + 1}: ')))
            matrix[i].append(i + j)
            sum_line += matrix[i][j]
            mem += show(j)
        matrix[i].append(sum_line)

    # print(*matrix, sep='\n')

    vars_ = [matrix, sum_line]
    for i in vars_:
        mem += show(i)

    return mem


def version_2(SIZE_M, SIZE_N):
    mem = 0
    matrix = []
    size_m = [i for i in range(SIZE_M)]
    size_n = [i for i in range(SIZE_N - 1)]

    for i in size_m:
        sum_line = 0
        matrix.append([])
        mem += show(i)
        for j in size_n:
            # matrix[i].append(int(input(f'Введите элемент - {j + 1} строки - {i + 1}: ')))
            matrix[i].append(i + j)
            sum_line += matrix[i][j]
            mem += show(j)
        matrix[i].append(sum_line)

    # print(*matrix, sep='\n')

    vars_ = [size_m, size_n, matrix, sum_line]
    for i in vars_:
        mem += show(i)

    return mem


def version_3(SIZE_M, SIZE_N):
    mem = 0
    matrix = []
    for i in range(SIZE_M):
        matrix.append([])
        mem += show(i)
        for j in range(SIZE_N - 1):
            # matrix[i].append(int(input(f'Введите элемент - {j + 1} строки - {i + 1}: ')))
            matrix[i].append(i + j)
            mem += show(j)

    for line in matrix:
        sum_line = 0
        mem += show(line)
        for item in line:
            sum_line += item
            mem += show(item)
        line.append(sum_line)

    # print(*matrix, sep='\n')

    vars_ = [matrix, sum_line]
    for i in vars_:
        mem += show(i)

    return mem


print(version_1(5, 4))  # 1728
print(version_2(5, 4))  # 2168
print(version_3(5, 4))  # 3040


# Ubuntu 19.04 x64 Ubuntu 19.04
# Python 3.7.3 x64
# первый вариант оказался лучше, во втором варианте добавлены 2 переменные
# со списками для цикла по ним, в третьем варианте добавлены два
# дополнительных цикла для подсчета суммы строки, что привело к
# увеличению используемой памяти.