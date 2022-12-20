class ZeroDivision(Exception):
    def __init__(self, number, divider):
        self.number = number
        self.divider = divider

    def divide_null(self):
        try:
            print(f"Результат деления: {self.number / self.divider}")
        except ZeroDivisionError as err:
            print(err)


a = ZeroDivision(3, 0)
a.divide_null()