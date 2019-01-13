# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба являться минимальными), так и различаться.
import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

min_num = max_item  # любое число, превосходящее все элементы массива
min_num_prev = max_item
min_item_prev = max_item
for item in array:
    if item < min_num:
        if min_item_prev < min_num_prev:
            min_num_prev = min_item_prev
        min_num = item
        min_item_prev = item
    else:
        if item < min_num_prev:
            min_num_prev = item

print(min_num, min_num_prev)
