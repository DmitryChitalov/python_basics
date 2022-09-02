with open("task2_notprog.txt", "r", encoding='utf-8') as f_obj:
    print(f"Количество строк в файле: {len(f_obj.readlines())}")

words = 0
lines = 0
with open("task2_notprog.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        words = line.split()
        lines += 1
        print(f"Количество слов в {lines} строке: {len(words)}")
