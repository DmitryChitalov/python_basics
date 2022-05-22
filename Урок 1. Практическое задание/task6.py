a = float(input("Введите количество км в первый день: "))
b = int(input("Введите количество км, которое должен пробежать: "))

count = 1;

while (True):
    print(f"День = {count}; км = {a:.2f}")
    count += 1
    a = a + a * 0.1;
    if (a > b):
        break
print(f"День = {count}; км = {a:.2f}")
