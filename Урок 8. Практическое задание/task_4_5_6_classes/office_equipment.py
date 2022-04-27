class OfficeEquipment:
    __internal_cost:int = None

    def __init__(self, cost:int) -> None:
        self.cost = cost

    @property
    def cost(self) -> int:
        return self.cost

    @cost.setter
    def cost(self, cost:int) -> None:
        if cost <= 0:
            raise ValueError("Cost can't be less than 0.")
        self.__internal_cost = cost