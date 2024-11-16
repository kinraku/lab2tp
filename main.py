import random
from abc import ABC, abstractmethod

# ABC Attacker - для классов которые могут атаковать
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

# ABC Moveable - для классов которые могут перемещаться
class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

class GameObject(ABC):
    def __init__(self, object_id, name, x, y):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self._hp = hp
    def is_alive(self):
        return self._hp > 0
    def get_hp(self):
        return self._hp
    def receive_damage(self):
        self._hp -= (random.randint(18, 23))

class Archer(Unit, Attacker, Moveable):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y, hp)
    def attack(self, target):
        if isinstance(target, Unit):  # Проверяем, является ли цель экземпляром Unit
            print(f"{self.get_name()} атакует {target.get_name()}")
            target.receive_damage()  # Условный урон
            print(f"Здоровье {target.get_name()} после атаки {self.get_name()}: {target.get_hp()}")
        else:
            print(f"{self.get_name()} не может атаковать {target.get_name()}, так как это не юнит")
    def move(self, x, y):
        print(f"{self.get_name()} перемещается на координаты ({x}, {y})")
        self._x = x
        self._y = y

class Building(GameObject):
    def __init__(self, object_id, name, x, y):
        super().__init__(object_id, name, x, y)
        self._built = False
    def is_built(self):
        print(f"Строение {self._name} построено: {self._built}")
    def set_built(self, built):
        self._built = built

class Fort(Building, Attacker):
    def __init__(self, object_id, name, x, y):
        super().__init__(object_id, name, x, y)
        self.set_built(True)  # Предположим, что крепость всегда построена
    def attack(self, target):
        if isinstance(target, Unit):  # Проверяем, является ли цель экземпляром Unit
            print(f"{self.get_name()} атакует {target.get_name()} из пушек")
            target.receive_damage()
            print(f"Здоровье {target.get_name()} после атаки {self.get_name()}: {target.get_hp()}")
        else:
            print(f"{self.get_name()} не может атаковать {target.get_name()}, так как это не юнит")

# Класс MobileHome, который реализует Moveable
class MobileHome(Building, Moveable):
    def __init__(self, object_id, name, x, y):
        super().__init__(object_id, name, x, y)
        self.set_built(True)  # Предположим, что дом всегда построен
    def move(self, x, y):
        print(f"{self.get_name()} перемещается на координаты ({x}, {y})")
        self._x = x
        self._y = y

# Пример
def main():
    archer = Archer(1, "Лучник", 0, 0, 100)
    fort = Fort(2, "Крепость", 10, 10)
    mobile_home = MobileHome(3, "Дом на колесах", 5, 5)
    archer.move(3, 3)
    archer.attack(fort)  # Попытка атаковать объект типа Fort
    fort.attack(archer)  # Атака крепости на лучника
    mobile_home.move(7, 8)
    Building.is_built(fort)

if __name__ == "__main__":
    main()
