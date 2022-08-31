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
dict_int = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

task_input = open("task3_input.txt", 'r', encoding='utf-8')
task_output = open("task3_output.txt", 'w', encoding='utf-8')
for line in task_input:
    for key in dict_int.keys():
        line = line.replace(key, dict_int[key])
    task_output.write(line)
task_output.close()
task_input.close()