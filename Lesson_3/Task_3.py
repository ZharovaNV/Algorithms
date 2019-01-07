# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

size = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

min_tmp = array[0]
max_tmp = array[0]
min_ndx_tmp = 0
max_ndx_tmp = 0
for i, item in enumerate(array):
    if item < min_tmp:
        min_tmp = item
        min_ndx_tmp = i
    if item > max_tmp:
        max_tmp = item
        max_ndx_tmp = i

array[min_ndx_tmp], array[max_ndx_tmp] = array[max_ndx_tmp], array[min_ndx_tmp]
print(array)
