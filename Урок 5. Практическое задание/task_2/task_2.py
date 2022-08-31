"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open(r"file_t02_l05.txt", encoding="UTF-8") as f_obj:
    f_lines = f_obj.readlines()
    print(f"Всего строк в файле: {len(f_lines)}")
    for key, value in enumerate(f_lines):
        f_words = value.split(' ')
        print(f"Количество слов в строке {key + 1}: {len(f_words)}")
