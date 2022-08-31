"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
+ from datetime import date 
+
+
+ class data:
+   def __init__(self, data):
+       self.data = data.split('-')
+
+   @classmethod
+   def type(cls, data):
+       try:
+           day, month, year =[int(i) for i in data.split('/')]
+           return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
+       except ValueError:
+           return 'Формат даты не верен!'
+
+   @staticmethod
+   def valid(data):
+       try:
+           day, month. year = data.split('/')
+           date(int(year), int(month), int(day))
+           return 'Есть такая дата!'
+       except ValueError:
+           return 'Формат даты не верен!'
+
+
+   print(Data.valid('01/01/2001'))
+   print(Data.valid('01-01-2001'))
+   print(Data.type('12/12'))
+
+
+
+
