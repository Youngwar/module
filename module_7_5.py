import os
import time



#os.chdir(r'C:\Users\admin\Desktop\PY')
directory = '.'
for root, dirs, files in os.walk(directory):
    for dir in dirs:
        for file in files:

                filepath = os.path.join(directory, file)
                #print(filepath)
                filetime = os.path.getmtime(filepath)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                #print(formatted_time)
                filesize = os.path.getsize(filepath)
                #print(filesize)
                parent_dir = os.path.dirname(filepath)
                #print(parent_dir)
                print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        directory = os.path.join(directory, dir)
