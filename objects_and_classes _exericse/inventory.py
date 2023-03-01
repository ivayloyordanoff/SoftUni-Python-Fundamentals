class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.left_capacity = capacity

    def add_item(self, item: str):
        if self.left_capacity > 0:
            self.items.append(item)
            self.left_capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"
