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
rus_num = ["Один ", "Два ", "Три ", "Четыре "]
i = 0
res_text = []
with open("file.txt", "r", encoding="utf-8") as ext_file:
    for line in ext_file:
        list_words = line.split(" ", 1)  # делим по первому пробелу
        list_words[0] = rus_num[i]  # заменяем нулевой элемент списка
        res_text.extend(list_words)  # добавляем в результирующий список
        i += 1
""" запись результата в новый файл """
with open("result.txt", "w", encoding="utf-8") as res_file:
    res_file.writelines(res_text)
""" для наглядности вывел файл результат в терминал """
with open("result.txt", "r", encoding="utf-8") as res_file:
    print(res_file.read())
