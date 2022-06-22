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
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file.txt') as f:
  for i in f:
      i = i.split(' ', 1)
      print(i)
      new_file.append(rus[i[0]] + ' ' + i[1])
print(new_file)


with open('n_file.txt', 'w') as n_file:
    n_file.writelines(new_file)


file = open('n_file.txt', 'r')
content = file.read()
print(content)
file.close()




