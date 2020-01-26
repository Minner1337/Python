import random
from utilities import *
from monster import Monster, get_type_advantage

Water = Monster(w, 10)
Fire = Monster(f, 10)
Plant = Monster(p, 10)
monsterlist = [w, f, p]

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