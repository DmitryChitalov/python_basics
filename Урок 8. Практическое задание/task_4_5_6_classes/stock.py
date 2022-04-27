from typing import Dict, List
from .office_equipment import OfficeEquipment
from .printer import Printer
from .scanner import Scanner
from .xerox import Xerox
from .empty_list_error import EmptyListError


class Stock:
    __office_equipments:Dict[type, List[OfficeEquipment]] = None

    def __init__(self) -> None:
        self.__office_equipments = {
            Printer: [],
            Scanner: [],
            Xerox: []
        }

    def add_item(self, item:OfficeEquipment) -> None:
        if not issubclass(type(item), OfficeEquipment):
            raise ValueError("Stock can stored only office equipments.")
        
        item_type = type(item)
        if item_type in self.__office_equipments:
            self.__office_equipments[item_type].append(item)
        else:
            self.__office_equipments[item_type] = [ item ]

    def get_item(self, item_type:type) -> OfficeEquipment:
        if item_type in self.__office_equipments and len(self.__office_equipments[item_type]) > 0:
            return self.__office_equipments[item_type].pop(0)
        else:
            raise EmptyListError(f"{item_type.__name__} out of stock.")

    def get_items(self, item_type:type, count:int) -> List[OfficeEquipment]:
        if not type(count) is int:
            raise ValueError("Count must be a integer value")

        if item_type in self.__office_equipments and len(self.__office_equipments[item_type]) >= count:
            result_list = []
            for i in range(count):
                result_list.append(self.__office_equipments[item_type].pop(0))
            
            return result_list
        else:
            raise EmptyListError(f"Can't get {count} {item_type.__name__}s. {item_type.__name__} out of stock.")