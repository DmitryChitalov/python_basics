__author__ = 'AndreiM'
__version__ = "1.0 18.04.2023"
print("\n task_2 \n -------- \n")

"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_text = ['Hello, World\n',
'   pppp      pppp\n',
' PPPPPPPP  PPPPPPPP\n',
'PPPPPPPPPPPPPPPPPPPP\n',
'pppppp ПИТОН pppppp\n',
' pppp PYTHONE pppp\n',
'  PPPPPPPPPPPPPP\n',
'      PPPPPPPP\n',
'         pp']

filename = 'text_2.txt'

#создаем файл и записываем в него my_text
try:
    with open(filename, 'w+', encoding='utf-8') as f:
        f.writelines(my_text)
        print(f'В файле {filename}')
        line = 0
        letter_str = ' '.join(my_text).split()
        for func_line in my_text:
            line += 1

            flag = 0
            word = 0
            for func_letter in func_line:
                if func_letter != ' ' and func_letter != '\n' and flag == 0:
                    word += 1
                    flag = 1
                elif func_letter == ' ':
                    flag = 0

            print(f'   В стр.: {func_line} = {len(func_line)-1} символ. включая пробелы и {word} слова')

        print(f' Всего:  {line} строк., {len(letter_str)} слов.')

except FileNotFoundError:
    print(f'Error. Невозможно создать или открыть файл')