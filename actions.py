from player import *
from monster import *


def start_game():
    print("Welcome to the most simple combat sim ever. What would you like your name to be?")
    selection = input("Selection: ")
    player = Fighter(selection, 50, 50,  0, 5, "greatsword", "simple armor", 500)
    print(player)
    merchant_or_arena(player)


def player_attack_monster(player, monster):
    print(f"\nYou attack the {monster.name} for {player.damage}")
    damage_calc = max(0, player.damage - monster.dr)
    if damage_calc > 0:
        current_monster_hp = monster.hp - damage_calc
        print(f"\nThe {monster.name}'s hit points were reduced from {monster.hp} to "
              f"{current_monster_hp}")
        monster.hp = current_monster_hp
    else:
        print(f"\nYour damage was reduced by {monster.dr} and is rendered ineffective.")
    if monster.hp <= 0:
        if monster.name == "dragon":
            print("\nCongratulations, you beat the dragon and have reached the end of the effort "
                  "I'm willing to keep putting into this. Well done!")
        else:
            print(f"\nThe {monster.name} has been defeated! You are awarded {monster.gold} gold for winning.")
            player.gold += monster.gold
            merchant_or_arena(player)
    else:
        monster_attack_player(player, monster)


def monster_attack_player(player, monster):
    print(f"\nThe {monster.name} attacks you for {monster.damage}")
    damage_calc = max(0, monster.damage - player.dr)
    if damage_calc > 0:
        current_player_hp = player.hp - damage_calc
        print(f"\nYour hit points were reduced from {player.hp} to "
              f"{current_player_hp}")
        player.hp = current_player_hp
    else:
        print(f"\nThe {monster.name}'s damage was reduced by {player.dr} and is rendered ineffective.")
    if player.hp <= 0:
        print(f"\nYou have fallen unconscious and are rushed to the cleric. They heal you, but you have lost all "
              f"of your gold.")
        player.gold = 0
        merchant_or_arena(player)
    else:
        attack_or_run(player, monster)


def attack_or_run(player, monster):
    print("\nWould you like to (1) attack or (2) run?")
    selection = input("Selection: ")
    while selection not in ["1", "2"]:
        print("Please select (1) attack or (2) run.")
    if selection == "1":
        player_attack_monster(player, monster)
    else:
        print("You scramble away and are healed by the cleric. You forfeit half your gold.")
        player.gold = player.gold / 2
        player.hp = player.maxhp
        merchant_or_arena(player)


merchant_wares = {1: ["magical greatsword", 10, 40, "weapon"],
                  2: ["legendary greatsword", 100, 150, "weapon"],
                  3: ["set of magical armor", 10, 10, "armor"],
                  4: ["set of legendary armor", 100, 50, "armor"]}


def equipment_shop(player):
    print("\nThe merchant has the following items available:")
    for item in merchant_wares:
        print(f"\nA {merchant_wares[item][0]} which costs {merchant_wares[item][1]} gold and provides a bonus of "
              f"{merchant_wares[item][2]} to either damage or damage reduction (weapon gives damage, armor gives "
              f"damage reduction.)")
    print(f"\nYou currently have {player.gold} gold available. Would you like to purchase an item? (1) Yes or (2) No")
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
    print(f"\nYou currently have {player.gold} gold available. Which item would you like to purchase? Please select a "
          f"corresponding number.")
    selection = int(input("Selection: "))
    while selection not in merchant_wares.keys():
        equipment_purchase(player)
    if player.gold < merchant_wares[selection][1]:
        print("\nYou do not have enough gold to afford that.")
        equipment_shop(player)
    else:
        player.gold -= merchant_wares[selection][1]
        print("Excellent choice. Your equipment and stats have been updated.")
        equipment_upgrade(player, merchant_wares[selection][0], merchant_wares[selection][2],
                          merchant_wares[selection][3], selection)


def equipment_upgrade(player, name, value, description, selection):
    if description == "weapon":
        player.damage = value
        player.weapon = name
        del merchant_wares[selection]
    else:
        player.dr = value
        player.armor = name
        del merchant_wares[selection]
    print(player)
    merchant_or_arena(player)


def merchant_or_arena(player):
    print("Would you like to visit the (1) merchant or the (2) arena?")
    selection = input("Selection: ")
    while selection not in ["1", "2"]:
        merchant_or_arena(player)
    if selection == "1":
        equipment_shop(player)
    else:
        monster_selection(player)


def monster_selection(player):
    options = {1: ["kobold", 10, 0, 2, 25],
               2: ["yeti", 50, 20, 10, 50],
               3: ["dragon", 200, 30, 75, 250]}
    print("Which Monster would you like to fight? Please select a number.")
    for option in options:
        print(f"{option}: {options[option][0]}")
    selection = int(input("Selection: "))
    while selection not in range(1, 4):
        monster_selection(player)
    monster = Monster(options[selection][0], options[selection][1], options[selection][2], options[selection][3],
                      options[selection][4])
    player.hp = player.maxhp
    player_attack_monster(player, monster)
