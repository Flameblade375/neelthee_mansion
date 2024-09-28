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

class Lock:
    def __init__(self, key_code: str = None):
        self.key_code = key_code if key_code else get_random_string(10)
        self.is_locked = True
    
    def unlock(self, key, player):
        if not self.is_locked:
            do_lock = loop_til_valid_input(
                "The lock is not locked, do you want to lock it again? Y/N",
                "You didn't entor Y or N",
                Y_N
            ).value
            if do_lock:
                type_text("You relock the lock")
                return False
        
        elif key.GetKeyCode() == self.key_code:
            type_text("The lock clicks open!")
            self.is_locked = False
            if key.KeyDels:
                player.inventory.remove(key)
                type_text(f"The {key.name} was used and has been removed from your inventory.")
            return True
            
        else:
            type_text("The lock holds fast!")
            return False
    
    def __str__(self) -> str:
        return self.key_code

class Key(item):
    def __init__(self, name: str = '', KeyCode: str = None, KeyDels: bool = False):
        super().__init__(name, 'key', KeyCode if KeyCode else get_random_string(10))
        self.KeyDels = KeyDels
        self.reveal_count = 0
        self.CurentRevealStr = "=" * len(self.value)

    def GetKeyCode(self):
        return self.value

class KeyRevealer:
    def __init__(self, max_reveals=2):
        self.max_reveals = max_reveals
    
    def reveal_key_code(self, obj: Key, mask_char="="):
        if obj.reveal_count >= self.max_reveals:
            type_text(f"You can only reveal a Key Code {self.max_reveals} times.")
            type_text(f"Here is what you already know about this lock: {obj.CurentRevealStr}")
            return

        if not hasattr(obj, 'lock'):
            key_code = obj.value
        else:
            key_code = obj.lock.key_code
        
        one_third_length = len(key_code) // 3
        
        # Keep track of already revealed indices
        revealed_indices = {i for i, char in enumerate(obj.CurentRevealStr) if char != mask_char}
        
        # Get new indices to reveal
        new_indices = set(sample(range(len(key_code)), one_third_length))

        # Combine revealed and new indices
        all_revealed_indices = revealed_indices.union(new_indices)
        
        # Create the result with revealed characters
        result = [
            key_code[i] if i in all_revealed_indices else mask_char
            for i in range(len(key_code))
        ]

        obj.reveal_count += 1
        obj.CurentRevealStr = ''.join(result)
        type_text("".join(result))
        return True

class ShopItem:
    def __init__(self, item: item, price: int):
        self.item = item
        self.price = price

    def display(self):
        return f"{self.item.name} - {self.price} gold: {self.item.value}"

    def can_buy(self, player) -> bool:
        return player.money >= self.price

    def buy(self, player) -> bool:
        if self.can_buy(player):
            player.money -= self.price
            player.inventory_add(self.item)
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
    
    def keys(self) -> list[Key]:
        keys = []
        for key in self:
            if isinstance(key, Key):
                keys = keys + [key]
        return keys

class container:
    def __init__(self, contents: list[item], secret: bool = False, KeyCode=None) -> None:
        self.contents = contents
        self.secret = secret
        self.lock = Lock(KeyCode) if KeyCode else None
        self.RevealCount = 0
        self.CurentRevealStr = "=" * len(self.lock.key_code) if isinstance(self.lock, Lock) else ""
    
    def take_contents(self, geter=None):
        if isinstance(self.lock, Lock) and self.lock.is_locked:
            type_text("The container is locked and won't budge.")
            return None

        try:
            for Item in self.contents:
                geter.inventory_add(Item)
        except:
            pass
        finally:
            self.contents = []
    
    def Unlock(self, key: Key, player):
        return self.lock.unlock(key, player)
    
    def __str__(self) -> str:
        return self.CurentRevealStr
