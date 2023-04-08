class Fighter:
    def __init__(self, name="nobody", hp=0, dr=0, damage=0, weapon="none", armor="none", gold=0):
        self.name = name
        self.hp = hp
        self.dr = dr
        self.damage = damage
        self.weapon = weapon
        self.armor = armor
        self.gold = gold

    def __repr__(self):
        return f"\n{self.name} has {self.hp} hit points, wears {self.armor} and is wielding a {self.weapon}." \
               f"\nThey deal {self.damage} damage, have {self.dr} damage reduction and {self.gold} gold."


def character_creation():
    print("Welcome to the most simple combat sim ever. What would you like your name to be?")
    selection = input("Selection: ")
    player = Fighter(selection, 20, 0, 5, "sword", "studded leather armor", 0)
    print(player)