"""
Dragon Battle!

Pits the player against a ferocious dragon. The player can 
choose between a sword attack, a powerful (Albeit not very
consistent) magic attack, a defensive manuever, and chugging
a health potion. The dragon randomly chooses attacks, so
players need to balance healing with their offensive strats.
"""

import random

# Setting all the constants the dragon will need
DRAGON_HEALTH_INIT = 50
DRAGON_BREATH_MAX = 7
DRAGON_BREATH_MIN = 5
DRAGON_BREATH_CHANCE = .15
DRAGON_CLAW_MAX = 3
DRAGON_CLAW_MIN = 1
DRAGON_CLAW_CHANCE = .75
DRAGON_STATES = ["healthy","slightly wounded","getting weaker","near defeat"]

# Setting all of the hero's basic stats
HERO_HEALTH_INIT = 15
HERO_SWORD_MAX = 7
HERO_SWORD_MIN = 3
HERO_SPELL_MAX = 10
HERO_SPELL_MIN = 0
HERO_HEAL_MAX = 6
HERO_HEAL_MIN = 1

def main():
    # Initializing the health and dragon state
    dragon_health = DRAGON_HEALTH_INIT
    dragon_state = DRAGON_STATES[0]
    hero_health = HERO_HEALTH_INIT
    hero_defending = False

    print("You stand off against a dangerous dragon! It bellows angrily, and readies its claws")
    while (hero_health > 0) and (dragon_health > 0):
        # The hero goes first. We start by presenting the player with their four options
        print("You currently have "+str(hero_health)+" health remaining! The dragon appears to be "+str(dragon_state)+".")
        print("[1] Attack  [2] Magic  [3] Defend  [4] Heal")
        choice = int(input("What would you like to do? "))
        while not input_is_valid(choice):
            choice = int(input("That's not an option! Pick another choice: "))
        # If the input was valid (1, 2, 3, or 4), then we continue with the turn.
        print("")
        if (choice == 1) or (choice == 2):
            # Attack and Magic do the same thing, just with different damage ranges
            dragon_health -= hero_attack(choice)
            dragon_state = set_dragon_state(dragon_health)
        elif choice == 3:
            # Defend just blocks the next dragon attack. Honestly not very useful right now
            print("You raise your shield, bracing for the next attack!")
            hero_defending = True
        elif choice == 4:
            # This heals the player for a random amount
            hero_health += hero_heal()
        if dragon_health > 0:
            # The dragon always goes after the hero, but if the dragon runs out of health, it shouldn't get a turn
            hero_health -= dragon_turn(hero_defending)
        # Resetting the defending state to False, otherwise, you'd be blocking forever
        hero_defending = False
        print("")
    if hero_health > 0:
        print("The dragon is slain! A hero is you!")
    elif dragon_health > 0:
        print("You are too weak to carry on! \nGAME OVER.")
    else:
        print("Somehow you and the dragon slew each other. This shouldn't be possible, so congrats?")


def hero_attack(choice):
    # We use the attack or spell's minimum and maximum values to get a random damage number, then send the damage value back out to our main function
    damage = 0
    if choice == 1:
        damage = random.randint(HERO_SWORD_MIN,HERO_SWORD_MAX)
        print("You slash at the beast to deal "+str(damage)+" damage!")
    elif choice == 2:
        damage = random.randint(HERO_SPELL_MIN,HERO_SPELL_MAX)
        print("You fire a powerful spell to deal "+str(damage)+" damage!")
    return damage

def hero_heal():
    # We use the heal's minimum and maximum values to get a random heal number, then send that value back out to our main function
    heal = random.randint(HERO_HEAL_MIN,HERO_HEAL_MAX)
    print("You quickly chug a potion, healing "+str(heal)+" points of damage!")
    return heal

def set_dragon_state(dragon_health):
    # This obfusciates the dragon's health, to create a bit o' tension
    if dragon_health > (DRAGON_HEALTH_INIT * .75):
        return DRAGON_STATES[0]
    elif dragon_health > (DRAGON_HEALTH_INIT * .5):
        return DRAGON_STATES[1]
    elif dragon_health > (DRAGON_HEALTH_INIT * .25):
        return DRAGON_STATES[2]
    else:
        return DRAGON_STATES[3]

def dragon_turn(hero_defending):
    # We use the fire breath or claw's minimum and maximum values to get a random damage number, then send the damage value back out to our main function
    dice_roll = random.random()
    if dice_roll < DRAGON_BREATH_CHANCE:
        if hero_defending:
            # If the hero is defending, no damage is dealt
            print("The dragon breathes a powerful flame, but you blocked it with your shield!")
            return 0
        else:
            damage = random.randint(DRAGON_BREATH_MIN,DRAGON_BREATH_MAX)
            print("The dragon breaths a powerful flame, dealing "+str(damage)+" damage!")
            return damage
    elif dice_roll < DRAGON_CLAW_CHANCE:
        if hero_defending:
            # If the hero is defending, no damage is dealt
            print("The dragon strikes at you, but you blocked it with your shield!")
            return 0
        else:
            damage = random.randint(DRAGON_CLAW_MIN,DRAGON_CLAW_MAX)
            print("The dragon strikes you with its claw to deal "+str(damage)+" damage!")
            return damage
    else:
        print("The dragon roars angrily!")
        return 0

def input_is_valid(choice):
    if 0 < choice < 5:
        return True
    else:
        return False

if __name__ == "__main__":
    main()