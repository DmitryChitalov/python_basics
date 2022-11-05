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


replace_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def multiple_replace(target_str, replace_d):
    # получаем строку которую надо заменить, и словарь, в котором находятся необходимые для замены значения
    for i, j in replace_d.items():
        # обходим словарь, i - ключ, j - значение которое будет использоваться под замену
        target_str = target_str.replace(i, j)
        # Когда в строке обнаруживается значение i, оно заменяется на j. Если не находится - ничего не происходит
    return target_str


my_f = open("1234.txt", "r", encoding="utf-8")
new_file = open("1234_new.txt", "w", encoding="utf-8")


for line in my_f:
    my_str = multiple_replace(line, replace_dict)
    new_file.write(my_str)

my_f.close()
new_file.close()

# Смотрим новый файл

with open("1234_new.txt", "r", encoding="utf-8") as my_new_file:
    print(my_new_file.read())
