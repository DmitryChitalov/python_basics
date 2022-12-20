class IntNumbers(Exception):

    @staticmethod
    def input_num():
        number_list = []
        print("Введите числа. Чтобы закончить ввод - stop.")
        while True:
            number = input()
            if number == "stop":
                break
            else:
                try:
                    number_list.append(int(number))
                except ValueError as ve:
                    print(f"Введите число! Недопустимое значение {number}")
        return number_list

print(IntNumbers.input_num())