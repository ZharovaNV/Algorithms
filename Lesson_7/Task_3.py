import random


# Идем последовательно по массиву.
# Считаем сколько элементов меньше первого элемента.
# Если их количество равно m (точнее из-за повторяющихся элементом проверка будет чуть сложнее),
# то нашли медиану,
# иначе, если количество менее m, то находим следующий бОльший элемент,
# если количесвто больше m, то находим следующий меньший элемент,
# и для него повторяем вычисления

def get_median(array, m):
    i = 0
    while i < len(array):
        indx_tmp = i
        j = 0
        less = 0
        equal = 0
        nflag = 0
        while j < len(array):
            if j != indx_tmp:
                if array[j] < array[indx_tmp]:
                    less += 1
                elif array[j] == array[indx_tmp]:
                    equal += 1
                if less > m:
                    nflag = 1
                    break
            j += 1

        if less <= m and less + equal >= m:  # нашли медиану
            return array[indx_tmp]

        if i < len(array):
            i += 1
        if nflag == 0:
            while i < len(array) and array[i] < array[indx_tmp]:
                i += 1
        else:
            while i < len(array) and array[i] >= array[indx_tmp]:
                i += 1
    return array[indx_tmp]


def gnome_sort(array):
    i = 1
    j = 2
    while i < len(array):
        if array[i - 1] < array[i]:
            i = j
            j += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1


m = int(input('Введите m (длина массива будет 2m+1)'))
array = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print(array)
print(f'Медиана = {get_median(array, m)}')

print('*' * 10, 'Проверка гномьей сортировкой', '*' * 10)
gnome_sort(array)
print(array)
print(f'Медиана = {array[m]}')
