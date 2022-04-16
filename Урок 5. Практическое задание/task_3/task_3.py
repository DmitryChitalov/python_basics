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

def converter(line):
    words = line.split()
    if "One" == words[0]:
        return "Один"
    if "Two" == words[0]:
        return "Два"
    if "Three" == words[0]:
        return "Три"
    if "Four" == words[0]:
        return "Четыре"

f_r = open("tmp.txt")
f_w = open("new_tmp.txt", "w")

while True:
    line = f_r.readline()
    if None == line:
        break;
    new_word = converter(line)
    f_w.write(new_word)
    words = line.split()
    f_w.write(line[len(words[0]):])

f_r.close()
f_w.close()

"""
Не понимаю, почему при выполнении кидается исключение, но при этом программа выполняется корректно:
Traceback (most recent call last):
  File "/home/aleksandr/git/study/python_basics/Урок 5. Практическое задание/task_3/task_3.py", line 30, in <module>
    new_word = converter(line)
  File "/home/aleksandr/git/study/python_basics/Урок 5. Практическое задание/task_3/task_3.py", line 14, in converter
    if "One" == words[0]:
IndexError: list index out of range"""

