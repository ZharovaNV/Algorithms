# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
import random

size = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

max_neg = 0
max_neg_ndx = 0
for i, item in enumerate(array):
    if item < 0 and (max_neg == 0 or item > max_neg):
        max_neg = item
        max_neg_ndx = i

print(f'Максимальный отрицательный элемент {max_neg}, его позиция {max_neg_ndx}')
