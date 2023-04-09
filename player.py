from monster import *

class Fighter:
    def __init__(self, name="nobody", maxhp = 0, hp=0, dr=0, damage=0, weapon="none", armor="none", gold=0):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.dr = dr
        self.damage = damage
        self.weapon = weapon
        self.armor = armor
        self.gold = gold

    def __repr__(self):
        return f"\n{self.name} has {self.hp} hit points, wears {self.armor} and is wielding a {self.weapon}." \
               f"\nThey deal {self.damage} damage, have {self.dr} damage reduction and {self.gold} gold."











