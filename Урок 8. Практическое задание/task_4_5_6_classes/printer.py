from .office_equipment import OfficeEquipment

class Printer(OfficeEquipment):
    __is_color:bool = False

    def __init__(self, cost:int, is_color:bool) -> None:
        if type(is_color) is bool:
            self.__is_color = is_color
        else:
            raise ValueError("Printer is_color value must be a boolean type.")
        super().__init__(cost)

    def is_color(self) -> bool:
        return self.__is_color