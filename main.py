import itertools
import pathlib

import emoji

# def main():
#     inp = input()
#     spl = inp.split()
#
#     with open("config_files/отсортированный_файл/отсортированный_файл_без_повторений_с_наименьшей_ценой.txt", encoding='utf-8', errors='ignore') as f:
#         try:
#
#             for line in f.readlines():
#                 results = itertools.permutations(spl)
#
#                 for item in results:
#                     blabla = ' '.join(item)
#
#
#                     if line.lower().__contains__(blabla.lower()):
#                         print(emoji.demojize(line))
#         except Exception:
#             print("Возникла ошибка!")
#
#
#     print("\n\n ВВедите новое значение для поиска и нажмите Enter:  ")

def main():
    inp = input()
    spl = inp.split()

    for txt_file in pathlib.Path('config_files/актуальные_цены').glob('*.txt'):
        with open(txt_file, encoding='utf-8', errors='ignore') as f:
            try:
                for line in f.readlines():
                    results = itertools.permutations(spl)
                    for item in results:
                        blabla = ' '.join(item)
                        if line.lower().__contains__(blabla.lower()):
                            print(emoji.demojize(line).replace('\n', '') + ">>>>>>>>>>>>>>>>" + txt_file.name)
            except Exception:
                print("Возникла ошибка!")

    print("\n\n ВВедите новое значение для поиска и нажмите Enter:  ")


if __name__ == '__main__':
    while True:  # вызываем нашу программу в бесконечном цикле
        main()

