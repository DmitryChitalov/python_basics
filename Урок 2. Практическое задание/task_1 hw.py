__author__ = 'AndreiM'
__version__ = "1.0 24.03.2023"
print("\n task_1 \n -------- \n")

my_list = [5, "String", 0.15, True, None]
def my_type(el):
    for i in range(len(my_list)):
        print(type(my_list[i]))
    return
my_type(my_list)

""""
Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""