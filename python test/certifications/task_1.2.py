
# Напишите код, который запускается  из командной строки и получает на вход  путь до директории на ПК.  Соберите информацию  о содержимом  в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или названия каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога
# В процессе сбора сохраните данные  в текстовый файл  используя логирование 


import os
from collections import namedtuple
import logging

logging.basicConfig(filename='logfile.txt', level=logging.INFO)

item = namedtuple('Item', ['name', 'extension', 'is_dir', 'parent_dir'])

def get_directory_content(path):
 items = []
 try:
  for item in os.listdir(path):
   item_path = os.path.join(path, item)
   if os.path.isfile(item_path):
     name, ext = os.path.splitext(item)
     items.append(item(name, ext, False, os.path.basename(path)))
  else:
     items.append(item(item, '', True, os.path.basename(path)))
 except Exception as e:
  logging.error(e)
  return items

if __name__ == "main":
 input_path = input("Введите путь до директории: ")
 items = get_directory_content(input_path)
for item in items:
  logging.info(item)

