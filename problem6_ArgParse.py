""" Нужно получить кодировку и название нового перекодированного файла
    через аргументы командной строки.
"""
import argparse
import chardet


def createParser():
    parser = argparse.ArgumentParser(description="Программа осуществляет \
перекодировку текстового файла и создаёт новый файл с новой кодировкой.\
Кодировка и название нового файла передаются в качестве аргументов командной \
строки.")
    parser.add_argument('encoding', type=str, help="Future encoding of the file.")
    parser.add_argument('name', type=str, help="A name of the new encoded file.")
    return parser

parser = createParser() # создаю экземпляр класса ArgumentParser через функцию
arguments = parser.parse_args() # собираю аргументы командной строки

f = open("02.txt", 'rb')
s = f.read()
f.close()
encoding = chardet.detect(s)['encoding']
print(f"Текущая кодировка --> {encoding}.")

available_encodings = ("utf-8","ISO-8859-5","cp1251")

if arguments.encoding not in available_encodings:
    print("Файл не может быть перекодирован в данную кодировку.")
    raise SystemExit
else:
    pass


old_file = open("02.txt", 'r', encoding=encoding)
new_file = open(arguments.name, "w+", encoding = arguments.encoding)
text = old_file.read()
new_file.write(text)
old_file.close()
new_file.close()

f = open(arguments.name, 'rb')
s = f.read()
f.close()
encoding = chardet.detect(s)['encoding']
print("Файл был успешно перекодирован.")
print(f"Окончательная кодировка --> {encoding}.")

    
