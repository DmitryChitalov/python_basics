"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
out_f = open("dz_3.txt", "w", encoding='utf-8')
str_list = ['Фещенко 23600.12\n', 'Иванов 22456.01\n', 'Сидоров 5678.45\n', 'Петров 34567.98\n', 'Головин 13543.34\n',
            'Ким 13333.44\n', 'Лим 4566.11\n', 'Ткаченко 34522.11\n', 'Степанов 11111.33\n', 'Гай 233333.23\n']
out_f.writelines(str_list)
out_f.close()


out_f = open("dz_3.txt", "r", encoding='utf-8')
i = 0
print("Cотрудники, имееющие оклад менее 20 тысяч:")
for line in out_f:
    line_i = line.split()
    i = i + float(line_i[1])
    if float(line_i[1]) < 20000:
        print(line_i[0])
print(f'Средняя величина дохода сотрудников - {i/float(len(str_list))}')
out_f.close()
