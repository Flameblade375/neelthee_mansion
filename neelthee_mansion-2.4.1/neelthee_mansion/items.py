from .utils import *

class item:

    def __init__(self, name: str = '', type: str = 'miscellaneous', value: int = 0):
        self.name = name
        self.type = type
        self.value = value

    def sell(self, seller) -> bool:
        if self.type.lower() == 'valuable':
            seller.money += self.value
            return True
        else:
            return False

    def IsUsable(self) -> bool:
        return self.usable

class ShopItem:
    def __init__(self, item: item, price: int):
        self.item = item
        self.price = price

    def display(self):
        return f"{self.item.name} - {self.price} gold: {self.item.effect}"

    def can_buy(self, player) -> bool:
        return player.money >= self.price

    def buy(self, player) -> bool:
        if self.can_buy(player):
            player.money -= self.price
            player.inventory.append(self.item)
            return True
        else:
            return False

class inv(list):
    def __contains__(self, item_name) -> bool:
        for item_ in self:
            if item_.name == item_name:
                return True
        return False
    
    def index(self, value, start=0, end=None):
        if end is None:
            end = len(self)
        
        # Custom implementation of index method
        for i in range(start, end):
            if isinstance(self[i], item):
                if self[i].name == value:
                    return i
        return None
    
    def remove(self, value):
        if isinstance(value, item):
            if value in self:
                del self[self.index(value.name)]
                return
        del self[self.index(value)]

class container:
    def __init__(self, contents: list[item], secret: bool = False) -> None:
        self.contents = contents
        self.secret = secret
    
    def take_contents(self, geter = None):
        try:
            for Item in self.contents:
                geter.inventory_add(Item)
        finally:
            self.contents = None
