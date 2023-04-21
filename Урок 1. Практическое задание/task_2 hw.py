__author__ = 'AndreiM'
__version__ = "1.0 23.03.2023"
print("\n task_2 \n -------- \n")

secs = float(input("Введите время в секундах: "))

hours = secs / 3600
minutes = secs / 60

print(f"Время в формате ч:м:с - {hours} : {minutes} : {secs}")
#Время в формате ч:м:с - 1.0 : 60.0 : 3600

# Вариант 2
print(f"Время в формате ч:м:с - {secs / 3600:.2f} : {secs / 60:.2f} : {secs}")