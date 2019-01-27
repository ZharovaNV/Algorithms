# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import namedtuple
from collections import defaultdict

n = int(input('Введите количество предприятий'))
stat = namedtuple('stat', 'name q1 q2 q3 q4')
stat_comp = defaultdict(float)
avg = 0
for _ in range(n):
    data = input('Введите наименование организации и прибыль за 4 квартала через пробел')
    # не пишу обработчик ошибок так как договорились, что пользователь идеальный
    comp = stat._make(data.split())
    stat_comp[comp.name] = float(comp.q1) + float(comp.q2) + float(comp.q3) + float(comp.q4)
    avg += stat_comp[comp.name]

avg = avg / len(stat_comp)
print(f'Средняя прибыль равна {avg:.2f}')

flag = 0
flag2 = 0
for name, val in sorted(stat_comp.items(), key=lambda t: t[1], reverse=True):
    if val > avg:
        if flag == 0:
            print('Наименования предприятий, чья прибыль выще среднего')
            flag = 1
        print(name)
    if val < avg:
        if flag2 == 0:
            print('Наименования предприятий, чья прибыль ниже среднего')
            flag2 = 1
        print(name)
