"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""

with open('fin.txt', 'w') as f:  # result txt
    with open('numbers.txt', 'r') as s:  # txt with nums
        for i in s:
            num = i.split()
            if num[0] == 'One':
                num[0] = 'Один'
                f.write(' '.join(num) + '\n')
            if num[0] == 'Two':
                num[0] = 'Два'
                f.write(' '.join(num) + '\n')
            if num[0] == 'Three':
                num[0] = 'Три'
                f.write(' '.join(num) + '\n')
            if num[0] == 'Four':
                num[0] = 'Четыре'
                f.write(' '.join(num) + '\n')
print(f'All is done')

"""
Один - 1
Два - 2
Три - 3
Четыре - 4
"""
