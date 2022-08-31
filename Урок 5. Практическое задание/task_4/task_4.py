
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



+ content = []
+ dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
+ with open("eng.txt", 'r', encoding='utf-8') as eng_obj:
+    for line in eng_obj:
+        if line.split()[0] in dictionary:
+           content.append(line.replace(line.split()[0], dictionary[line.split()[0]]))
+ with open("ру.txt", 'w', encoding='utf-8') as rus_obj:
+    rus_obj.writelines(content)
