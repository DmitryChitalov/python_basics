"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("input_file.txt", "r", encoding='utf-8') as f_obj:
    string_list = f_obj.readlines()
print(f"Количество строк во входном файле: {len(string_list)}")
for i in range(1, len(string_list) + 1):
    print(f"Количество слов в {i} строке: {len(string_list[i - 1].split())}")
