class Monster:
    def __init__(self, name="nobody", hp=0, dr=0, damage=0, gold=0):
        self.name = name
        self.hp = hp
        self.dr = dr
        self.damage = damage
        self.gold = gold

    def __repr__(self):
        return(f"\n{self.name} has {self.hp} hit points and {self.dr} damage reduction. They deal {self.damage} damage"
               f"and are work {self.gold} gold.")

    def monster_selection(self):
        pass  # This may not need to be a method in the monster class. Want monsters to be generated as select, not
# not pre-generated.


kobold = Monster("kobold", 10, 0, 2, 10)
yeti = Monster("yeti", 50, 10, 10, 50)
dragon = Monster("dragon", 200, 20, 20, 250)

monsters = [kobold, yeti, dragon]