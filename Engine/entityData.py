import copy
import enum
import logging


class itemType(enum.Enum):
    Potion = 1,
    Rune1 = 2,
    Rune2 = 3,
    Rune3 = 4


class Item:
    def __init__(
            self,
            _name,
            _cost,
            _texture,
            _quantity=1,
            _item_type=itemType.Potion,
            _effect_value=0
    ):
        self.name = _name
        self.cost = _cost
        self.quantity = _quantity
        self.texture = _texture
        self.item_type = _item_type
        self.effect_value = _effect_value


class Inventory:
    def __init__(self, _items=None, _capacity=1):
        self.capacity = _capacity
        if _items is None:
            self.items = []
        else:
            self.items = _items
        if len(self.items) > self.capacity:
            logging.critical(f"Inventory: given _items: {_items}, but capacity is {_capacity}")
            raise
        for _ in range(self.capacity - len(self.items)):
            self.items.append(None)

    def addItem(self, _item):
        for item_num in range(self.capacity):
            if self.items[item_num] is None:
                self.items[item_num] = _item
                return

    def removeItem(self, _item):
        self.items.remove(_item)

    def isEmpty(self):
        for item_num in range(self.capacity):
            if self.items[item_num] is not None:
                return False
        return True

    def merge(self, _other):
        first_free = -1
        for item_num in range(self.capacity):
            if self.items[item_num] is None:
                first_free = item_num
                break
        if first_free == -1:
            return
        for item_num in range(_other.capacity):
            if _other.items[item_num] is not None:
                self.items[first_free] = _other.items[item_num]
                _other.items[item_num] = None
                first_free = -1
                for item in range(first_free, self.capacity):
                    if self.items[item_num] is None:
                        first_free = item_num
                        break
                if first_free == -1:
                    return


class EntityData:
    def __init__(
            self,
            _env,
            _hp=100,
            _state="",
            _position=(0, 0),
            _animation_stage=0.0,
            _inventory=None,
            _custom=""
    ):
        self.env = _env
        self.hp = _hp
        self.state = _state
        self.position = _position
        self.animation_stage = _animation_stage
        self.inventory = _inventory
        if self.inventory is None:
            self.inventory = Inventory([])
        self.custom = _custom

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        result.inventory = copy.deepcopy(self.inventory)
        return result