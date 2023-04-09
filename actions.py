from player import *
from monster import *

def character_creation():
    print("Welcome to the most simple combat sim ever. What would you like your name to be?")
    selection = input("Selection: ")
    player = Fighter(selection, 20, 20,  0, 5, "sword", "studded leather armor", 0)
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
        merchant_or_arena()
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
        merchant_or_arena()
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
        merchant_or_arena()


def merchant_or_arena():
    print("Would you like to visit the (1) merchant or the (2) arena?")
    selection = input("Selection: ")
    while selection not in ["1", "2"]:
        merchant_or_arena()
    if selection == "1":
        pass # Need logic to visit the merchant and buy wares.


