import random


def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array) // 2

    left = merge_sort(array[:m])
    right = merge_sort(array[m:])

    i = 0
    j = 0
    total = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            total.append(left[i])
            i += 1
        elif left[i] >= right[j]:
            total.append(right[j])
            j += 1
        else:
            raise Exception('Случилось чудо!')
    if i < len(left):
        for k in range(i, len(left)):
            total.append(left[k])
    if j < len(right):
        for k in range(j, len(right)):
            total.append(right[k])
    return total


n = int(input('Введите длину массива'))
array = [round(random.random() * 50, 2) for _ in range(n)]
print(array)
new_array = merge_sort(array)
print(new_array)
