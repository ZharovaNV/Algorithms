# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even = 0
odd = 0
num = input('Введите натуральное число:')
for i in num:
    if int(i) % 2:
        odd += 1
    else:
        even += 1

print(f'Четных цифр {even}')
print(f'Нечетных цифр {odd}')