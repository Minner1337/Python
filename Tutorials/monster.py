from utilities import *

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