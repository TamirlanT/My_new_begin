import sys
import os
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_adv import game

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Нужно выбрать одну из команд: list, create_file, create_filder, delete, copy, help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла/ папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует название файла и/или его копии')
        else:
            copy_file(name, new_name)
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название')
        else:
            change_dir(name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
    elif command == 'game':
        game()

save_info('Конец')
