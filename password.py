#bridger hope
#10/18
#password progam

def check_account(username, password):
    username = username
    password = password
    enterUsername = input("enter your name")
    enterPassword = input("enter your password")
    if username == enterUsername and passord == enterPassword or enterUsername == "admin":
        return True
    else:
        print("usernaem or pssword is correct")
        check_account(username, password)

def get_password():
    print("your password must start with a captital letter \n and must contain at least 1 symbol \n and msut be at least 10 characters long")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password) >= 10:
        print("password is set")
        return password
    else:
        print("your password does not meet the requirements of our liking")
        get_password()



    
def get_username():
    print("your username can only contain numbers and letters\n can only contain 20 charecters \n must cantain at least 3 characters")
    username = input("enter your username")
    if username.isalnum() and len(username) >=3 and len(username)<=21:
        print("your username is set")
        return username
    else:
        print("your username does not meet the requirements of our liking")

def menu():
    choice = 0
    while choice == 0:
        print("to sign uo press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
    if choice == 1:
        print("choice 1")
        username = get_username()
        passweord = get_password()
        choice = 0
    elif choice == 2:
        print("choice 2")
        login = check_account()
        return password, username, login

def main():
    password, username, gotin = menu()

    if gotin == True:
            print("you got in")
    else:
            print("thats not right")
main()
