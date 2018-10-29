#bridger hope
#10/18
#infinite loops


##loops = 0
##while True:
##    print("i have looped",loops,"times")
##    loops += 1
##    if loops==10000:
##        break

##count = 0
##while True:
##    count += 1
##    if count > 100:
##        break
##    if count == 5 or count == 25 or count == 50:
##        continue
##    print(count)
##
##input("\n\n press enter to exit")

##i="enter"
##while i == 1000:
##    print("looping")
##    x=input("do you want to keep looping: yes or no")
##    if x == "yes":
##        continue
##    else:
##        i = " "

print("Your lone hero is surrounded by a massive army of trolls")
print("Their decaying green bodies strecth out, melting in the horizon.")
print("Your hero unsheathes his sword for the last fight of his life. \n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage
    print("Your hero seings and defeats an evil troll," \
          "but takes", damage, "damage points.\n")



print(" Your hero foight valiantly and defeated", trolls, "trolls.")
print("but alas, your hero is no more.")

input("\n\n press enter to end")
