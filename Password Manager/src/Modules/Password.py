from Modules.Colours import *
from cryptography.fernet import Fernet

def password_function():

    file = open('../temp/key.txt','rb')
    key = file.read()
    file.close()

    try:
        file = open('../temp/password.txt', 'r')
        password = file.read()
        while(True):
            entered_password = input("Enter your password \n> ")
            if(password == entered_password):
                green("Logged in successfully")
                grey("Press any key to continue...")
                input()
                break
            else:
                red("Incorrect password")
    except:
        green("PASSWORD MANAGER")
        cyan("-" * 25)
        print("Since, this is the first time you are using Password_manager, Create a password.")
        red("DO NOT FORGET THIS PASSWORD. YOU CANNOT CHANGE IT LATER.")
        
        password = input("Enter your password \n> ")
        fernet = Fernet(key)
        encrypted = fernet.encrypt(password)

        file = open('../temp/password.txt', 'w')
        file.write(encrypted)
        green("Your password has been saved successfully")
        cyan("Relaunch the application to continue.")
        grey("Press enter to exit...")
        input()
        sys.exit(0)