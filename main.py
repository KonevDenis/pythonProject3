##1)Считать названия объектов, даты и звездные величины из файла.
f = open('task2_data.dat', 'r')  # открываем файл
stars = f.read().split('\n')  # считываем весь файл, разделяя по переходам строк (используем именно read, потому что readline и readlines создают списки)

#2)Вывести на экран имена объетов, присутствующих в каталоге (без дублей!!!) и фильтров,в которых есть данные для тех или иных объектов.
entries = []  # временный массив
for entry in stars:  # перебираем все ряды
    entries.append(entry.split())  # разделяем ряды по пробелам
entries = entries[1:]  # удаляем первое значение (заголовки)
stars = entries  # заменяем изначальный массив временным
entries = []  # обнуляем временный массив
print(stars)

# for i in stars:
#     names = i[:1]
#     names_obj = names.sort()
#     print(names)
for entry in stars:
    name = ''  # формируем одинаковое имя
    if len(entry) > 4:  # в имени есть пробел
        name = entry[0] + ' ' + entry[1]  # первая часть имени плюс пробел плюс вторая часть имени
        entry = [name] + entry[2:]  # обновляем ряд в соответствии с новым именем
    elif len(entry) < 4:  # ряд не рассматриваем
        continue
    else:
        name = entry[0]

    # SU_Hor, su hor, SU Hor => suhor - преобразовываем все варианты записи имен в один
    name = name.replace('_', '')
    name = name.replace(' ', '')
    name = name.lower()
    name = name[:2].upper() + ' ' + name[2:].title()  # снова преобразовываем, suhor => SU Hor
    entry[0] = name  # обновляем ряд

    entry[1] = float('24' + entry[1])  # преобразуем дату и звездную величину в числа из строк
    entry[3] = float(entry[3])

    entries.append(entry)  # обновляем временный массив
    name = entry[0]
    print(name)
