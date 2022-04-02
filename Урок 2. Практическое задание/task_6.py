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
my_list_product = []
my_choice = "5"
while my_choice != "0":
    print(
        f"Товары 0 - закончить работу с программой, 1 - ввести товар, 2 - вывести список товаров,"
        f" 3 - вывести аналитику")
    my_choice = input(f"Введите ваш выбор : ")
    if my_choice == "0":
        print(f"End")
    elif my_choice == "1":
        while input("Введите 1 и начните заполнять товары, после окончания введите 0 ") == "1":
            my_number = int(input("Введите номер номер товара : "))
            my_list_product_temp = {}
            while input("Введите 1 и начните заполнять параметры товара, после окончания введите 0 ") == "1":
                my_list_product_temp_key = input("Введите наиметование : ")
                my_list_product_temp_value = input("Введите значение : ")
                my_list_product_temp[my_list_product_temp_key] = my_list_product_temp_value
            my_list_product.append(tuple([my_number, my_list_product_temp]))
    elif my_choice == "2":
        print(my_list_product)
    elif my_choice == "3":
        my_analitics = {}
        for my_key in my_list_product:
            for my_list_product_temp_key, my_list_product_temp_value in my_key[1].items():
                if my_list_product_temp_key in my_analitics:
                    my_analitics[my_list_product_temp_key].append(my_list_product_temp_value)
                else:
                    my_analitics[my_list_product_temp_key] = [my_list_product_temp_value]
        print(my_analitics)
