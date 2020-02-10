# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.


import hashlib


def search_substr(str):

    sub_str = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1 if i != 0 else len(str)):
            sub_hash = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
            sub_str.add(sub_hash)

    return len(sub_str)


print(search_substr('ab c'))
