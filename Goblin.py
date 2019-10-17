import random

numberMonster = 0

class Monster:
    def __init__(mon, Name, Type, HP, Atk, Acc, Ini):
        mon.Name = Name
        mon.Type = Type
        mon.HP = HP
        mon.Atk = Atk
        mon.Acc = Acc
        mon.Ini = Ini



def monAdd(mon):
    print("Added a " + mon.Name)
    print("A " + mon.Type + "-type monster!")
    print("Health: " + str(mon.HP))
    print("Damage: " + str(mon.Atk))
    print("Accuracy: " + str(mon.Acc))
    print("Initiative: " + str(mon.Ini))

def startGame():
    global numberMonster
    while True:
        try:
            numberMonster = int(input("How many monsters?"))
        except(ValueError):
            print("Enter a number!")
        else:
            print(numberMonster)
            break

gob = Monster("Goblin", "goblin", 2, 3, 1, 2)
zom = Monster("Zombie", "undead", 3, 4, 3, 1)
kob = Monster("Kobold", "reptile", 1, 3, 2, 3)
monsterList = [gob, kob, zom]

def buildEncounter():
    global monsterList
    global numberMonster
    while numberMonster > 0:
        monAdd(random.choice(monsterList))
        numberMonster = numberMonster - 1
    else:
        print("Monsters added!")


startGame()
buildEncounter()
#print(encMonsters)







