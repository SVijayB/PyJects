import os
import shutil
import sys
import time

if __name__ == "__main__":
    os.system('cls')
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    print(output)
    print("\n"+"-"*20)
    print("SAFE HAVEN")
    time.sleep(1)
    secret = input("\nEnter the address of the folder you want to hide \n> ")
    location = input("\nWhere would you like us to create your secure folder \n> ")
    try:
        password = int(input("\nEnter the password (Only numbers)\n> "))
    except:
        print("ERROR : ENTER ONLY NUMBERS")
        input("Press enter to exit...")
        sys.exit(0)

    location = os.path.join(location,"Safe-Haven")
    try:
        os.mkdir(location)
    except:
        print("ERROR : SAFE-HEAVEN ALREADY EXISTS...\nPICK A DIFFERENT FOLDER TO SAVE TO.")
        input("Press enter to exit...")
        sys.exit(0)

    for index_1 in str(password):
        for index_2 in range(1,11):
            main = os.path.join(location,str(index_2))
            try:
                os.mkdir(main)
            except:
                pass
            for index_3 in range(1,11):
                sub = os.path.join(main,str(index_3))
                try:
                    os.mkdir(sub)
                except:
                    pass
                
        location = location + "/" + index_1

    print("\nFolders created successfully!\nFiles are being moved...")
    try:
        shutil.move(secret,location)
    except:
        print("ERROR UNABLE TO MOVE FILES")
        input("Press enter to exit...")
        sys.exit(0)

    print("Completed!")
    input("Press enter to exit...")