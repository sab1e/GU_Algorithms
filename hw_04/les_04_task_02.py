import timeit
import cProfile

# Вариант 1 Без использования «Решета Эратосфена»
def prime(n):
    l = 20 * n  # размер первоночального массива
    lst = [2]
    for i in range(3, l + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[n - 1]


# print(timeit.timeit('prime(1000)', number=100, globals=globals()))  # 0.8596315700051491
# print(timeit.timeit('prime(2000)', number=100, globals=globals()))  # 1.95678307399794
# print(timeit.timeit('prime(4000)', number=100, globals=globals()))  # 4.728673361998517

cProfile.run('prime(1000)')
# 1    0.013    0.013    0.013    0.013 les_04_task_02.py:5(prime)


# Вариант 2 с использованием алгоритма «Решето Эратосфена»
def get_seive_pos(n):
    l = 20 * n  # размер первоночального массива
    sieve = [i for i in range(l)]
    sieve[1] = 0

    for i in range(2, l):
        if sieve[i] != 0:
            j = i + i
            while j < l:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    return res[n - 1]


# print(timeit.timeit('get_seive_pos(1000)', number=100, globals=globals()))  # 0.502677151998796
# print(timeit.timeit('get_seive_pos(2000)', number=100, globals=globals()))  # 0.9714353429990297
# print(timeit.timeit('get_seive_pos(4000)', number=100, globals=globals()))  # 1.9931788780013449

# cProfile.run('get_seive_pos(1000)')
# 1    0.001    0.001    0.001    0.001 les_04_task_02.py:17(<listcomp>)
# 1    0.006    0.006    0.007    0.007 les_04_task_02.py:5(get_seive_pos)
# 1    0.001    0.001    0.001    0.001 les_04_task_02.py:7(<listcomp>)


# Вывод: оба варианта имеют линейную зависимость, алгоритм «Решето Эратосфена» работает быстрее.