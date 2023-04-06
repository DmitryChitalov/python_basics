"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

# os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
# os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])]]

import csv
import re


def get_data():
    main_data = ["Изготовитель системы", "Название ОС", "Код продукта",
                 "Тип системы"]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    files_array = ["info_1.txt", "info_2.txt", "info_3.txt"]

    for i in range(3):
        file = open(files_array[i], "r")
        content = file.read()
        pattern_1 = re.compile(r'Изготовитель системы:\s*\S*')
        # Как (можно ли) сделать значение - свойство паттерна перебираемым
        os_prod_list.append(pattern_1.findall(content)[0].split()[2])
        pattern_2 = re.compile(r'Название ОС:\s*(.*)')
        # НЕ ПОЛУЧАЕТСЯ вывести сразу два значения, Windows (номер)
        os_name_list.append(pattern_2.findall(content)[0].split()[1])
        pattern_3 = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(pattern_3.findall(content)[0].split()[2])
        pattern_4 = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(pattern_4.findall(content)[0].split()[2])
        file.close()

    array_arrays = []
    array_arrays.append(main_data)

    for i in range(3):
        array = []
        array.append(os_prod_list[i])
        array.append(os_name_list[i])
        array.append(os_code_list[i])
        array.append(os_type_list[i])
        array_arrays.append(array)
    # Совсем туплю, не понимаю как делать не через эти костыли ^^^^^^^^^
    return array_arrays


def write_to_csv(array):
    with open('main_data.csv', 'w') as f_n:
        writer = csv.writer(f_n)
        for row in array:
            writer.writerow(row)
    pass

write_to_csv(get_data())

with open('main_data.csv') as f_n:
    reader = csv.reader(f_n)
    for row in reader:
        print(row)

#ГОСПОДЬ 10 часов и получилось что то похожее 0_о
#При открыти csv файла через PY русские слова отоброжаются вопросами