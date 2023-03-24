# Создаем класс-дескриптор для конвертации температуры между градусами Цельсия и Фаренгейта
class TemperatureDescriptor:
    def __get__(self, instance, owner):
        return (instance._temperature - 32) * 5 / 9

    def __set__(self, instance, value):
        instance._temperature = value * 9 / 5 + 32


# Создаем класс-дескриптор для валидации возраста
class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        instance._age = value
# Создаем класс-дескриптор для валидации имени
class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        if len(value) < 2:
            raise ValueError("Имя должно состоять из двух или более символов")
        instance._name = value.capitalize()


# Создаем класс Temperature с дескриптором для преобразования температуры
class Temperature:
    celsius = TemperatureDescriptor()

    def __init__(self, celsius):
        self.celsius = celsius


# Создаем класс Person с дескрипторами для валидации возраста и имени
class Person:
    age = AgeDescriptor()
    name = NameDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Пример использования класса Temperature
t = Temperature(0)
print(f"{t.celsius}°C = {t._temperature}°F")  # 0.0°C = 32.
