#bridger hope
# 10/18
import random

mHealth = 100
pHealth =  100


choice = input("attack or run")

while choice == "attack":
    pDamage = random.randrange(0, 25)
    mDamage = random.randrange(0,50)
    print("you attack the monster for",pDamage)
    mHealth -= pDamage
    if mHealth >= 0:
        print("the monster attacks you for", mDamage)
        pHealth -= mDamage
    if pHealth <= 0:
        win = 0
        print("you got reckt")
        break
    elif mHealth <= 0:
        win = 1
        print("you reckt the monster")
        break
    elif pHealth >= 0 and mHealth >= 0:
        print("you have",pHealth,"health")
        print("the monster has",mHealth,"health")
        choice = input("attack or run")
        if choice != "attack" or choice != "run":
            print("not sure what that is, but i think you meant attack")
            choice = "attack"
            continue
        else:
            continue
        
        

if choice == "run":
    print("you are a coward\n the monster cathes up to you and it eats you")
    win = 0
if win == 0:
    print("game over")
else:
    print("You won!!!")
