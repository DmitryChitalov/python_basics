str_ = input("Введите выручку: ")
profit = income = costs = personal = 0
try:
    income = int(str_)
except:
    print("ОШИБКА: введенное значение содержит символы")
    quit()
str_ = input("Введите издержки: ")
try:
    costs = int(str_)
except:
    print("ОШИБКА: введенное значение содержит символы")
    quit()
str_ = input("Введите численность сотрудников: ")
try:
    personal = int(str_)
except:
    print("ОШИБКА: введенное значение содержит символы")
    quit()

profit = income - costs
print(f"Прибыль = {profit:10d}\n"
        f"Реентерабельность = {(profit / income):10.2f}\n"
        f"Прибыль/сотрудик = {(profit / personal):10.2f}")
