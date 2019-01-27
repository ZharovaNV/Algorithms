# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque
import random

SYSNUM = 16
SYSDICT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
           "D": 13, "E": 14, "F": 15}
SYSDICTKEYS = list(SYSDICT.keys())


def sum_hex(a, b):
    a.reverse()
    b.reverse()
    sum_ = deque()
    intpart = 0

    if a.__len__() < b.__len__():
        a, b = b, a
    max_len = a.__len__()

    b.extend('0' * (max_len - b.__len__()))

    for i in range(max_len):
        sum_.append(SYSDICTKEYS[(SYSDICT[a[i]] + SYSDICT[b[i]] + intpart) % SYSNUM])
        intpart = (SYSDICT[a[i]] + SYSDICT[b[i]] + intpart) // SYSNUM

    if intpart != 0:
        sum_.append(str(intpart))

    sum_.reverse()
    a.reverse()
    b.reverse()
    i = 0
    while i < b.__len__() and b[i] == '0':
        b.popleft()
        i += 1
    return sum_


def prod_hex(a, b):
    a.reverse()
    b.reverse()
    prod_ = deque()
    tot_prod = deque()
    intpart = 0
    if a.__len__() < b.__len__():
        a, b = b, a

    for i in range(b.__len__()):
        prod_.clear()
        intpart = 0
        for j in range(a.__len__()):
            prod_.append((SYSDICT[a[j]] * SYSDICT[b[i]] + intpart) % SYSNUM)
            intpart = (SYSDICT[a[j]] * SYSDICT[b[i]] + intpart) // SYSNUM
        if intpart != 0:
            prod_.append(intpart)

        intpart = 0
        for j in range(prod_.__len__()):
            if j + i >= tot_prod.__len__():
                tot_prod.append((prod_[j] + intpart) % SYSNUM)
                intpart = (prod_[j] + intpart) // SYSNUM
            else:
                num_tmp = (tot_prod[j + i] + prod_[j] + intpart) % SYSNUM
                intpart = (tot_prod[j + i] + prod_[j] + intpart) // SYSNUM
                tot_prod[j + i] = num_tmp
        if intpart != 0:
            tot_prod.append(intpart)

    tot_prod.reverse()
    for i, s in enumerate(tot_prod):
        # print(i, s)
        tot_prod[i] = SYSDICTKEYS[s]
    a.reverse()
    b.reverse()
    return tot_prod


def main():
    a = deque(input('Введите первое число').upper())

    # a = deque('a2'.upper())
    # b = deque('c4f'.upper())
    is_correct = True
    for s in a:
        if SYSDICT.get(s) == None:
            is_correct = False
    if is_correct == False:
        print(f'Первое число не в шестнадцатеричной системе счисления')
        return

    b = deque(input('Введите второе число').upper())
    for s in b:
        if SYSDICT.get(s) == None:
            is_correct = False
    if is_correct == False:
        print(f'Первое число не в шестнадцатеричной системе счисления')
        return

    print(f'Сумма чисел равна {list(sum_hex(a, b))}')
    print(f'Произведеление чисел равно {list(prod_hex(a, b))}')


main()


def testf():
    for i in range(1000):
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)

        assert deque(hex(a + b)[2:].upper()) == sum_hex(deque(hex(a)[2:].upper()), deque(hex(b)[2:].upper())) and \
               deque(hex(a * b)[2:].upper()) == prod_hex(deque(hex(a)[2:].upper()), deque(hex(b)[2:].upper())), \
            f'Тест {i} не пройден a = {a}, b = {b}'
        print(f'Тест {i} пройден a = {a}, b = {b}')

# testf()
