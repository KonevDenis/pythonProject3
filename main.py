##1)Считать названия объектов, даты и звездные величины из файла.
def jdn(jdn): #функция, которая переводит из юлин. в григор. дату
    c = (jdn + 32082)//1
    d = (4*c+3)//1461
    e = c - (1461*d)//4
    m = (5*e+2)//153
#

    month = m + 3 - 12*(m//10)
    year = d - 4800 + (m//10)
    hour0 = jdn%1*60
    hour = hour0-hour0%1 + 12
    if hour > 24: # если часов в дне получилось больше 24, то прибавляем сутки
        day = e - ((153 * m + 2) // 5) + 2
        ptp = hour - 24
    else:
        day = e - ((153 * m + 2) // 5) + 1
    minute0 = hour0%1*60
    minute = minute0 - minute0%1
    second0 = minute0%1*60
    second = second0 - second0%1
    return f'{int(day)}.{int(month)}.{int(year)} {int(ptp)}.{int(minute)}.{int(second)}'
f = open('task2_data.dat', 'r')  # открываем файл
stars = f.read().split('\n')  # считываем весь файл, разделяя по переходам строк (используем именно read, потому что readline и readlines создают списки)

#2)Вывести на экран имена объетов, присутствующих в каталоге (без дублей!!!) и фильтров,в которых есть данные для тех или иных объектов.
item = []  # временный массив # item - записи, котрорые будем использовать input_data - входные данные
for input_data in stars:  # перебираем все ряды
    item.append(input_data.split())  # разделяем ряды по пробелам
item = item[1:]  # удаляем первое значение (заголовки)
#ПРО СРЕЗЫ item[START:STOP:STEP]             Это способ запомнить, что начальное значение является инклюзивным, а конечное - исключающим.
stars = item  # заменяем изначальный массив временным
item = []  # обнуляем временный массив

# for i in stars:
#     names = i[:1]
#     names_obj = names.sort()
#     print(names)
for input_data in stars:
    name = ''  # формируем одинаковое имя
    if len(input_data) > 4:  # в имени есть пробел
        name = input_data[0] + ' ' + input_data[1]  # первая часть имени плюс пробел плюс вторая часть имени
        input_data = [name] + input_data[2:]  # обновляем ряд в соответствии с новым именем
    elif len(input_data) < 4:  # ряд не рассматриваем
        continue
    else:
        name = input_data[0]

    # SU_Hor, su hor, SU Hor => suhor - преобразовываем все варианты записи имен в один
    name = name.replace('_', '') # replace  помогает нам заменить ненужные символы
    name = name.replace(' ', '') # в агрументах через запятую сначала ставим old через запятую new
    name = name.lower() #преобразует все символы верхнего регистра в строке в символы нижнего регистра
    name = name[:2].upper() + ' ' + name[2:].title()  # снова преобразовываем, suhor => SU Hor


    input_data[0] = name  # обновляем ряд
    input_data[1] = float('24' + input_data[1])  # преобразуем дату и звездную величину в числа из строк
    input_data[3] = float(input_data[3])
    item.append(input_data)  # обновляем временный массив

    name = input_data[0]
    stars = item  # замена
    item = []  # обнуление
    print(name)
# 3 пункт Попросить пользователя ввести имя объекта, данные для которого он хочет получить и названия
# фильтров, данные в которых нужны (возможно введение нескольких фильтров).
# print('Объекты:', object)
# print('Фильтры:', filter)

