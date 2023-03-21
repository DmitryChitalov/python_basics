"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

# формирование и наполнение структуры данных "Товары"

g_name = "Введите название товара: "  # вспомогательные переменные для сокращения длины кода при создании словаря
g_price = "Введите цену: "
g_qty = "Введите количество: "
g_unt = "Введине единицу измерения: "
g_k1 = "название"
g_k2 = "цена"
g_k3 = "количество"
g_k4 = "ед."
end_of_list = 'y'  # признак конца ввода данных пользователем
num = 1
my_list = []
while end_of_list == 'y':
    my_dict = {g_k1: input(g_name), g_k2: int(input(g_price)), g_k3: int(input(g_qty)), g_k4: input(g_unt)}
    my_tuple = (num, my_dict)  # кортеж из номера элемента списка и нового заполненного словаря
    my_list.append(my_tuple)
    num += 1
    end_of_list = input("Если хотите продолжить ввод элементов списка, введите 'y', иначе - любое другое значение")
print("Наполнение структуры данных 'Товары':")
print(*my_list, sep='\n')  # вывод каждого элемента списка с новой строки

# решение аналитической задачи

list_name = []  # вспомогательные списки из уникальных значений для формирования аналитического словаря
list_price = []
list_qty = []
list_unit = []
for el in my_list:
    if list_name.count(el[1].get(g_k1)) == 0:
        list_name.append(el[1].get(g_k1))
    if list_price.count(el[1].get(g_k2)) == 0:
        list_price.append(el[1].get(g_k2))
    if list_qty.count(el[1].get(g_k3)) == 0:
        list_qty.append(el[1].get(g_k3))
    if list_unit.count(el[1].get(g_k4)) == 0:
        list_unit.append(el[1].get(g_k4))

analytical_dict = {"названия": list_name, "цены": list_price, "количества": list_qty, "ед.": list_unit}

print("Наполнение аналитического словаря (ключ -> уникальные значения):")
for key, value in analytical_dict.items():
    print(key, '->', value)
