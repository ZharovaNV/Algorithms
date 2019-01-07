# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

FIRST = 32
SECOND = 127
COL = 10
for i in range((SECOND - FIRST) // COL + 1):
    result = ''
    for j in range(10):
        if FIRST + i * COL + j <= SECOND:
            result += str(FIRST + i * COL + j).ljust(3, ' ') + ' - "' + chr(FIRST + i * COL + j) + '"   '
    print(result)
