import zipfile
"""Импорт библиотеки."""


archive = zipfile.ZipFile("sample.zip", 'r')
data = []

for info in archive.infolist():
  data.append(info.filename)

include = ''
print("Информация о содержимом архива:")
for i in range(len(data)):
  include += data[i] + ' '
  print(data[i], end=" ")
print()

file1 = archive.extract("01.txt")
f = open(file1, 'w', encoding="utf-8")
f.write("")
f.close()

file2 = archive.extract("02.txt")
f = open(file2, 'r', encoding="utf-8")
length = len(f.read())
f.close()

f = open(file2, 'a', encoding="utf-8")
f.write('\n' + "Содержимое архива:")
f.write(include + '\n')
f.write("Кол-во символов до изменения:")
f.write(' ' + str(length) + '\n')
f.close()

__linelist = ["ФИО: Абрамов Илья Викторович\n",
              "Группа: ИСиТ1-2б\n", "Дата: 08.10.2021; 22:06:00."
              ]

with open("03.txt", 'w+') as file3:
  file3.writelines(__linelist)

with zipfile.ZipFile('newzip.zip', 'w') as new_archive:
    new_archive.write('01.txt')
    new_archive.write('02.txt')
    new_archive.write('03.txt')

archive.close()
