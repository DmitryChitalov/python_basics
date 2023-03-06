plus = int(input("Введите значение прибыли: "))
minus = int(input("Введите значение издержек: "))

if plus < minus:
    print("Фирма работает в убыток")
else:
    print("Финансовый результат - прибыль. Ее величина:" , plus - minus)
    clear_plus = plus - minus
    rent = clear_plus / plus
    print("Рентабельность выручки =" , rent)
    people = int(input("Введите численность сотрудников фирмы: "))
    clear_for_person = clear_plus/people
    print("Прибыль фирмы в расчете на одного сотрудника: " , clear_for_person)