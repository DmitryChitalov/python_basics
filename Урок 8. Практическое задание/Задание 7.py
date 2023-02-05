"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

num_a = '2+i'  # same 2+1i
num_b = '3+4i'
num_a = num_a[:-1].split(',')
num_b = num_b[:-1].split(',')


class Complexint:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):

        for i in range(len(self.num)):
            for j in range(len(other.num)):
                self.num[i] = self.num[i] + other.num[j]
                i += 1
            break
        return Complexint(self.num)

    def __mul__(self, other):
        for i in range(len(self.num)):
            for j in range(len(other.num)):
                try:
                    self.num[i] = (self.num[i] * other.num[j] - self.num[i + 1] * other.num[j + 1])
                    self.num[i + 1] = (self.num[i] * other.num[j + 1] + self.num[i + 1] * other.num[j])
                except IndexError:
                    pass
            break
        return Complexint(self.num)

    def __str__(self):
        final = [str(i) for i in self.num]
        final = '+'.join(final)
        return f'{final}i'


for i in num_a:
    minuscount = i.count('-')
    if '+' in i:
        i = i.split('+')
        if i[1] == '':
            i[1] = '1'
    if '-' in i:
        i = i.split('-')
        if i[1] == '':
            i[1] = '1'
        if minuscount == 1:
            i[-1] = f'-{i[-1]}'
        if minuscount == 2:
            i[-1] = f'-{i[-1]}'
            i[-2] = f'-{i[-2]}'
            i.remove('')
    num_a = i
    num_a = [int(i) for i in num_a]

for j in num_b:
    minuscount = j.count('-')
    if '+' in j:
        j = j.split('+')
        if j[1] == '':
            j[1] = '1'
    if '-' in j:
        j = j.split('-')
        if j[1] == '':
            j[1] = '1'
        if minuscount == 1:
            j[-1] = f'-{j[-1]}'
        if minuscount == 2:
            j[-1] = f'-{j[-1]}'
            j[-2] = f'-{j[-2]}'
            j.remove('')
    num_b = j
    try:
        num_b = [int(m) for m in num_b]
    except ValueError:
        pass

x_add = Complexint(num_a)
y_add = Complexint(num_b)

x_mul = Complexint(num_a)
y_mul = Complexint(num_b)

# Тестировать или + или *, не одновременно

# print(f'Add complex integers {x_mul} and {y_mul}:')
# print(x_add + y_add)

print(f'Multiply complex integers {x_mul} and {y_mul}:')
print(x_mul * y_mul)

"""
Add complex integers 2+1i and 3+4i:
5+5i

Multiply complex integers 2+1i and 3+4i:
2+11i
"""
