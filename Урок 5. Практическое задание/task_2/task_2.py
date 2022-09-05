"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('file.txt', 'r') as my_file:
    count = 0
    for line in my_file:
        count += 1
        sp = line.split()
        letters = len(sp)
        print(f'В строке №{count} количество слов: {letters}')


"""убрал кодировку utf-8, т.к. файл создавал в windows - блокнот и при добавлении encoding='utf-8' появляется ошибка
с которой пока не разобрался:

(result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 0: invalid continuation byte
 
 """