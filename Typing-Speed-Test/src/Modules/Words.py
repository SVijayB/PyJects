import urllib.request
import random
import time
from Modules.TestWindow import testwindow

def words(choice):
    choice = int(choice)
    data = open("../assets/dictionary.txt","r").read()
    words = data.splitlines()
    basic_words = []
    j = 3
    if(choice == 1):
        i = 20
    elif(choice == 2):
        i = 7
    elif(choice == 3):
        i = 12; j = 5
    for x in words:
        if(len(x) < i and len(x) > j):
            basic_words.append(x)
    result = random.sample(basic_words,200)
    testwindow(result)