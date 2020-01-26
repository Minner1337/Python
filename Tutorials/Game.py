import random

chosentype = ""
monstertype = ""
damage = 4
w = "Water"
f = "Fire"
p = "Plant"
monsterlist = [w, f, p]

def get_type_advantage(attacktype, monstertype):

    returndamage = 0
    effectiveness = ""

    if (attacktype == w and monstertype == f) or (attacktype == f and monstertype == p) or (attacktype == p and monstertype == w):
        returndamage = damage*2
        effectiveness = "very effetive"
    elif attacktype == monstertype:
        returndamage = damage
        effectiveness = "successfull"
    else:
        returndamage = damage/2
        effectiveness = "not effective"
    
    print("The attack was", effectiveness, ",you've done ", returndamage, "damage.")

    return returndamage

class Monster:
    def __init__(self, t, hp):
        self.type = t
        self.hp = hp
    def hit(self, attacktype):
        print("You hit", self.type+"monster with a" ,attacktype, "type attack.")

        self.hp -= get_type_advantage(attacktype, self.type)

        if self.hp <= 0:
            self.hp = 0

        print("The", self.type+ "monster now has", self.hp, "HP left.")

Water = Monster(w, 10)
Fire = Monster(f, 10)
Plant = Monster(p, 10)

while True:

    text =""

    for monster in monsterlist:
        text+= "\n"+monster

    print("Wich attack type do you want to use? \n", text, "\n")

    answer = input()

    if answer == w:
        chosentype = w
    elif answer == f:
        chosentype = f
    elif answer == p:
        chosentype = p
    else:
        print("This attacktype doesnt exist.")

    print("Wich monster do you want to attack? \n", text, "\n")

    answer = input()

    if answer == w:
        monstertype = Water
    elif answer == f:
        monstertype = Fire
    elif answer == p:
        monstertype = Plant
    else:
        print("This monster doesnt exist.")

    monstertype.hit(chosentype)

    if Fire.hp <= 0 and Water.hp <= 0 and Plant.hp <= 0:
        break

print("Win!")