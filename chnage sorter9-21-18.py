#Bridger Hope
#9/18
#change sorter

def change():
    #1 get input form user how much change
    total_change =  int(input("How much change do you have?: "))
    #2 calulate total for q n d p
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickles = whats_left // 5
    whats_left = whats_left % 5
    pennys = whats_left
    #3 display it back to user
    print("Quaters: ",quarters, "\nDimes: ",dimes, "\nNickles: ",nickles,"\nPennys: ",pennys)

change()

def change2(total_change):
     #1 get input form user how much change
    total_change = total_change
    #2 calulate total for q n d p
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickles = whats_left // 5
    whats_left = whats_left % 5
    pennys = whats_left
    #3 return value
    return quarters, dimes, nickles, pennys
total_change = int(input("How much change do you have?: "))
quarters, dimes, nickles, pennys = change2(total_change)
print("Quaters: ",quarters, "\nDimes: ",dimes, "\nNickles: ",nickles,"\nPennys: ",pennys)



    
    
