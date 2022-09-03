"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
def row_count():
    try:
        with open("data_file2.txt", "r", encoding="utf-8") as df:
            line_list = df.readlines()
            for i in range(len(line_list)):
                new_list = line_list[i].split()

                print(f"В {i + 1}-ой строке {len(new_list)} слов(а)")
    except FileNotFoundError:
        return print("\nФайл не найден.")
    print(f"Количество строк в файле - {len(line_list)}")


row_count()