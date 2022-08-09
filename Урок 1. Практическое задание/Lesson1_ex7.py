present_result = input("Введите Ваш нанешний результат в км: ")
goal = input("Введите Ваш желаемый результат в км: ")
day = 1
present_result = float(present_result)
goal = float(goal)
if goal > present_result:
    while (True):
        print(f"{day}-й день: {round(present_result, 2)}")
        if goal > present_result:
            present_result = present_result + present_result * 0.1
            day = day + 1
        else:
            print(f"На {day}  день Вы достигните результата — не менее {goal} км")
            break
else:
    print("Ваши нынешние показатели соотвествуют желаемым ")
