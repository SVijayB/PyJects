import sqlite3
from getpass import getpass
import os

conn = sqlite3.connect('Password Manager\src\Database.db')
cursor = conn.cursor()

if __name__ == "__main__":
    try:
        conn.execute('''CREATE TABLE DETAILS 
            (ACCOUNT TEXT PRIMARY KEY NOT NULL, 
            USERNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL)''')
        print("Your locker has been created. \nWhat would you like to do?")
    except:
        print("What would you like to do?")
    
    while True:
        print("\n" + "*" * 15)
        print("1) Retrieve an account")
        print("2) Retrieve all account details")
        print("3) Store account details")
        print("4) Update Password")
        print("5) Delete an account")
        print("6) Exit")
        choice = input("> ")

        if (choice == 1):
            account = input("What is the name of the account? \n> ")
            flag = check_details(account)
            if flag:
                username, password = get_password(account)
                print(account.capitalize() + " Details : ")
                print("Username : ", username)
                print("Password : ", password)

        elif (choice == 2):
            get_all()

        elif(choice==3):
            account = input("Enter the account you are saving details for (Eg : Gmail) \n> ")
            cursor.execute("SELECT ACCOUNT from DETAILS where ACCOUNT = ?", (account,))
            data = cursor.fetchall()
            if (len(data)==0):
                username = input("Enter username \n> ")
                password = getpass("Enter password \n> ")
                if username == '' or password == '':
                    print("Your username or password is empty.")
                else:
                    add_password(account, username, password)
                    print("\n" + account.capitalize() + " password stored\n")
            else:
                print("Account details for {} already exists.".format(account))

        elif (choice == 4):
            account = input("What is the name of the account you want to update details for? \n> ")
            flag = check_details(account)
            if flag:
                password = getpass("Enter new password :\n> ")
                update_password(account, password)
            else:
                print("Account does not exist")

        elif (choice == 5):
            account = input("What is the name of the account you want to delete? \n> ")
            flag = check_details(account)
            if flag:
                delete_account(account)
            else:
                print("Account does not exist")

        elif(choice==6):
            print("\nThanks for using Password_manager.")
            conn.close()
            break