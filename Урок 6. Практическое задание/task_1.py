from time import sleep
class TrafficLight:
    try:
        i_rate = int(input("Введите количество циклов (не более 30): "))
        if i_rate > 30:
            raise BaseException
    except BaseException:
        print("Ошибка. Нужно ввести целое число")
        exit(-1)
    __color = ('красный', 'желтый', 'зеленый')
    def running(self):
        i_cycle = 0
        while i_cycle < self.i_rate:
            i_cycle += 1
            i_text = "Сейчас горит светофор: "
            for i_color in TrafficLight.__color:
                if i_color == 'красный':
                    print(i_text, i_color)
                    sleep(7)
                elif i_color == 'желтый':
                    print(i_text, i_color)
                    sleep(2)
                elif i_color == 'зеленый':
                    print(i_text, i_color)
                    sleep(4)
                else:
                    print("Ошибка. Перезапустите программу.")
                    exit(-1)
TrafficLight().running()