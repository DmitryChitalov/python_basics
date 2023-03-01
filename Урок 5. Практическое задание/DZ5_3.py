pay_obj = open("DZ5_3.txt", 'r')
own_vol = 0
worker = 0
work_list = []
for line in pay_obj:
    pay_list = line.split(' ')
    work_sname = pay_list[0]
    own_vol += float(pay_list[1])
    worker  += 1
    if float(pay_list[1]) < 20000:
        work_list.append(work_sname)
print(f'Зарплата меньше 20000 у {work_list}', '\n', f'средняя зарплата равна {own_vol / worker}, количество работников - {worker}')
pay_obj.close()


