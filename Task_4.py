# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

letter1 = input('Введите первую букву')
letter2 = input('Введите вторую букву')

place1 = ord(letter1) - ord('a') + 1
place2 = ord(letter2) - ord('a') + 1
if place1 > place2 + 1:
    dif = place1 - place2 - 1
elif place2 > place1 + 1:
    dif = place2 - place1 - 1
else:
    dif = 0

print(f'Буква {letter1} на месте {place1}, буква {letter2} на месте {place2}, между ними {dif} букв (невключительно)')
