class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

user_list = []
while True:
    try:
        user_data = input("Введите число. Для выхода из программы введите "
                          "stop: ")
        if user_data == 'stop':
            print(f"Список чисел сформирован: {user_list}. Программа "
                  f"завершена.")
            break
        if user_data.isdigit() == False:
            raise OwnError("Вы ввели не число!")
            continue
        else:
            user_list.append(int(user_data))
    except OwnError as err:
        print(err)
        continue