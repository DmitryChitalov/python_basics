"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

EXIT_STRING = 'q'


def summarize():
    print(f'Если вдруг захотите выйти введите "{EXIT_STRING}"')
    full_sum = 0
    while True:
        nums = input("Введите числа, разделенные пробелом: ").split()
        try:
            for num in nums:
                if num in EXIT_STRING:
                    print('Goodbye')
                    return full_sum
                else:
                    full_sum += int(num)
        except ValueError:
            print('Сделаем вид, что вы хотите выйти')
            return full_sum
        print(f"Текущая сумма: {full_sum}")


print(f"Итоговая сумма: {summarize()}")
