"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

sum_salary = 0
low_salary = []
payroll_list = [line.split() for line in open('payroll.txt', encoding='utf-8')]
for el in payroll_list:
    sum_salary += float(el[1])
    if float(el[1]) < 20000:
        low_salary.append(el[0])
print(f'Сотрудники с окладом менее 20 тысяч: {", ".join(low_salary)}')
print(f'Cредний доход сотрудников: {(sum_salary / len(payroll_list))}')
