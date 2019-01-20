# cd ..\..\Algorithm\Lesson_4
# python -m timeit -n 100 -s "import Task_2" "Task_2.f_sieve(100)"

import cProfile
import math


# решето Эратосфена
def f_sieve(n_simple):

    if n_simple == 1:
        return 2

    if n_simple <= 6:
        n = n_simple * n_simple
    else:
        n = int(n_simple * math.log(n_simple) + n_simple * math.log(math.log(n_simple))) # ограничение сверху на n-ое простое число nln(n) + lnln(n)
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
                return sieve[i]

            if sieve[i] >= sqrt_n:  #дальше проверять нет смысла
                continue

            j = i * i  # начинаем с квадрата - до этого числа уже все проверено
            while j < n:
                sieve[j] = 0
                j += 2 * i  # исключаем четные

# 100 loops, best of 5: 271 usec per loop   -100
# 100 loops, best of 5: 1.96 msec per loop  -500
# 100 loops, best of 5: 4.39 msec per loop  -1000
# 100 loops, best of 5: 66.4 msec per loop   -10000
# 100 loops, best of 5: 192 msec per loop  -25000


# cProfile.run('f_sieve(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_2.py:20(<listcomp>)
#         1    0.002    0.002    0.002    0.002 Task_2.py:9(f_sieve)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('f_sieve(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_2.py:17(<listcomp>)
#         1    0.004    0.004    0.004    0.004 Task_2.py:7(f_sieve)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('f_sieve(25000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.177    0.177 <string>:1(<module>)
#         1    0.018    0.018    0.018    0.018 Task_2.py:20(<listcomp>)
#         1    0.156    0.156    0.174    0.174 Task_2.py:9(f_sieve)
#         1    0.000    0.000    0.177    0.177 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('f_sieve(1000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.117    0.117   10.849   10.849 <string>:1(<module>)
#         1    1.196    1.196    1.196    1.196 Task_2.py:20(<listcomp>)
#         1    9.537    9.537   10.733   10.733 Task_2.py:9(f_sieve)
#         1    0.000    0.000   10.849   10.849 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print(f_sieve(500))








################################# Второй алгоритм и вывод  ############################################
# Алгоритм, в котором для каждого нечетного числа проверяем его делимость на ренее найденные простые числа
# Если ни на одно не делится, добавляем в список простых чисел
# В четырех версиях меняется только реализация (используемые средства), но не сам алгоритм
# Наиболее оптимальный по времени f_sieve2_v2 за счет того что проверяются не все простые числа,
# а только до квадратного корня из проверяемого числа. Однако временные завтраты на вычисление корня
# не приводят к тому, что алгортм начинает работать существенно быстрее.
# Данный алгоритм хуже решета, так как для каждого нечетного числа проверяется его делимость на все простые числа
# вместо того чтобы сразу пропускать все числа кратные ранее найденным простым числам.





def f_sieve2(n):
    # sieve = [0 for _  in range(1, n + 1)]
    sieve = [2]
    if n == 1:
        return 2;

    i = 2
    num = 1
    while i <= n:
        num += 2
        for j in sieve:
            if num % j == 0:
                break
        else:
            # sieve[i] = num
            sieve.append(num)
            i += 1

    return  sieve[n-1]


# 100 loops, best of 5: 606 usec per loop   -100
# 100 loops, best of 5: 13.4 msec per loop  -500
# 100 loops, best of 5: 53.8 msec per loop  -1000

# cProfile.run('f_sieve2(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.015    0.015    0.015    0.015 Task_2.py:89(f_sieve2)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#       499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('f_sieve2(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   10.531   10.531 <string>:1(<module>)
#         1   10.528   10.528   10.531   10.531 Task_2.py:89(f_sieve2)
#         1    0.000    0.000   10.531   10.531 {built-in method builtins.exec}
#      9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def f_sieve2_v2(n):
    # sieve = [0 for _  in range(1, n + 1)]
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
            # sieve[i] = num
            sieve.append(num)
            i += 1

    return  sieve[n-1]

# 100 loops, best of 5: 739 usec per loop   -100
# 100 loops, best of 5: 12.9 msec per loop  -500
# 100 loops, best of 5: 47.2 msec per loop  -1000
# 100 loops, best of 5: 178 msec per loop   -2000

# cProfile.run('f_sieve2_v2(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.015    0.015    0.015    0.015 Task_2.py:118(f_sieve2_v2)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#      1785    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#       499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('f_sieve2_v2(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.454    6.454 <string>:1(<module>)
#         1    6.437    6.437    6.454    6.454 Task_2.py:132(f_sieve2_v2)
#         1    0.000    0.000    6.454    6.454 {built-in method builtins.exec}
#     52364    0.015    0.000    0.015    0.000 {built-in method math.sqrt}
#      9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('f_sieve2_v2(25000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   46.048   46.048 <string>:1(<module>)
#         1   45.994   45.994   46.047   46.047 Task_2.py:132(f_sieve2_v2)
#         1    0.000    0.000   46.048   46.048 {built-in method builtins.exec}
#    143558    0.047    0.000    0.047    0.000 {built-in method math.sqrt}
#     24999    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# генерация списка [val for val in sieve if val <= stop] вместо if сильно замедляет работу
def f_sieve2_v3(n):
    # sieve = [0 for _  in range(1, n + 1)]
    sieve = [2]
    if n == 1:
        return 2;

    i = 2
    num = 1
    while i <= n:
        num += 2
        stop = math.sqrt(num)
        for j in [val for val in sieve if val <= stop]:
            if num % j == 0:
                break
        else:
            # sieve[i] = num
            sieve.append(num)
            i += 1

    return  sieve[n-1]

# 100 loops, best of 5: 1.84 msec per loop  -100
# 100 loops, best of 5: 185 msec per loop   -1000



def f_sieve2_v4(n):
    sieve = [n] * n
    # sieve = [2]
    sieve[0] = 2
    if n == 1:
        return 2;

    i = 1
    num = 1
    while i < n:
        num += 2
        stop = math.sqrt(num)
        for j in sieve:
            if j <= stop:
                if num % j == 0:
                    break
        else:
            sieve[i] = num
            # sieve.append(num)
            i += 1

    return  sieve[n-1]

# 100 loops, best of 5: 1.13 msec per loop  -100
# 100 loops, best of 5: 85.1 msec per loop  -1000

# cProfile.run('f_sieve2_v4(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.028    0.028 <string>:1(<module>)
#         1    0.028    0.028    0.028    0.028 Task_2.py:172(f_sieve2_v4)
#         1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#      1785    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# print(f_sieve2_v4(500))