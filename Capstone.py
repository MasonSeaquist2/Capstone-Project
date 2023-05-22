    import random

# Variables
# total_number = 0
# current_number = 0
# List_Of_Numbers = []

# Input Variables
# rang = input("What is the Range")
# times = input("how many times")

# Rolling Code
# for i in range(int(times)):
#   Current_Number = random.randint(1, int(rang))
#    Total_Number = Current_Number + Total_Number
#    List_Of_Numbers.append(Current_Number)

# Printing the numbers
# List_Of_Numbers.sort()
# print(List_Of_Numbers)
# print(Total_Number)


# Define a list of monsters
monsters = ["goblin", "skeleton", "orc", "troll", "dragon"]

# Define a list of weapons
weapons = ["sword", "bow and arrow", "wand", "dagger", "mace"]

# Define a list of spells
spells = ["fireball", "lightning bolt", "magic missile", "ice storm", "healing"]
print("0 : Fireball : Roll an 9 or higher on a d20 to hit for 5d6 damage")
print("1 : Lighting bolt : Roll a 15 or higher on a d20 to hit for 8d8 damage")
print("2 : Magic Missile : 4d4 guaranteed damage")
print("3 : Ice Storm : Roll a 5 or higher on a d20 to hit for 3d8 damage")
print("4 : Healing : Heal 2d8 health")
spell_chosen = False
what_spell = ""
while not spell_chosen:
    what_spell = input("What spell would you like to use? (0-4) ")
    if what_spell == "0" or what_spell == "1" or what_spell == "2" or what_spell == "3" or what_spell == "4":
        spell_chosen = True
    else:
        print("Invalid choice")
character_spell = spells[int(what_spell)]
print("You will use the " + character_spell + " spell")

# Define a list of races
races = ["Human", "Elf", "Dwarf", "Gnome", "Half-Elf"]
print("\n0 : Humans get a +5 to health +2 to damage of both kinds")
print("1 : Elves get advantage on magic attack rolls")
print("2 : Dwarves get a +20 to health")
print("3 : Gnome get a +10 to health and a +4 to magic damage")
print("4 : Half-Elves get a +7 bonus to weapon damage")
race_chosen = False
what_race = ""
while not race_chosen:
    what_race = input("What race would you like to be? (0-4) ")
    if what_race == "0" or what_race == "1" or what_race == "2" or what_race == "3" or what_race == "4":
        race_chosen = True
    else:
        print("Invalid choice")
character_race = races[int(what_race)]
print("you are a " + character_race)


def roll_dice(number_of_rolls, dice_type):
    total_number = 0
    list_of_numbers = []
    for i in range(int(number_of_rolls)):
        current_number = random.randint(1, int(dice_type))
        total_number = current_number + total_number
        list_of_numbers.append(current_number)
    list_of_numbers.sort()
    print(list_of_numbers)
    print(total_number)
    return total_number


# Define a function to generate a random encounter
def generate_encounter():
    # Choose a random monster from the list
    monster = random.choice(monsters)

    # Choose a random weapon from the list
    weapon = random.choice(weapons)

    # Print out the encounter details
    print("\nYou have encountered a " + monster + "!")
    print("You draw your " + weapon + " and prepare to fight.")
    print("You also have the option to cast " + character_spell + " if you wish.")

    # Define player and monster health and damage
    player_health = 100
    monster_health = random.randint(50, 100)
    player_magic_damage = random.randint(10, 20)
    player_weapon_damage = random.randint(10, 20)
    monster_damage = random.randint(5, 15)

    # Begin combat loop
    while player_health > 0 and monster_health > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("1 : Attack with " + weapon)
        print("2 : Cast " + character_spell)
        choice = input("What do you want to do? ")
        if choice == "1":
            print("You attack the " + monster + " with your " + weapon + "!")
            monster_health -= player_weapon_damage
            print("The " + monster + " now has " + str(monster_health) + " health left.")
        elif choice == "2":
            if character_spell == "healing":
                print("You cast " + character_spell + "and heal yourself.")
                player_health += roll_dice(2, 8)
                if player_health > 100:
                    player_health = 100
                print("You now have " + str(player_health) + " health.")
            elif character_spell == "magic missile":
                print("You cast " + character_spell + " at the " + monster + "!")
                monster_health -= roll_dice(4, 4)
                print("The " + monster + " now has " + str(monster_health) + " health left.")
            elif character_spell == "lightning bolt":
                print("You cast " + character_spell + " at the " + monster + "!")
                if roll_dice(1, 20) < 15:
                    print("You missed!")
                else:
                    print("You hit!")
                    monster_health -= roll_dice(8, 8)
                    print("The " + monster + " now has " + str(monster_health) + " health left.")
            elif character_spell == "fireball":
                print("You cast " + character_spell + " at the " + monster + "!")
                if roll_dice(1, 20) < 9:
                    print("You missed!")
                else:
                    print("You hit!")
                    monster_health -= roll_dice(5, 6)
                    print("The " + monster + " now has " + str(monster_health) + " health left.")
            elif character_spell == "ice storm":
                print("You cast " + character_spell + " at the " + monster + "!")
                monster_health -= player_magic_damage
                print("The " + monster + " now has " + str(monster_health) + " health left.")
        else:
            print("Invalid choice. Try again.")
            continue

        # Check if the monster is defeated
        if monster_health <= 0:
            print("\nYou defeated the " + monster + "!")
            return

        # Monster's turn
        print("\nMonster's turn:")
        print("The " + monster + " attacks you!")
        player_health -= monster_damage
        print("You now have " + str(player_health) + " health.")

        # Check if the player is defeated
        if player_health <= 0:
            print("\nYou were defeated by the " + monster + ". Game over.")
            return


# start the game
generate_encounter()

