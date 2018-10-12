
age = input("what is your age?")


if age < "65" or age > "16" and age.isdigit():
    print("i can drive!!!")
elif age < "65" and age.isdigit():
    print("sorry mate you can't drive becaue you old")
elif age < "16" and age.isdigit():
    print ("you need to grow up")
else:
    print("you shouldn't be driving")
