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

car_list = []
try:
    index = 1
    while True:
        print("Enter a car data or input \"Continue\" for continue work program")

        brand = input("Please, input car brand name - ")
        if brand == "Continue":
            break

        model = input("Please, input car model name - ")
        if model == "Continue":
            break

        price = int(input("Please, input car price - "))
        count = int(input("Please, input count cars - "))

        engine = input("Please, input engine type - ")
        if engine == "Continue":
            break

        car_list.append((index, {
            "brand": brand, 
            "model": model, 
            "price": price, 
            "count": count, 
            "engine": engine}
            )
        )
        print()
        index += 1
except:
    pass
finally:
    print("Base data: ")
    for car in car_list:
        print(car)

    result = {
        "brand": [],
        "model": [],
        "price": [],
        "count": [],
        "engine": []
    }

    for car in car_list:
        for key in car[1]:
            result[key].insert(0, car[1][key])


    print("Result:")
    print("{")
    for key in result:
        print(f"  {key}: {list(set(result[key]))},")

    print("}")