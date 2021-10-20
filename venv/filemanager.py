import subprocess
import os
import shutil
from sys import platform

def dir(l,symb):
    cd = input('Введите назвние каталога .\n')
    directory = (l + symb + cd)
    files = os.listdir(directory)
    os.chdir(l + symb + cd)
    for i in files:
        print(i)
    file = os.chdir(l + symb + cd)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')
    return(directory)

def updir(l,symb):
    deldir = l.split(symb)
    print(deldir[-1])
    cd = l.split(symb+deldir[-1])
    print(cd[0])
    return(cd[0])

def delf(l,symb):
    d = input('Введите путь к файлу для удаления>>')
    os.remove(l + symb + d, dir_fd=None)
    print('готово,файл', d, 'удален из дерриктории:', l)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def deld(l,symb):
    d = input('Введите путь к каталогу для удаления>>')
    os.rmdir(l + symb + d)
    print('готово,файл', d, 'удален из дерриктории:', l)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def newf(l,symb):
    nf = input('Введите имя и расширение файла>>')
    open(nf, "w")
    print('Файл создан в дерриктории:', l, 'с именем', nf)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def newd(l,symb):
    print('Введите название паки чтобы создать ее в дериктории:', l)
    nd = input(">>")
    os.mkdir(nd)
    print('готово, папка создана с именем-', nd, 'в дерриктории:', l)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def read(l,symb):
    print('Введите путь к файлу')
    in_file = input()
    my_file = open(l + symb + in_file)
    my_string = my_file.read()
    print(my_string)
    my_file.close()
    print('Прочитан файл - ', in_file)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def write(l,symb):
    print('Введите путь к файлу')
    in_file = input()
    my_file = open(l + symb + in_file, "a")
    writing = input('Введите текст\n')
    my_file.write(writing)
    my_file.close()
    print('Запись сдедлана в файл - ', in_file)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def copyf(l,symb):
    path1 = input('Введите путь файла, который нужно скопировать\n')
    path2 = input('Введите путь, куда нужно скопировать\n')
    shutil.copy2(l + symb + path1, l + symb + path2)
    print('Файла скопирован в ', l + symb + path2)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def movef(l,symb):
    path1 = input('Введите путь файла, который нужно переместить\n')
    path2 = input('Введите путь, куда нужно переместить\n')
    shutil.move(l + symb + path1, l + symb + path2)
    print('Файла перемещен в ', l + symb + path2)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def renamef(l,symb):
    path1 = input('Введите путь файла, который нужно переименовать\n')
    path2 = input('Введите новое имя\n')
    os.rename(l + symb + path1, l + symb + path2)
    print('Файла перемещен в ', l + symb + path2)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def openf(l,symb):
    openf = input('Введите название файла >> ')
    cmd = openf
    subprocess.Popen(cmd, shell=True)
    print('введите Полное название католога для перехода или просто введите название каталога в этой дирректории')

def __main__():
    if platform == "linux" or platform == "linux2":
        symb = '/'
    elif platform == "win32" or platform == "win64":
        symb = '\\'
    c=''
    print('введите Полное название католога в виде C:\ ')
    l = input()
    homedir = l
    print(symb)
    while c != 'stop':
        directory = (l)
        files = os.listdir(directory)
        file = os.chdir(l)
        print('Текущий каталог: ', l)
        print('Домашний каталог: ', homedir)
    # запуск программ или переход в другую директорию
        print('введите комманду')
        c = input()
        if c == 'help':
            print("\nвведите dir чтобы перейти в другой каталог либо в католог в этой папке "
                "\nвведите updir чтобы перейти на папку выше "
                "\nвведите lsdir чтобы отобразить содержимое текущей папки "
                "\nдля того чтобы создать файл введите newf, "
                "\nвведите newd чтобы создать папку, "
                "\nвведите delf если хотите удалить файл в катологе>"
                "\nвведите deld если хотите удалить каталог>"
                "\nвведите read чтобы посмотреть содержимое файла"
                "\nвведите write чтобы сделать запись в файл"
                "\nвведите copyf чтобы скопировать файл в другой каталог"
                "\nвведите movef чтобы переместить файл в другой каталог"
                "\nвведите renamef чтобы переименовать файл\n"
                "stop для остановки программы\n",
                l)
        elif c == 'lsdir':
            for i in files:
                print(i)
        elif c == 'dir':
            l = dir(l,symb)
        elif c == 'updir':
            if l == homedir:
                print('!Невозможно подняться выше домашнего каталога!')
            else:
                l = updir(l,symb)
        elif c == 'delf':  # Удаление файла из дерриктории
            delf(l,symb)
        elif c == 'deld':  # Удаление файла из дерриктории
            deld(l,symb)
        elif c == 'newf':
            newf(l,symb)
        elif c == 'newd':
            newd(l,symb)
        elif c == 'read':
            read(l,symb)
        elif c == 'write':
            write(l,symb)
        elif c == 'copyf':
            copyf(l,symb)
        elif c == 'movef':
            movef(l,symb)
        elif c == 'renamef':
            renamef(l,symb)
        elif c == 'open':
            openf(l,symb)
        elif c == 'stop':
            print('Выхожу из программы')
        else:
            print('Введена неверная команда\nОткатываемся\nВведите путь заново')


if __name__ == "__main__":
    __main__()
