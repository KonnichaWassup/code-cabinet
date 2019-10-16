import random

class Monster:
    def __init__(mon, Name, Type, HP, Atk, Acc):
        mon.Name = Name
        mon.Type = Type
        mon.HP = HP
        mon.Atk = Atk
        mon.Acc = Acc

    def monGen(mon):
        print("Added a " + mon.Name)
        print("A " + mon.Type + "-type monster!")
        print("Health: " + str(mon.HP))
        print("Damage: " + str(mon.Atk))
        print("Accuracy: " + str(mon.Acc))

encounterMonsters = []

m1 = Monster("Goblin", "goblin", 2, 3, 4)

m1.monGen()
encounterMonsters.append(m1.Name)



print(encounterMonsters)





