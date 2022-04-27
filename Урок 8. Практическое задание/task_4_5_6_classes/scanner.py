from typing import Tuple
from .office_equipment import OfficeEquipment

class Scanner(OfficeEquipment):
    __internal_resolution:Tuple[int, int]= None

    def __init__(self, cost:int, resolution_width:int, resolution_height:int) -> None:
        if resolution_width <= 0 or resolution_height <= 0:
            raise ValueError("Resolution can't be less than 0.")

        self.__internal_resolution = (resolution_width, resolution_height)
        super().__init__(cost)

    @property
    def resolution(self) -> Tuple[int, int]:
        return self.__internal_resolution