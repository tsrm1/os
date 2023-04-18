# https://docs.python.org/3/library/os.path.html

import os
from datetime import datetime

img_folder = './img/'
file_name = 'Text Document.txt'
print('os.getcwd()                                              -> ', os.getcwd())                      # возвращает абсолютный адрес к текущему каталогу
abs_path = os.path.abspath(img_folder)
print('os.path.abspath(img_folder)                              -> ', os.path.abspath(img_folder))      # возвращает абсолютный адрес к eуказанному каталогу
print('os.path.basename(img_folder)                             -> ', os.path.basename(img_folder))     # for the Unix. For Windows = ''
# print('os.path.basename(img_folder)                            -> ', os.path.commonpath(img_folder)
print("os.path.commonprefix(['/usr/lib', '/usr/local/lib'])     ->", os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
print("os.path.commonpath(['/usr/lib', '/usr/local/lib'])       ->", os.path.commonpath(['/usr/lib', '/usr/local/lib']))
print('os.path.dirname(img_folder)                              ->', os.path.dirname(img_folder))
print('os.path.dirname(abs_path)                                ->', os.path.dirname(abs_path))

print('os.path.exists(img_folder)                               ->', os.path.exists(img_folder))        # Boolean, есть ли указанный путь? октрытый файл?
print('os.path.lexists(img_folder)                              ->', os.path.lexists(img_folder))       # Boolean, есть ли указанный путь?
print('os.path.expanduser(img_folder)                           ->', os.path.expanduser(img_folder))    # user’s home directory.
print('os.path.expandvars(img_folder)                           ->', os.path.expandvars(img_folder))

print('os.path.getatime(img_folder + file_name)                 ->', os.path.getatime(img_folder + file_name))  # Время последнего доступа, выраженное в секундах
print('os.path.getmtime(img_folder + file_name)                 ->', os.path.getmtime(img_folder + file_name))  # Время последней модификации контента, выраженное в секундах
print('os.path.getctime(img_folder + file_name)                 ->', os.path.getctime(img_folder + file_name))  # Время создания в Windows, выраженное в секундах
print('os.path.getsize(img_folder + file_name)                  ->', os.path.getsize(img_folder + file_name))   # Размер файла в байтах
print('os.path.isabs(img_folder + file_name)                    ->', os.path.isabs(img_folder + file_name))     # Boolean. Указан ли путь в абсолютном виде?
print('os.path.isfile(img_folder + file_name)                   ->', os.path.isfile(img_folder + file_name))    # Boolean. Есть ли указанный файл?
print('os.path.islink(img_folder + file_name)                   ->', os.path.islink(img_folder + file_name))    # Boolean. Правильно ли указана ссылка (/, \, абсолютный вид)?
print('os.path.isdir(img_folder)                                ->', os.path.isdir(img_folder))                 # Boolean. Есть ли указанный каталог/папка?
print('os.path.ismount(img_folder)                              ->', os.path.ismount(img_folder))               # Boolean. Возврат, Trueесли pathname path является точкой монтирования : точка в файловой системе, где была смонтирована другая файловая система?
# print('os.path.supports_unicode_filenames(img_folder + file_name)->', os.path.supports_unicode_filenames(img_folder + file_name)) # Boolean. True if arbitrary Unicode strings can be used as file names (within limitations imposed by the file system).



# os.path.samefile(path1, path2)  # Return True if both pathname arguments refer to the same file or directory. This is determined by the device number and i-node number and raises an exception if an os.stat() call on either pathname fails.

# os.path.sameopenfile(fp1, fp2) # Return True if the file descriptors fp1 and fp2 refer to the same file.

# os.path.samestat(stat1, stat2) # Return True if the stat tuples stat1 and stat2 refer to the same file. These structures may have been returned by os.fstat(), os.lstat(), or os.stat(). This function implements the underlying comparison used by samefile() and sameopenfile().


print('os.path.join(img_folder, file_name)                      ->', os.path.join(img_folder, file_name))       # Объединение частей пути в один
f_path = ['Projects', 'Python', img_folder, file_name]
f_path = os.path.join("c:", *f_path)
print('os.path.join("c:", *f_path)                              ->', f_path)                                    # Объединение частей пути в один
print('os.path.normcase(f_path)                                 ->', os.path.normcase(f_path))                  # приводит символы в нижний регистр, приводит замену '/' на '\'
print('os.path.normpath(f_path)                                 ->', os.path.normpath(f_path))         # исправляет ошибки в описании пути, приводит замену '/' на '\' и другое
print('os.path.realpath(img_folder + file_name)                 ->', os.path.realpath(img_folder + file_name))  # возвращает реальный путь к файлу
# print('os.path.realpath(img_folder, *, strict=False)            ->', os.path.realpath(img_folder + file_name, *, strict=False))  # возвращает реальный путь к файлу
print('os.path.relpath(img_folder + file_name)                  ->', os.path.relpath(img_folder + file_name))                    # возвращает относительный путь к файлу, относительно текущего каталога
print('os.path.relpath(img_folder + file_name, start=os.curdir) ->', os.path.relpath(img_folder + file_name, start=os.curdir))   # возвращает относительный путь к файлу, относительно указанного каталога
print('os.path.relpath(img_folder + file_name, start="c:/")     ->', os.path.relpath(img_folder + file_name, start='c:/'))       # возвращает относительный путь к файлу, относительно указанного каталога
print('os.path.split(abs_path)                                  ->', os.path.split(abs_path))       # возвращает (head, tail), где tail — это последний компонент имени пути, а head — все, что к нему ведет
print('os.path.splitdrive(abs_path)                             ->', os.path.splitdrive(abs_path))       # возвращает (drive, tail), где drive является либо точкой монтирования, либо пустой строкой
print('os.path.splitext(img_folder + file_name)                 ->', os.path.splitext(img_folder + file_name))       # возвращает последний кусок текста, отделённый точкой


print('_________________________________________________________________________')
statinfo = os.stat(img_folder + file_name)
print("os.stat(img_folder + file_name)                          ->", statinfo)
print("os.stat(img_folder + file_name).st_mode                  ->", statinfo.st_mode)  # .st_mode - Режим файла: биты типа файла и режима файла (разрешения).
print("os.stat(img_folder + file_name).st_ino                   ->", statinfo.st_ino)   # .st_ino - индекс файла в Windows/ номер инода в Unix
print("os.stat(img_folder + file_name).st_dev                   ->", statinfo.st_dev)   # .st_dev - Идентификатор устройства, на котором находится этот файл
print("os.stat(img_folder + file_name).st_nlink                 ->", statinfo.st_nlink) # .st_nlink - Количество жестких ссылок
print("os.stat(img_folder + file_name).st_atime                 ->", statinfo.st_atime, datetime.fromtimestamp(statinfo.st_atime)) # .st_atime - Время последнего доступа, выраженное в секундах
print("os.stat(img_folder + file_name).st_mtime                 ->", statinfo.st_mtime, datetime.fromtimestamp(statinfo.st_mtime)) # .st_mtime - Время последней модификации контента, выраженное в секундах.
print("os.stat(img_folder + file_name).st_ctime                 ->", statinfo.st_ctime, datetime.fromtimestamp(statinfo.st_ctime)) # .st_ctime - время создания в Windows, выраженное в секундах/время последнего изменения метаданных в Unix
print('_________________________________________________________________________')
# current date and time
now = datetime.now()
print('datetime.now()                           ->', now)

# convert from datetime to timestamp
ts = datetime.timestamp(now)
print('datetime.timestamp(now)                  ->', ts)

# convert from timestamp to datetime
date = datetime.fromtimestamp(ts)
print('datetime.fromtimestamp(ts)               ->', date)

print('date.strftime("%H:%M:%S")                ->', date.strftime("%H:%M:%S"))

# YY/mm/dd H:M:S format
print('date.strftime("%Y/%m/%d, %H:%M:%S")      ->', date.strftime("%Y/%m/%d, %H:%M:%S"))

# dd/mm/YY H:M:S format
date_string = date.strftime("%d/%m/%Y, %H:%M:%S")
print('date.strftime("%d/%m/%Y, %H:%M:%S")      ->', date.strftime("%d/%m/%Y, %H:%M:%S"))

# convert from string to datetime
date = datetime.strptime(date_string, "%d/%m/%Y, %H:%M:%S")
print('date.strftime("%d/%m/%Y, %H:%M:%S")      ->', date.strftime("%d/%m/%Y, %H:%M:%S"))
print('_________________________________________________________________________')

date_string = '01/01/1999, 01:01:01'
times = datetime.strptime(date_string, "%d/%m/%Y, %H:%M:%S")
times = int(datetime.timestamp(times))
print(times)


file_path = img_folder + file_name
ns = times = atime, mtime = times, times    # дата и время в секундах
ns = atime_ns, mtime_ns = times, times      # дата и время в наносекундах
os.utime(file_path, times=times, dir_fd=None, follow_symlinks=True) # Set the access and modified times of the file specified by path
# os.utime(file_path, ns=ns, dir_fd=None, follow_symlinks=True) # Set the access and modified times of the file specified by path
# os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)
