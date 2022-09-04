from sys import argv


def sal(t, r, p):
    return t * r + p


hw4_task1, time, rate, prize = argv

print("Выработка в часах: ", time)
print("Ставка в час: ", rate)
print("Премия: ", prize)

print(f"Заработная плата составляет {sal(int(time), int(rate), int(prize))} рублей")
