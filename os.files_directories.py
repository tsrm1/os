import os
import stat

img_folder = './img/'
file_name = 'Text Document.txt'
file = img_folder + file_name

print('_________________________________________________________________________1')
# os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
# os.F_OK
# os.R_OK
# os.W_OK
# os.X_OK
if os.access(file, os.R_OK):
    with open(file) as fp:
        data = fp.read()
        print(data)



print('_________________________________________________________________________2')
try:
    fp = open(file)
except PermissionError:
    data = "some default data"
else:
    with fp:
        data = fp.read()
finally:
    print(data)
    
print('_________________________________________________________________________3')

# os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)

# https://docs.python.org/3/library/stat.html#stat.S_IRUSR
# stat.S_ISUID - Set UID bit.
# stat.S_ISGID - Set-group-ID bit.
# stat.S_ENFMT
# stat.S_ISVTX - Sticky bit. When this bit is set on a directory it means that a file in that directory can be renamed or deleted only by the owner of the file, by the owner of the directory, or by a privileged process.
# stat.S_IREAD
# stat.S_IWRITE
# stat.S_IEXEC
# stat.S_IRWXU - Mask for file owner permissions.
# stat.S_IRUSR - Owner has read permission
# stat.S_IWUSR - Owner has write permission.
# stat.S_IXUSR - Owner has execute permission.
# stat.S_IRWXG - Mask for group permissions.
# stat.S_IRGRP - Group has read permission.
# stat.S_IWGRP - Group has write permission.
# stat.S_IXGRP - Group has execute permission.
# stat.S_IRWXO - Mask for permissions for others (not in group).
# stat.S_IROTH - Others have read permission.
# stat.S_IWOTH - Others have write permission.
# stat.S_IXOTH - Others have execute permission.

os.chmod(file, stat.S_IRUSR)
print('_________________________________________________________________________4')
print('os.getcwd()              ->', os.getcwd())   # возвращает текущую директорию
print('os.getcwdb()             ->', os.getcwdb())  # возвращает текущую директорию в бинарном виде
print('_________________________________________________________________________5')


print('os.listdir(path=".")     ->', os.listdir(path=img_folder)) # возвращает список файлов и папок по указанному пути
print('_________________________________________________________________________6')
files = os.scandir(path=img_folder)
print('os.scandir(path=".")     ->', files) # возвращает список файлов и папок по указанному пути
for file in files:
    print(file.name)
print('_________________________________________________________________________7')
with os.scandir(img_folder) as files:
    for file in files:
        if not file.name.startswith('.') and file.is_file():
            print('File  : ', file.name)
        elif file.is_dir():
            print('Folder: ', file.name)
        elif file.is_symlink():
            print('Link  : ', file.name)
print('_________________________________________________________________________8')

dir_name = img_folder + '1'
if not os.path.exists((dir_name)):      # создаём папку, если её нет
    os.mkdir(dir_name,  mode=0o777)
    print("Create folder: ", dir_name)
    dir_name += '/2'
    os.mkdir(dir_name,  mode=0o777)
    print("Create folder: ", dir_name)
    dir_name += '/3'
    os.mkdir(dir_name,  mode=0o777)
    print("Create folder: ", dir_name)

dir_name = img_folder + '4/5/6'
if not os.path.exists((dir_name)): 
    os.makedirs(dir_name, mode=stat.S_IRWXU, exist_ok=False) # рекурсивное создание папок
    print("Create folders: ", dir_name)

# os.remove(img_folder + file_name) # удаление файла

input('Нажмите Enter')

src = img_folder + '4'
dst = img_folder + '10'
os.rename(src, dst, src_dir_fd=None, dst_dir_fd=None)
print("Folder ", src,' renamed on ', dst )

input('Нажмите Enter')
old = dst + '/5/6'
new = dst + '/11/12'
os.renames(old, new) # Recursive directory or file renaming function. Works like rename(), except creation of any intermediate directories needed to make the new pathname good is attempted first
print("Folders ", old,' renamed on ', new )


input('Нажмите Enter')
os.removedirs(new) # Remove directories recursively
print("Delete folders: ", new)

src = img_folder + '1/2'
dst = img_folder + '2'
os.replace(src, dst, src_dir_fd=None, dst_dir_fd=None) # Rename the file or directory src to dst

os.rmdir(img_folder + '1', dir_fd=None) # Remove (delete) the directory path
os.rmdir(img_folder + '2/3', dir_fd=None) # Remove (delete) the directory path
os.rmdir(img_folder + '2', dir_fd=None) # Remove (delete) the directory path


print('_________________________________________________________________________9')
# https://docs.python.org/3/library/os.html#os.walk
# os.walk(top, topdown=True, onerror=None, followlinks=False) # 
# Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames)

top = os.getcwd()
for root, dirs, files in os.walk(top, topdown=True):
    print(root, "consumes", end=" ")
    print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
print('_________________________________________________________________________10')
top = './img/temp_folder'
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

print('_________________________________________________________________________11')
input("Внимание. Все данные в  папке ./img/temp_folder/ будут удалены. Нажмите Enter")


# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
top = './img/temp_folder'
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
print(f'Все файлы из папки {top} - удалены!')
print('_________________________________________________________________________12')

