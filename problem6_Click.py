import click
import chardet


@click.command()
@click.argument("new_encoding", type=str)
@click.argument("name", type=str)
def main(new_encoding, name):
  f = open("02.txt", 'rb')
  s = f.read()
  f.close()
  encoding = chardet.detect(s)['encoding']
  print(f"Текущая кодировка --> {encoding}.")

  available_encodings = ("utf-8","ISO-8859-5","cp1251")

  if new_encoding not in available_encodings:
    print("Файл не может быть перекодирован в данную кодировку.")
    raise SystemExit
  else:
    pass

  old_file = open("02.txt", 'r', encoding=encoding)
  new_file = open(name, "w+", encoding = new_encoding)
  text = old_file.read()
  new_file.write(text)
  old_file.close()
  new_file.close()

  f = open(name, 'rb')
  s = f.read()
  f.close()
  encoding = chardet.detect(s)['encoding']
  print("Файл был успешно перекодирован.")
  print(f"Окончательная кодировка --> {encoding}.")


if __name__ == "__main__":
  main()



