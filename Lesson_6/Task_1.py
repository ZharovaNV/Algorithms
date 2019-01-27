import math
import sys


def calc_size(x):
    nsize = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                nsize += calc_size(key)
                nsize += calc_size(value)
        elif not isinstance(x, str):
            for item in x:
                nsize += calc_size(item)
    return nsize


# решето Эратосфена
def f_sieve(n_simple):
    if n_simple == 1:
        return 2

    if n_simple <= 6:
        n = n_simple * n_simple
    else:
        n = int(n_simple * math.log(n_simple) + n_simple * math.log(
            math.log(n_simple)))  # ограничение сверху на n-ое простое число nln(n) + lnln(n)
    sqrt_n = math.sqrt(n)

    sieve = [i for i in range(n)]

    sieve[1] = 0
    cnt = 1
    j = 2
    while j < n:
        sieve[j] = 0
        j += 2

    for i in range(3, n):

        if sieve[i] != 0:
            cnt += 1
            if cnt == n_simple:

                nsize = 0
                d = dict(locals())
                for item, item_value in d.items():
                    # if item[0:2] != '__' and str(type(item_value)) != '<class \'module\'>':
                    nsize += calc_size(item_value)
                print(f'Используемая память = {nsize}')
                return sieve[i]

            if sieve[i] >= sqrt_n:  # дальше проверять нет смысла
                continue

            j = i * i  # начинаем с квадрата - до этого числа уже все проверено
            while j < n:
                sieve[j] = 0
                j += 2 * i  # исключаем четные


# Метод из ДЗ - не решето
def f_not_sieve(n):
    sieve = [2]
    if n == 1:
        return 2;

    i = 2
    num = 1
    while i <= n:
        num += 2
        stop = math.sqrt(num)
        for j in sieve:
            if j <= stop:
                if num % j == 0:
                    break
        else:
            sieve.append(num)
            i += 1

    d = dict(locals())
    nsize = 0
    for item, item_value in d.items():
        # if item[0:2] != '__' and str(type(item_value)) != '<class \'module\'>':
        nsize += calc_size(item_value)
    print(f'Используемая память = {nsize}')

    return sieve[n - 1]


# метод из проверки ДЗ - не решето
def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    d = dict(locals())
    nsize = 0
    for item, item_value in d.items():
        # if item[0:2] != '__' and str(type(item_value)) != '<class \'module\'>':
        nsize += calc_size(item_value)
    print(f'Используемая память = {nsize}')

    return current_prime


print('f_sieve')
print(f'Простое число равно {f_sieve(5)}')

print('f_not_sieve')
print(f'Простое число равно {f_not_sieve(5)}')

print('prime')
print(f'Простое число равно {prime(5)}')

# В последнем примере количество используемой памяти не зависит от аргумента функции
# и равно 4 * память под целочисленные переменные(у меня равно 14 * 4)
# Решето Эратосфена самое затратный по памяти алгоритм, так как формируется список с большим запасом
# по количесвту элементов, но зато самый это наиболее быстрый алгоритм

# f_sieve
# Используемая память = 550
# Простое число равно 11
# f_not_sieve
# Используемая память = 198
# Простое число равно 11
# prime
# Используемая память = 56
# Простое число равно 11

# Python 3.7.1
# 64-разрядная система
