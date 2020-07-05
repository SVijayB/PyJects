from Password_manager import * 

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