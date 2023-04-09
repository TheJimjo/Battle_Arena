from player import *
from monster import *

def character_creation():
    print("Welcome to the most simple combat sim ever. What would you like your name to be?")
    selection = input("Selection: ")
    player = Fighter(selection, 20, 20,  0, 5, "greatsword", "simple", 0)
    print(player)

def player_attack_monster(player, monster):
    print(f"\nYou attack the {monster.name} for {player.damage}")
    current_monster_hp = monster.hp - player.damage + monster.dr
    print(f"\n\nThe {monster.name}'s hit points were reduced from {monster.hp} to "
          f"{current_monster_hp}")
    monster.hp = current_monster_hp
    if monster.hp <= 0:
        print(f"\nThe {monster.name} has been defeated! You are awarded {monster.gold} for winning.")
        player.gold += monster.gold
        merchant_or_arena(player)
    else:
        monster_attack_player(player, monster)


def monster_attack_player(player, monster):
    print(f"\n{monster.name} attacks you for {monster.damage}")
    current_player_hp = player.hp - monster.damage + player.dr
    print(f"\n\nYour hit points were reduced from {player.hp} to "
          f"{current_player_hp}")
    player.hp = current_player_hp
    if player.hp <= 0:
        print(f"\nYou have fallen unconscious and are rushed to the cleric. They heal you, but you have lost all"
              f"of your gold.")
        player.gold = 0
        merchant_or_arena(player)
    else:
        attack_or_run(player, monster)


def attack_or_run(player, monster):
    print("Would you like to (1) attack or (2) run?")
    selection = input("Selection")
    while selection not in ["1", "2"]:
        print("Please select (1) attack or (2) run.")
    if selection == "1":
        player_attack_monster(player, monster)
    else:
        print("You scramble away and are healed by the cleric. You forfeit half your gold.")
        player.gold = player.gold / 2
        player.hp = player.maxhp
        merchant_or_arena(player)


merchant_wares = {1: ["magical greatsword", 10, 10],
                  2: ["legendary greatsword", 100, 100],
                  3: ["magical armor", 10, 5],
                  4: ["legendary armor", 100, 50]}

def equipment_shop(player):
    print("The merchant has the following available:")
    for item in merchant_wares:
        print(f"\nA {merchant_wares[item][0]} costing {merchant_wares[item][1]} gold and providing a bonus of "
              f"{merchant_wares[item][2]} to either damage or damage reduction (weapon gives damage, armor gives "
              f"damage reduction.")
    print("Would you like to purchase an item? (1) Yes or (2) No")
    selection = input("Selection: ")
    while selection not in ["1", "2"]:
        equipment_shop(player)
    if selection == "1":
        equipment_purchase(player)
    else:
        merchant_or_arena(player)


def equipment_purchase(player):
    for item in merchant_wares:
        print(f"\n{item}: {merchant_wares[item][0]}")
    print(f"\nYou currently have {player.gold} available. Which item would you like to purchase? Please select a "
          f"corresponding number.")
    selection = input("Selection: ")
    while selection not in merchant_wares.keys():
        equipment_purchase(player)
    while player.gold < merchant_wares[int(selection)][1]:


def merchant_or_arena(player):
    print("Would you like to visit the (1) merchant or the (2) arena?")
    selection = input("Selection: ")
    while selection not in ["1", "2"]:
        merchant_or_arena(player)
    if selection == "1":
        equipment_shop(player)


