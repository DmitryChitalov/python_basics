"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
# Создан файл C:\PyScr\Worker_salary.py

from sys import argv


def worker_salary(w_hours, h_pay, cb_prcnt):
    w_sal = (w_hours * h_pay) + (w_hours * h_pay) / 100 * cb_prcnt
    return w_sal


script, w_h, h_p, cb_persent = argv
w_h = int(w_h)
h_p = int(h_p)
cb_persent = int(cb_persent)

print("Этот скрипт называется: ", script)
print(f"Получены аргументы:\nОтработаные часы - {w_h}, "
      f"Оплата в час - {h_p} и % премии - {cb_persent}.")

print(f"Зарплата работника равна {worker_salary(w_h, h_p,cb_persent)} руб.")

# Жаль выбрасывать рабочий код.
'''
def worker_salary(w_h, h_p, cb_persent):
    w_sal = (w_h * h_p) + (w_h * h_p) / 100 * cb_persent
    return w_sal


u_quit = 0
while u_quit != "**":
    sal_param = input(f"\nВведите Рабочие_ЧАСЫ, Оплата_ЧАС, "
                      f"ПРЕМИЯ_в_% через пробел: ").split()
    w_sal_str = [int(x) for x in sal_param if x.isdigit()]
    if len(w_sal_str) < 3:
        print(f"Ведены некорректные данные! Попробуйте еще раз.")
    else:
        print(f"Зарплата работника равна {worker_salary(*w_sal_str)} руб.")
    u_quit = input("Continue - any, Quit - **: ")
'''