class Myclass:

    def __init__(self):
        self.a = []
        while True:
            b = input(f"Введите значение ")
            if b == "yes":
                print(self.a)
                break
            else:
                try:
                    self.a.append(int(b))
                except ValueError:
                    print("Не является цифрой")
            print(f"Введите yes чтобы закончить ввод")


Myclass()