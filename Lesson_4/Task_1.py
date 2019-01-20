# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба являться минимальными), так и различаться.

# python -m timeit -n 100 -s "import Task_1" "Task_1.main(10)"

import random
import timeit
import cProfile

# вариант из сданного ДЗ
def two_min(array):
    min_num = min_num_prev = min_item_prev = float('inf')
    for item in array:
        if item < min_num:
            if min_item_prev < min_num_prev:
                min_num_prev = min_item_prev
            min_num = item
            min_item_prev = item
        else:
            if item < min_num_prev:
                min_num_prev = item
    return min_num, min_num_prev

# 100 loops, best of 5: 31.7 usec per loop  -10
# 100 loops, best of 5: 271 usec per loop   -100
# 100 loops, best of 5: 2.76 msec per loop  -1000

# cProfile.run('main(100000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.365    0.365 <string>:1(<module>)
#         1    0.000    0.000    0.365    0.365 Task_1.py:61(main)
#         1    0.051    0.051    0.350    0.350 Task_1.py:65(<listcomp>)
#         1    0.015    0.015    0.015    0.015 Task_1.py:8(two_min)                 0.015 Task_1.py:8(two_min)
#    100000    0.121    0.000    0.253    0.000 random.py:174(randrange)
#    100000    0.046    0.000    0.300    0.000 random.py:218(randint)
#    100000    0.098    0.000    0.132    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.365    0.365 {built-in method builtins.exec}
#    100000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126682    0.025    0.000    0.025    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('main(1000000)')
  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.002    0.002    3.826    3.826 <string>:1(<module>)
  #       1    0.000    0.000    3.824    3.824 Task_1.py:120(main)
  #       1    0.529    0.529    3.690    3.690 Task_1.py:124(<listcomp>)
  #       1    0.134    0.134    0.134    0.134 Task_1.py:8(two_min)            0.134 Task_1.py:8(two_min)
  # 1000000    1.324    0.000    2.686    0.000 random.py:174(randrange)
  # 1000000    0.475    0.000    3.161    0.000 random.py:218(randint)
  # 1000000    1.017    0.000    1.362    0.000 random.py:224(_randbelow)
  #       1    0.000    0.000    3.826    3.826 {built-in method builtins.exec}
  # 1000000    0.089    0.000    0.089    0.000 {method 'bit_length' of 'int' objects}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  # 1267674    0.257    0.000    0.257    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main(10000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.018    0.018   36.946   36.946 <string>:1(<module>)
#         1    1.315    1.315    1.315    1.315 Task_1.py:11(two_min)          1.315 Task_1.py:11(two_min)
#         1    0.000    0.000   36.928   36.928 Task_1.py:247(main)
#         1    5.077    5.077   35.613   35.613 Task_1.py:251(<listcomp>)
#  10000000   12.589    0.000   25.854    0.000 random.py:174(randrange)
#  10000000    4.682    0.000   30.536    0.000 random.py:218(randint)
#  10000000    9.966    0.000   13.264    0.000 random.py:224(_randbelow)
#         1    0.000    0.000   36.946   36.946 {built-in method builtins.exec}
#  10000000    0.843    0.000    0.843    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12672015    2.456    0.000    2.456    0.000 {method 'getrandbits' of '_random.Random' objects}



# два последовательных просмотра - долгий алгоритм изза использования lambda, см two_min2_v2 без lambda ниже
def two_min2(array):
    indx_min = 0
    for i in range(len(array)):
        if array[i] < array[indx_min]:
            indx_min = i

    if indx_min == 0:
        indx_min_prev = 1
    else:
        indx_min_prev = 0

    for i in filter(lambda j: j != indx_min, range(len(array))):
        if array[i] < array[indx_min_prev]:
            indx_min_prev = i

    return array[indx_min], array[indx_min_prev]

# 100 loops, best of 5: 36.2 usec per loop  -10
# 100 loops, best of 5: 322 usec per loop   -100
# 100 loops, best of 5: 3.28 msec per loop  -100

# cProfile.run('main(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.428    0.428 <string>:1(<module>)
#         1    0.000    0.000    0.428    0.428 Task_1.py:161(main)
#         1    0.049    0.049    0.355    0.355 Task_1.py:165(<listcomp>)
#         1    0.058    0.058    0.073    0.073 Task_1.py:58(two_min2)       # 0.073  время затраченное на two_min2
#    100000    0.015    0.000    0.015    0.000 Task_1.py:69(<lambda>)
#    100000    0.128    0.000    0.260    0.000 random.py:174(randrange)
#    100000    0.046    0.000    0.306    0.000 random.py:218(randint)
#    100000    0.099    0.000    0.132    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.428    0.428 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    100000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126882    0.025    0.000    0.025    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('main(1000000)')
  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.002    0.002    4.476    4.476 <string>:1(<module>)
  #       1    0.570    0.570    0.727    0.727 Task_1.py:40(two_min2)      # 0.727  время затраченное на two_min2
  # 1000000    0.157    0.000    0.157    0.000 Task_1.py:47(<lambda>)
  #       1    0.000    0.000    4.474    4.474 Task_1.py:88(main)
  #       1    0.554    0.554    3.748    3.748 Task_1.py:92(<listcomp>)
  # 1000000    1.327    0.000    2.717    0.000 random.py:174(randrange)
  # 1000000    0.477    0.000    3.194    0.000 random.py:218(randint)
  # 1000000    1.041    0.000    1.389    0.000 random.py:224(_randbelow)
  #       1    0.000    0.000    4.476    4.476 {built-in method builtins.exec}
  #       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
  # 1000000    0.089    0.000    0.089    0.000 {method 'bit_length' of 'int' objects}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  # 1267297    0.260    0.000    0.260    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('main(10000000)')
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.017    0.017   43.974   43.974 <string>:1(<module>)
 #        1    0.000    0.000   43.957   43.957 Task_1.py:103(main)
 #        1    5.349    5.349   36.608   36.608 Task_1.py:107(<listcomp>)
 #        1    5.791    5.791    7.349    7.349 Task_1.py:40(two_min2)          # 7.349  время затраченное на two_min2
 # 10000000    1.559    0.000    1.559    0.000 Task_1.py:47(<lambda>)
 # 10000000   13.144    0.000   26.543    0.000 random.py:174(randrange)
 # 10000000    4.716    0.000   31.259    0.000 random.py:218(randint)
 # 10000000   10.047    0.000   13.399    0.000 random.py:224(_randbelow)
 #        1    0.000    0.000   43.974   43.974 {built-in method builtins.exec}
 #        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
 # 10000000    0.871    0.000    0.871    0.000 {method 'bit_length' of 'int' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 # 12672849    2.480    0.000    2.480    0.000 {method 'getrandbits' of '_random.Random' objects}



# два пследовательных просмотра без lambda
def two_min2_v2(array):
    indx_min = 0
    for i in range(len(array)):
        if array[i] < array[indx_min]:
            indx_min = i

    if indx_min == 0:
        indx_min_prev = 1
    else:
        indx_min_prev = 0

    for i in range(len(array)):
        if array[i] < array[indx_min_prev] and i != indx_min:
            indx_min_prev = i

    return array[indx_min], array[indx_min_prev]

# 100 loops, best of 5: 34 usec per loop
# 100 loops, best of 5: 306 usec per loop
# 100 loops, best of 5: 3.08 msec per loop




# cProfile.run('main(100000)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.400    0.400 <string>:1(<module>)
   #      1    0.034    0.034    0.034    0.034 Task_1.py:130(two_min2_v2)           0.034 Task_1.py:130(two_min2_v2)
   #      1    0.000    0.000    0.399    0.399 Task_1.py:161(main)
   #      1    0.051    0.051    0.366    0.366 Task_1.py:165(<listcomp>)
   # 100000    0.131    0.000    0.268    0.000 random.py:174(randrange)
   # 100000    0.048    0.000    0.315    0.000 random.py:218(randint)
   # 100000    0.103    0.000    0.137    0.000 random.py:224(_randbelow)
   #      1    0.000    0.000    0.400    0.400 {built-in method builtins.exec}
   #      2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   # 100000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   # 126732    0.025    0.000    0.025    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main(100000)')
  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.002    0.002    3.959    3.959 <string>:1(<module>)
  #       1    0.335    0.335    0.335    0.335 Task_1.py:130(two_min2_v2)              0.335 Task_1.py:130(two_min2_v2)
  #       1    0.000    0.000    3.957    3.957 Task_1.py:176(main)
  #       1    0.521    0.521    3.622    3.622 Task_1.py:180(<listcomp>)
  # 1000000    1.274    0.000    2.623    0.000 random.py:174(randrange)
  # 1000000    0.478    0.000    3.101    0.000 random.py:218(randint)
  # 1000000    1.002    0.000    1.349    0.000 random.py:224(_randbelow)
  #       1    0.000    0.000    3.959    3.959 {built-in method builtins.exec}
  #       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
  # 1000000    0.089    0.000    0.089    0.000 {method 'bit_length' of 'int' objects}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  # 1268258    0.259    0.000    0.259    0.000 {method 'getrandbits' of '_random.Random' objects}


# сортировка массива функцией sorted
def two_min3(array):
    array = sorted(array)
    return array[0], array[1]

# 100 loops, best of 5: 28.5 usec per loop  -10
# 100 loops, best of 5: 273 usec per loop   -100
# 100 loops, best of 5: 2.79 msec per loop  -1000


# cProfile.run('main(100000)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.361    0.361 <string>:1(<module>)
   #      1    0.000    0.000    0.015    0.015 Task_1.py:180(two_min3)           0.015 Task_1.py:180(two_min3)
   #      1    0.000    0.000    0.361    0.361 Task_1.py:192(main)
   #      1    0.049    0.049    0.346    0.346 Task_1.py:196(<listcomp>)
   # 100000    0.120    0.000    0.251    0.000 random.py:174(randrange)
   # 100000    0.046    0.000    0.297    0.000 random.py:218(randint)
   # 100000    0.098    0.000    0.131    0.000 random.py:224(_randbelow)
   #      1    0.000    0.000    0.361    0.361 {built-in method builtins.exec}
   #      1    0.015    0.015    0.015    0.015 {built-in method builtins.sorted}
   # 100000    0.008    0.000    0.008    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   # 126737    0.025    0.000    0.025    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main(1000000)')
  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.002    0.002    3.851    3.851 <string>:1(<module>)
  #       1    0.000    0.000    0.158    0.158 Task_1.py:180(two_min3)           0.158 Task_1.py:180(two_min3)
  #       1    0.003    0.003    3.849    3.849 Task_1.py:204(main)
  #       1    0.521    0.521    3.688    3.688 Task_1.py:208(<listcomp>)
  # 1000000    1.319    0.000    2.691    0.000 random.py:174(randrange)
  # 1000000    0.476    0.000    3.168    0.000 random.py:218(randint)
  # 1000000    1.031    0.000    1.372    0.000 random.py:224(_randbelow)
  #       1    0.000    0.000    3.851    3.851 {built-in method builtins.exec}
  #       1    0.158    0.158    0.158    0.158 {built-in method builtins.sorted}
  # 1000000    0.088    0.000    0.088    0.000 {method 'bit_length' of 'int' objects}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  # 1266991    0.253    0.000    0.253    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main(10000000)')
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.017    0.017   38.105   38.105 <string>:1(<module>)
 #        1    0.000    0.000    1.571    1.571 Task_1.py:180(two_min3)      1.571 Task_1.py:180(two_min3)
 #        1    0.030    0.030   38.087   38.087 Task_1.py:223(main)
 #        1    5.155    5.155   36.486   36.486 Task_1.py:227(<listcomp>)
 # 10000000   13.194    0.000   26.659    0.000 random.py:174(randrange)
 # 10000000    4.672    0.000   31.331    0.000 random.py:218(randint)
 # 10000000   10.099    0.000   13.465    0.000 random.py:224(_randbelow)
 #        1    0.000    0.000   38.105   38.105 {built-in method builtins.exec}
 #        1    1.571    1.571    1.571    1.571 {built-in method builtins.sorted}
 # 10000000    0.866    0.000    0.866    0.000 {method 'bit_length' of 'int' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 # 12675896    2.501    0.000    2.501    0.000 {method 'getrandbits' of '_random.Random' objects}


def main(size):
    # size = 10
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    two_min3(array)


    # print(array)
    # print(two_min(array))
    # print(two_min2(array))
    # print(two_min2_v2(array))
    # print(two_min3(array))

# main(10)

# cProfile.run('main(10000000)')


################## Вывод ###############################
# Судя по cProfile наибольшая часть времени тратится на формирование списка, а не на нахождение минимальных значений
# Поэтому при оценке времени при использовании timeit корректнее вычитать время, затраченные на формирование списка
# При этом при анализе cProfile можно ориентироваться сразу на время затраченные навызов функций two_min.
#
# Первый алгоритм имеет асимтотику O(n), так как ищет два минимальных значения за одно прохождение по массиву
# Второй алгорит требует два прохождения, но поскольку O(2 * n -1) = O(n), то асимтотически он не отличается от первого,
# хотя времени тратится в два раза больше - см. two_min2_v2 (two_min2 без v2 это реализоция через lambda функцию,
# которая оказалась очень затратной по времени, так как отрабатывает при каждой итерации цикла).
# Третий алгортм - стандартная сортировка функцией sorted.
# Согласно данным в интернете в ней используется алгоритм TimSort с асимпотитикой O(nln(n)).
# Временные показатели это подтверждают
