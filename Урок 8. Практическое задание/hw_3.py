class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
a = ""
while True:
    try:
        a = input("Введите число: ")
        if a == "стоп":
            break
        elif a.isdigit():
            my_list.append(a)
        else:
            raise MyException("Вводите только целые числа!")
    except MyException as e:
        print(e.txt)

print(my_list)