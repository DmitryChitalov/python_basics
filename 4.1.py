from sys import argv
def obj(args, index):
    try:
        return int(args[index])
    except:
        return 0

salary, time, bonus = obj(argv, 1), obj(argv, 2), obj(argv, 3)
print(f'Сотрудник получил = {time * salary + bonus}')