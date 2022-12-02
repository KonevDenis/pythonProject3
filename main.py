##1)Считать названия объектов, даты и звездные величины из файла.
f = open('task2_data.dat', 'r')  # открываем файл
file = f.read().split('\n')  # считываем весь файл, разделяя по переходам строк (используем именно read, потому что readline и readlines создают списки)
# first = item
# input_data = elem
#
#
#2)Вывести на экран имена объетов, присутствующих в каталоге (без дублей!!!) и фильтров,в которых есть данные для тех или иных объектов.
item = []  # временный массив # item - записи, котрорые будем использовать input_data - входные данные
for input_data in file:  # перебираем все ряды
    item.append(input_data.split())  # разделяем ряды по пробелам
item = item[1:]  # удаляем первое значение (заголовки)
#ПРО СРЕЗЫ item[START:STOP:STEP]             Это способ запомнить, что начальное значение является инклюзивным, а конечное - исключающим.
file = item  # заменяем изначальный массив временным
item = []  # обнуляем временный массив
obj_1 = []
fil_1 = []
zvzdn = []
svet = []
#file = file[1:167] + file[168:172] + file[177:255] + file[257:267]
print(file)
for i in range(len(file)):
    obj_1.append(file[i][0])
    # print(i)
    # print(pip)
    #print(object)
for i in range(len(file)):
    fil_1.append(file[i][2])
# obj_2 = set(obj_1)
# fil_2 = set(fil_1)
# print(set(obj_1))
# print(set(fil_1))
for i in range(len(file)):
    svet.append(file[i][3])

    #print(i)
#[i.split('\t', 1)[0] for i in pip]
#print(pep)
# obj_1 = set() # имена объектов в виде множества
# fil_1 = set() # фильтры
dates =[]
date = []
for i in range(len(file)):
    dates.append(file[i][1])
print(dates)
for i in dates:
    i = '24' + i
    date.append(i)
print(date)
print('Объекты:', set(obj_1))
print('Фильтры:', set(fil_1))
su_hor_fil = []
for i in file:
    if i[0] == "SU_Hor":
        su_hor_fil.append(i[2])
print(su_hor_fil)

rz_lyr_fil = []
for i in file:
    if i[0] == "RZ_Lyr":
        rz_lyr_fil.append(i[2])
print(rz_lyr_fil)
print(fil_1)

i_obj = input("Введите название объекта SU_Hor or RZ_Lyr:" )
i_filt = input("Введите названия фильтров через запятую V B Ic:" )
i_f = i_filt.split(",")


date_g = []
for i in range (0, len(date)):
    print(i)
    hjd = float(date[i]) + 0.5
    jd = int(hjd)
    dt = hjd - jd
    a = jd + 32044           #формула ии вики, чтобы переводить из юлианской в григорианскую
    b = (4*a + 3) // 146097
    c = a - (146097*b // 4)
    d = (4*c + 3)//1461
    e = c - (1461*d)//4
    m = (5*e + 2)//153
    day = e - (153*m + 2)//5 + 1
    month = m + 3 - 12 * (m//10)
    year = 100*b + d - 4800 + (m//10)

    h = dt*24
    mins = (h-int(h))*60
    sec = (mins-int(mins))*60
    g_date = f'{day}.{month}.{year} {int(h)}:{int(mins)}:{int(sec)}'
    date_g.append(g_date)

new_file = open(f'{i_obj}.dat', 'w')
inpfilt = i_filt.split(",")
f0, f1, f2 = None, None, None
if len(inpfilt) == 1:
    f0 = i_filt
    new_file.write(f"Date\t\t\t\t HJD\t\t\t Magn in {f0}\n")
elif len(inpfilt) == 2:
    f0, f1 = inpfilt[0], inpfilt[1]
    new_file.write(f"Date\t\t\t\t HJD\t\t\t Magn in {f0}\t Magn in {f1}\n")
elif len(inpfilt) == 3:
    f0, f1, f2 = inpfilt[0], inpfilt[1], inpfilt[2]
    new_file.write(f"Date\t\t\t\t HJD\t\t\t Magn in {f0}\t Magn in {f1}\t Magn in {f2}\n")

svet0, svet1, svet2, Hjd, data = [], [], [], [], []
for i in range(0, len(file)):
    # for j in range(0, len(obj_1)):
        if obj_1[i] == str(i_obj):
            if fil_1[i] == f0:
                Hjd.append(date[i])
                svet0.append(svet[i])
                data.append(date_g[i])
                svet1.append(f'\t\t')
                svet2.append(f'\t\t')
            elif fil_1[i] == f1:
                Hjd.append(date[i])
                svet0.append(f'\t\t')
                data.append(date_g[i])
                svet1.append(svet[i])
                svet2.append(f'\t\t')
            elif fil_1[i] == f2:
                Hjd.append(date[i])
                svet0.append(f'\t\t')
                data.append(date_g[i])
                svet1.append(f'\t\t')
                svet2.append(svet[i])

for k in range(0, len(Hjd)):
    min_Hjd = min(Hjd)
    ind = Hjd.index(min_Hjd)
    new_file.write(f"{data[ind]}\t {min_Hjd}\t {svet0[ind]}\t {svet1[ind]}\t {svet2[ind]}\n")
    del Hjd[ind], data[ind], svet0[ind], svet1[ind], svet2[ind]

new_file.close()





# #фильтры для сухор
# fil_2_suhor = []
# # while i[0][0] == 'SU_Hor':
# #     print(i)
# #     fil_2_suhor.append(i[0][2])
# # print(fil_2_suhor)
# for i in file:
#     if i[0][0] =
