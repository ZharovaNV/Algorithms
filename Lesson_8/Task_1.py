# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

def substr_count(main_str):
    substr_cnt = 0
    for len_sub in range(1, len(main_str)):
        h_list = []
        for pos in range(len(main_str) - len_sub + 1):
            h_sub = hash(main_str[pos:pos + len_sub])
            if h_sub not in h_list:
                h_list.append(h_sub)
        substr_cnt += len(h_list)
    return substr_cnt


s = input('Введите строку: ')
print(f'Количество различных подстрок в строке {s} равно {substr_count(s)}')
