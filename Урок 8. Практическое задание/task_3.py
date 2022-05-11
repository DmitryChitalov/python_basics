class MyExc(Exception):
    def __init__(self, txt):
        self.txt = txt


num_lst = []
while True:
    try:
        elem = input("Введите число или stop для завершения: ")
        if elem == 'stop':
            break
        elif elem.isdigit():
            num_lst.append(int(elem))
        else:
            raise MyExc("Вы ввели не число")
    except MyExc as e:
        print(e.txt)

print(num_lst)
