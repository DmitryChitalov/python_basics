#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_input = input("Введите число >>> ")
if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

result = 0
for x in range(1, 4):
    result += int(user_input * x)

print(result)

