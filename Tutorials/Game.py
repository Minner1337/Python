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

    while True:

        print("Wich attack type do you want to use? \n", text, "\n")

        answer = input()

        if answer == w:
            chosentype = w
            break
        elif answer == f:
            chosentype = f
            break
        elif answer == p:
            chosentype = p
            break
        else:
            print("This attacktype doesnt exist.")
            continue

    while True:

        print("Wich monster do you want to attack? \n", text, "\n")

        answer = input()

        if answer == w:
            monstertype = Water
            break
        elif answer == f:
            monstertype = Fire
            break
        elif answer == p:
            monstertype = Plant
            break
        else:
            print("This monster doesnt exist.")
            continue

    monstertype.hit(chosentype)

    if Fire.hp <= 0 and Water.hp <= 0 and Plant.hp <= 0:
        break

print("Win!")