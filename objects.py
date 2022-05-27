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

# Playable character class, extends unit super class
class PC(Unit):
    def __init__(self, name, idn):
        super().__init__(name, idn)

# Non-playable character class, extends unit super class
class NPC(Unit):
    def __init__(self, name, idn, creature_type):
        super().__init__(name, idn)
        self.__creature_type = creature_type
