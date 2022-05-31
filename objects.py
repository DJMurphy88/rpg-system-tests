# Object classes used with tests

# Super classes

# Super class for Units
class Unit:
    def __init__(self, name, idn):
        """
        Super class for creature units

        :param name: The name of the unit
        :type name: str
        :param idn: The Identification Number of the unit
        :type idn: int
        """
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        """
        :return: The Identification Number of the unit
        """
        return self.__idn

    def __str__(self):
        return self.__name

# Super class for creature types
class CreatureType:
    def __init__(self, name, idn):
        """
        Super class for creature types

        :param name: the name of the unit
        :type name: str
        :param idn: the Identification Number of the unit
        :type idn: int
        """
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        """
        :return: idn, the Identification Number of the unit
        """
        return self.__idn

    def __str__(self):
        return self.__name

# Super class for items
class Item:
    def __init__(self, name, idn):
        """
        Super class for Items

        :param name: The name of the unit
        :type name: str
        :param idn: The Identification Number of the unit
        :type idn: int
        """
        self.__name = name
        self.__idn = idn

    def getIDN(self):
        """
        :return: idn, the Identification Number of the unit
        """
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
        """
        :param name: The Name of the weapon
        :type name: str
        :param idn: The Identification Number of the weapon
        :type idn: int
        :param min_dam: The minimum damage
        :type min_dam: int
        :param max_dam: The maximum damage
        :type max_dam: int
        :param speed: Weapon speed
        :type speed: int
        """
        super().__init__(name, idn)
        self.__min_dam = min_dam
        self.__max_dam = max_dam
        self.__speed = speed

    def getMinMax(self):
        """
        :return: A tuple of the minimum and maximum damage
        """
        return self.__min_dam, self.__max_dam

# Armour class, extends Item super class
class Armour(Item):
    def __init__(self, name, idn, armour_value):
        """
        :param name: The name of the armour
        :type name: str
        :param idn: The Identification Number of the armour
        :type idn: int
        :param armour_value: The amount of armour value
        :type armour_value: int
        """
        super().__init__(name, idn)
        self.__armour_value = armour_value

# Potion class, extends Item super class
class Potion(Item):
    def __init__(self, name, idn, effect, amount):
        """
        :param name: The name of the potion
        :type name: str
        :param idn: The Identification Number of the potion
        :type idn: int
        :param effect: The effect the potion has
        :type effect: Ability
        :param amount: The amount it effects by
        :type amount: int
        """
        super().__init__(name, idn)
        self.__effect = effect
        self.__amount = amount
