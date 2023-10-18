from msilib import Directory
import os
from string import digits


# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.



import os
import glob
def group_rename_files(directory, pattern, new_name):

 if not os.path.isdir(directory):
    print(f"Директория {directory} не существует.")
    return

 files = os.listdir(directory)


 for file in files:
     if file.startswith(pattern):
        file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_name + file[len(pattern):])
        os.rename(file_path, new_file_path)
        print(f"Файл {file} был переименован в {new_file_path}.")
 

 num = 1
 for file in files:
   
    if pattern in file:
     
        new_file_name = new_name + str(num).zfill(num_digits)
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_file_name)
  
        os.rename(old_file_path, new_file_path)
       
        num += 1


def group_files(directory, old_extension, new_extension):
    file_pattern = f"{directory}/*.{old_extension}"
    file_paths = glob.glob(file_pattern)
    
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        new_file_name = os.path.splitext(file_name)[0] + f".{new_extension}"
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(file_path, new_file_path)

group_files("/path/to/directory", "txt", "docx")

def accepts_a_range(directory, start, end, desired_name=None):
    file_counter = 1
    for filename in os.listdir(directory):
        if filename.endswith('.txt'): 
            original_name = filename[start-1:end]  
            if desired_name:
                new_filename = desired_name + str(file_counter) + '.txt'  
            else:
                new_filename = original_name + '_' + str(file_counter) + '.txt'  

            original_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(original_path, new_path)  

            file_counter += 1
accepts_a_range("/path/to/directory", 3, 6, 'new_file_')
