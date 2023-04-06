"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в которомпервому ключу
соответствует список,второму — целое число, третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml
import string

slovar = {}
s = string.punctuation[3]
slovar['computer'] = '200' + s + '-1000' + s
slovar['keyboard'] = '5' + s + '-50' + s
slovar['mouse'] = '4' + s + '-7' + s
slovar['printer'] = '100' + s + '-300' + s

spisok = {'list': ['computer', 'printer', 'keyboard', 'mouse']}
cifra = {'num': 2}
slovar_vslovare = {'dict': slovar}

to_yaml = {}
to_yaml.update(spisok)
to_yaml.update(cifra)
to_yaml.update(slovar_vslovare)

with open('hoom_file.yaml', 'w', encoding='utf-8') as out_file:
    yaml.dump(spisok, out_file, default_flow_style=False, allow_unicode=True)
    yaml.dump(cifra, out_file, default_flow_style=False, allow_unicode=True)
    yaml.dump(slovar_vslovare, out_file, default_flow_style=False,
              allow_unicode=True)

# ТОЛЬКО НЕ ПОНЯЛ КАК ПЕРЕВРНУТЬ СОХРАНЕНИЕ В ОБРАТНОМ ПОРЯДКЕ
# Если сохроять всё в одном списке (to_yaml) оно задаёт свой порядок

with open('hoom_file.yaml', 'r', encoding='utf-8') as file:
    conten = yaml.load(file, Loader=yaml.FullLoader)
    print(to_yaml)
    print(conten)
    if to_yaml == conten:
        print("Cхожее")
    else:
        print("Не схожее")
