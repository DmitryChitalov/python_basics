"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml


def yaml_new_data():
    first = {
        1: [1, 2, 3, 4],
        2: 1254621,
        3: {1: '\u2740', 2: '\u2730', 3: '\u03ab'}
    }

    with open('file.yaml', 'w', encoding='utf-8') as file1:
        yaml.dump(first, file1, default_flow_style=False,
                  allow_unicode=True)


def read_file():
    try:
        with open('file.yaml', 'r', encoding='utf-8') as file2:
            content = yaml.Loader(file2)
            return content
    except FileNotFoundError:
        print('Файл не найден')


yaml_new_data()
print(read_file())
