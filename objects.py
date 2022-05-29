# Object classes used with tests

# General variable names
# name - name of the object
# idn - ID number of the object

# Super classes

# Super class for creature units
class Unit:
    def __init__(self, name, idn):
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        return self.__idn

    def __str__(self):
        return self.__name

# Super class for creature types
class CreatureType:
    def __init__(self, name, idn):
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        return self.__idn

    def __str__(self):
        return self.__name

# Super class for items
class Item:
    def __init__(self, name, idn):
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        return self.__idn

    def __str__(self):
        return self.__name

# Super class for abilities
class Ability:
    def __init__(self, name, idn):
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        return self.__idn

    def __str__(self):
        return self.__name

# Super class for inventories
class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__items = []

    def getCapacity(self):
        return self.__capacity

    def getItems(self):
        return self.__items

# Normal classes

# Playable character class, extends Unit super class
class PC(Unit):
    def __init__(self, name, idn):
        super().__init__(name, idn)

# Non-playable character class, extends Unit super class
class NPC(Unit):
    def __init__(self, name, idn, creature_type):
        super().__init__(name, idn)
        self.__creature_type = creature_type

# Weapon class, extends Item super class
class Weapon(Item):
    def __init__(self, name, idn, min_dam, max_dam, speed):
        super().__init__(name, idn)
        self.__min_dam = min_dam
        self.__max_dam = max_dam
        self.__speed = speed

    def getMinMax(self):
        return self.__min_dam, self.__max_dam

# Armour class, extends Item super class
class Armour(Item):
    def __init__(self, name, idn, armour_value):
        super().__init__(name, idn)
        self.__armour_value = armour_value

# Potion class, extends Item super class
class Potion(Item):
    def __init__(self, name, idn, effect, amount):
        super().__init__(name, idn)
        self.__effect = effect
        self.__amount = amount
