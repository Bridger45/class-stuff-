#Bridger Hope
#9/13/18
#get name function
import math
def  get_name(name_input):


#ask user for name
       name = name_input
       name = name.lower()
       name = name.title()
 #display name
       print("the name you entered was", name)
#verify name
       #input("is this correct yes or no")



print("this is our function")
name  = input("whats your name")
get_name(name)

# calulate the area of a circle
##def areaOfCircle(radius1):
##    PI = 3.14159265
#1 get a radius
    #radius = radius1
    
#2 compute an area
   # radius = float(radius)
    #area = radius*radius*PI
#3 display info back
   # print("the area of theh circle is: ",area)

    
#radiusx = input("what is the radius?")
#areaOfCircle(radiusx)

##def pythagoras_therom():
       #a^2+b^2=c^2
##       a = float(input("enter  the first side of the triangle"))
##       b = float(input("enter the second side of the triangle"))
##       c = a*a+b*b
##       c = math.sqrt(c)
##       print("The third side is", c)

##pythagoras_therom()


def add_numbers(x,y):
       num1 = x
       num2 = y
       num3 = int(num1)+int(num2)
       print(num1, ",this is num1")
       print(num2, ",this is num2")
       return num3

x = input("enter a number")
y = input("enter a second number")
num4 = add_numbers() #num4 = num3
print("the sum of your numbers is", num4)

