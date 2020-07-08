from Password_manager import * 
from Modules.Colours import *

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
    green("\n" + account + " password has been updated successfully.\n")

def delete_account(account):
    command = 'DELETE from DETAILS where ACCOUNT = "' + account + '"'
    conn.execute(command)
    conn.commit()
    green("\n"+account + " details have been deleted from the database successfully.\n")

def get_all():
    print()
    cursor.execute("SELECT * from DETAILS")
    data = cursor.fetchall()
    if len(data) == 0:
        red("No Data Present\n")
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
        return False
    else:
        return True

def destroy():
    cursor.execute('DELETE from DETAILS;',)
    print("\nDelete",cursor.rowcount,"records\n")
    conn.commit()

def password_function():
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
        file = open('../temp/password.txt', 'w')
        file.write(password)
        green("Your password has been saved successfully")
        cyan("Relaunch the application to continue.")
        grey("Press enter to exit...")
        input()
        sys.exit(0)