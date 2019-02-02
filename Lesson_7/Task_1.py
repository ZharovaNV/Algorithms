import random


def bubble_sort_desc(array):
    n = 1
    not_sorted = True
    while n < len(array) and not_sorted is True:
        not_sorted = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                not_sorted = True

        n += 1
        # print(array)


n = int(input('Введите длину массива'))
array = [random.randint(-100, 100) for _ in range(n)]
print(array)
bubble_sort_desc(array)
print(array)
