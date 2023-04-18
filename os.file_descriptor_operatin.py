import os

img_folder = './img/'
file_name_1 = 'Text Document.txt'
file_name_2 = 'readme.txt'

print('__________________________________________________________________________')
# fd = img_folder + file_name
fd1 = os.open(path = img_folder + file_name_1, flags=1, mode=os.O_RDONLY)
fd2 = os.open(path = img_folder + file_name_2, flags=1, mode=os.O_WRONLY)

print(fd1, type(fd1))
print(fd2)


fd = fd2
length = 15
os.ftruncate(fd, length) # обрезает файл до размера в length байт

# os.O_RDONLY
# os.O_WRONLY
# os.O_RDWR
# os.O_APPEND
# os.O_CREAT
# os.O_EXCL
# os.O_TRUNC

# os.O_BINARY
# os.O_NOINHERIT
# os.O_SHORT_LIVED
# os.O_TEMPORARY
# os.O_RANDOM
# os.O_SEQUENTIAL
# os.O_TEXT


# fd_ = 1 # 0 - input, 1 - output, 2 - error
# file = os.fdopen(1, 'r')

# os.close(fd1)
# os.close(fd2)
os.closerange(fd1, fd2)