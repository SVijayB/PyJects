import sqlite3
from getpass import getpass
import os
from Modules.Functions import *
from Modules.Colours import *

conn = sqlite3.connect('../assets/Database.db')
cursor = conn.cursor()

if __name__ == "__main__":
    try:
        conn.execute('''CREATE TABLE DETAILS 
            (ACCOUNT TEXT PRIMARY KEY NOT NULL, 
            USERNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL)''')
    except:
        pass

    os.system('cls')
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    print(output)
    
    while True:
        cyan("-" * 15)
        print("""What would you like to do?
        1) Add an account
        2) Retrieve an account
        3) Retrieve all account details
        4) Update Password
        5) Delete an account
        6) Destroy all data present
        7) Clear Screen
        8) Exit""")
        choice = int(input("> "))
        cyan("-" * 15)

        if(choice==1):
            account = input("Enter the account you are saving details for (Eg : Gmail) \n> ")
            cursor.execute("SELECT ACCOUNT from DETAILS where ACCOUNT = ?", (account,))
            data = cursor.fetchall()
            account = account.capitalize()
            if (len(data)==0):
                username = input("Enter username \n> ")
                password = getpass("Enter password \n> ")
                add_password(account, username, password)
                green("\n" + account + " details has been successfully stored\n")
            else:
                print("Account details for {} already exists.".format(account))

        elif (choice == 2):
            account = input("What is the name of the account? \n> ")
            account = account.capitalize()
            flag = check_details(account)
            if flag:
                username, password = get_password(account)
                green("\n" + account.capitalize() + " Details : ")
                print("Username :", username)
                print("Password :", password)
        
        elif (choice == 3):
            get_all()
        
        elif (choice == 4):
            account = input("What is the name of the account you want to update details for? \n> ")
            account = account.capitalize()
            flag = check_details(account)
            if flag:
                password = getpass("Enter new password :\n> ")
                update_password(account, password)
            else:
                pass

        elif (choice == 5):
            account = input("What is the name of the account you want to delete? \n> ")
            account = account.capitalize()
            flag = check_details(account)
            if flag:
                delete_account(account)
            else:
                pass

        elif (choice == 6):
            destroy()

        elif (choice == 7):
            os.system('cls')

        elif(choice == 8):
            green("\n-----x Thanks for using Password_manager x-----")
            grey("Press any key to exit...")
            input()
            conn.close()
            break

        else:
            red("\nERROR : Invalid choice\n")