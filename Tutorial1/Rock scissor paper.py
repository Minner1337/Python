import random

r = "Rock"
s = "Scissor"
p = "Paper"
at = "Attacktype"
nr = 0
rhp = 12
shp = 12
php = 12



nr = random.random()

if nr <= 0.33:
    at = r
elif nr >= 0.66:
    at = p
else:
    at = s

print("Your attack type is:", at, "Wich monster do you want to attack?")
print("[1]", r)
print("[2]", p)
print("[3]", s)

answer = input()
answer = int(answer)

if answer == 1 and at == r:
    rhp = -2
    print("Your attack was successful.")
    print(r, "has", rhp, "HP left.")
elif answer == 2 and at == r:
    php = -1
    print("Your attack was not very effective.")
    print(p, "has", php, "HP left.")
elif answer == 3 and at == r:
    shp = -4
    print("Your attack was very effective.")
    print(s, "has", shp, "HP left.")
elif answer == 1 and at == p:
    rhp = -4
    print("Your attack was very effective.")
    print(r, "has", rhp, "HP left.")
elif answer == 2 and at == p:
    php = -2
    print("Your attack was successful.")
    print(p, "has", php, "HP left.")
elif answer == 3 and at == p:
    shp = -1
    print("Your attack was not very effective.")
    print(s, "has", shp, "HP left.")
elif answer == 1 and at == s:
    rhp = -1
    print("Your attack was not very effective.")
    print(r, "has", rhp, "HP left.")
elif answer == 2 and at == s:
    php = -4
    print("Your attack was very effective.")
    print(p, "has", php, "HP left.")
elif answer == 3 and at == s:
    shp = -2
    print("Your attack was successful.")
    print(s, "has", shp, "HP left.")
else:
    print("You cannot attack that.")