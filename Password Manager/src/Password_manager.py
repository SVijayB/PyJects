import sqlite3
from getpass import getpass
import os

def get_password(account):
    command = 'SELECT * from DETAILS WHERE ACCOUNT = "' + account + '"'
    cursor = conn.execute(command)
    for row in cursor:
        username = row[1]
        password = row[2]
    return [username, password]

def add_password(account, username, password):
    command = 'INSERT INTO DETAILS (ACCOUNT,USERNAME,PASSWORD) VALUES("'+account+'","'+username+'","'+password+'");'
    conn.execute(command)
    conn.commit()

def update_password(account, password):
    command = 'UPDATE DETAILS set PASSWORD = "' + password + '" where ACCOUNT = "' + account + '"'
    conn.execute(command)
    conn.commit()
    print(account + " password has been updated successfully.")

def delete_account(account):
    command = 'DELETE from DETAILS where ACCOUNT = "' + account + '"'
    conn.execute(command)
    conn.commit()
    print(account + " details has been deleted from the database successfully.")

def get_all():
    cursor.execute("SELECT * from DETAILS")
    data = cursor.fetchall()
    if len(data) == 0:
        print('No Data Present')
    else:
        for row in data:
            print("Account : ", row[0])
            print("Username : ", row[1])
            print("Password : ", row[2])
            print()

def check_details(account):
    cursor.execute("SELECT ACCOUNT from DETAILS where ACCOUNT = ?", (account,))
    data = cursor.fetchall()
    if len(data) == 0:
        print('There are no details for %s' % account)
        return False
    else:
        return True

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