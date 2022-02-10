from classes_module import Barbarian, Archer, Yoda, Hero, TrollKing
from random import random


def intro():
    heroName = input(
        "'Oy, adventurer! Not seen ye 'round these parts. What's yer name?! ")
    print()
    print("Well then, {}, if you're looking for trouble, look no further! This here dungeon is riddled with strange creatures! Good luck on yer 'venturin'.\n".format(heroName))
    return Hero(heroName)


def battle(monster):
    print("\nYou encountered {}. Prepare to fight!\n".format(monster.getName()))
    print(monster.welcome())
    while hero.getHP() > 0 and monster.getHP() > 0:
        monster.reduceHealthPoints(hero.attack())
        if monster.getHP() <= 0:
            print("\n{} has been defeated!\n".format(monster.getName()))
            break
        hero.reduceHealthPoints(monster.attack())
    print()
    hero.addResource(monster.getResource())
    print()


def randomEncounter():
    randNum = random()
    if steps != 10:
        if randNum < .2:
            return Barbarian()
        elif randNum >= .2 and randNum < .5:
            return Archer()
        elif randNum >= .5 and randNum < .7:
            return Yoda()
        else:
            None
    else:
        return TrollKing()


def moveForward():
    proceed = input("Would you like to move forward with your journey? (y/n) ")
    return proceed


hero = intro()

steps = 0
finalStep = 10
heroDead = False

fileName = "steps.txt"
f = open(fileName, 'r')

while steps != finalStep:
    print("Steps: {}".format(steps))
    if steps == finalStep - 1:
        hero.setHP()
        print(hero.welcome())
    print(f.readline())
    if moveForward().casefold() == 'y'.casefold():
        steps += 1
        monster = randomEncounter()
        if monster != None:
            battle(monster)
            if hero.getHP() <= 0:
                heroDead = True
                break

f.close()

if heroDead == True:
    print("You FAILED!!")
else:
    print("Hero's HP: {}".format(hero.getHP()))
    print("Hero's gold: {}".format(hero.getResource()))
