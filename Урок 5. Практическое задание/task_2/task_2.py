"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

if __name__ == '__main__':
    try:
        with open('file.txt', 'r', encoding='utf-8') as string_obj:
            s = 0
            for i in string_obj:
                s += 1
                if len(i.split()) % 10 == 1 and len(i.split()) != 11:  # 1,21,31...
                    print(f"Строка {s} содержит {len(i.split())} слово.")
                elif (len(i.split()) % 10 == 2 or len(i.split()) % 10 == 3 or len(i.split()) % 10 == 4) and len(
                        i.split()) != 12 and len(i.split()) != 13 and len(
                    i.split()) != 14:  # 2,3,4,22,23,24...
                    print(f"Строка {s} содержит {len(i.split())} слова.")
                else:
                    print(f"Строка {s} содержит {len(i.split())} слов.")
            print(f"Файл содержит количество строк = {s}.")
    except IOError:
        print('Ошибка при вводе данных!')
    except Exception as e:
        print(e)
