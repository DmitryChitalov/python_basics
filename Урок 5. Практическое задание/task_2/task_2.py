"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("out_file.txt", "w", encoding='utf=8') as f_obj:
    while True:
        input_text = input("Введите данные для записи в файл. Для окончании ввода введите пустую строку.\n>>> ")
        if input_text == "":
            print("Введена пустая строка, данные сохраняются.")
            break
        f_obj.writelines(input_text + '\n')

with open("out_file.txt", encoding='utf=8') as f_obj:
    content = f_obj.readlines()
    print(f"Количество строк: {len(content)}")

with open("out_file.txt", encoding='utf=8') as f_obj:
    for line in f_obj:
        print(f"Количество слов в строке: {len(line.split(' '))}")
