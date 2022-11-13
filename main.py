##1)Считать названия объектов, даты и звездные величины из файла.
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
print(item)
for input_data in stars:
    name = ''  # формируем одинаковое имя
    if len(input_data) > 4:  # в имени есть пробел
        name = input_data[0] + ' ' + input_data[1]  # первая часть имени плюс пробел плюс вторая часть имени
        input_data = [name] + input_data[2:]  # обновляем ряд в соответствии с новым именем
    elif len(input_data) < 4:  # ряд не рассматриваем
        continue
    else:
        name = input_data[0]
        print(name)

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
