
def el_string_sum(string, ind):
    arr = string.split(" ")
    mas = []
    try:
        for el in arr:
            ind = el
            mas.append(int(el))
    except ValueError:
        return sum(mas), ind
    return sum(mas), ind


fin_sum = 0
index = ''
while index != 'q':
    enter = input('введите целое число через пробел или "q" для выхода: ')
    tmp, index = el_string_sum(enter, index)
    fin_sum += tmp
    print(f'sum = {fin_sum}')