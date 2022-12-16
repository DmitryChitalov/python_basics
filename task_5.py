all_numb = 0
while True:
    i = 0
    list_number = input("Введите несколько чисел, разделенных пробелом. "
                       "Для выхода из программы введите $: ").split()
    numbers = []
    sum_numb = 0
    for el in list_number:
        if el == '$':
            if list_number.index('$') == 0:
                i += 1
                break
            elif list_number.index('$') > 0:
                sum_numb = sum(numbers)
                i += 1
                break
        else:
            numbers.append(int(el))
    sum_numb = sum(numbers)
    all_numb += sum_numb
    print(all_numb)
    if i == 1:
        break
