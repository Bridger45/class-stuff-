#bridger hope
#10/18
#two way if statment

num = int(input("enter a number"))

if num%2 == 0:
    print("that number is an even number")
else:
    print("that number is an odd number")

print ("the program is finished")


num1 = float(input("pick a number"))
num2 = float(input("pick a number"))

if num1 <= num2:
    if num1 == num2:
        print("equal")
    else:
        print("not equal")
        if num1 < num2:
            print("less than")
        else:
            if num1 > num2:
                print("greater than")
print("done")
