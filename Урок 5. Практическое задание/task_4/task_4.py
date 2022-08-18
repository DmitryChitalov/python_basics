"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

my_dict = {}
with open("file_4.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.read().split()

for i in range(0, len(content) - 1, 2):
    my_dict[content[i]] = content[i + 1]

print(f"Сотрудники с зп меньше 20 000 = {[key for key, val in my_dict.items() if float(val) < 20000]}")

filtered_vals = [float(val) for key, val in my_dict.items() if val != 0]
print(f"Средний доход сотрудников = {sum(filtered_vals) / len(filtered_vals)}")
