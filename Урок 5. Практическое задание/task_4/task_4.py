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


from translate import Translator
translator = Translator(from_lang="en",to_lang="ru")

my_f = open("task4_lesson5.txt", "r") #открываем 1-й файл

content_en = my_f.read() #из 1-го файла переносим текст в переменную content_en
content_ru = translator.translate(content_en) #переводим content_en на русский язык и вставляем текст в content_ru
my_f2 = open("task4_lesson5_2.txt", "w")#открываем пустой 2-ой файл
my_f2.write(content_ru) #записываем в файл текст из content.ru

my_f.close()
my_f2.close()






print(content)



