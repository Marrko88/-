import os
import psutil
import shutil
import sys

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("фаил ", newfile, "был успешно создан")
            return True
        else:
            print("возникли проблемы копирования")
            return False

def duble_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i = i + 1

def sys_info():
    print("Что я знаю о системе:")
    print("количество процесоров:", psutil.cpu_count())
    print("кодировка файлов системы:", sys.getfilesystemencoding())
    print("Платформа:", sys.platform)
    print("Текущая дериктоия:", os.getcwd())
    print("Текущий пользователь:", os.getlogin())


def main( ):
    print("Привет, Mark!")
    name = input("Ваше имя:")

    print(name, ', добро пожаловать!')

    answer = ''

    while answer != 'q':
        answer = input("поработаем? (Y/N/q)")
        if answer == "Y":
            print("отлично друг!")
            print("Я умею!: ")
            print(' [1] - выведу список файлов')
            print(" [2] - информация о системе")
            print(" [3] - список процессов")
            print(" [4] - продублировать файлы в текущей дериктории")
            print(" [5] - продублировать указанный  файл ")
            print(" [6] - удалить дубликаты")
            do = int(input("укажите номер действия: "))

            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()
            elif do == 3:
                print(psutil.pids())
            elif do == 4:
                print("=дублировать файлы в текущей дериктории=")
                duble_files(".")
            elif do == 5:
                print(" продублировать указанный  файл ")
                filename = input("укажите имя файла:")
                duplicate_file(filename)

            elif do == 6:
                print(" Удаление дубликатов ")
                dirname = input("укажите имя дериктории:")
                file_list = os.listdir(dirname)
                for f in file_list:
                    fullname = os.path.join(dirname, f)
                    if fullname.endswith('.dupl'):
                        os.remove(fullname)

        elif answer == "N":
            print("В другой раз")
        else:
            print("Что!!!?:)")

if __name__ == "__main__" :
    main()


print ('hello')
