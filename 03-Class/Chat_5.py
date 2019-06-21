import os, random
import easygui
from datetime import datetime
import webbrowser as wb

name = input("Enter your name : ")
print("Welcome",name)
helloIntent = ["hi","hello","hey","hi there","hey there","hello there","howdy",
               "hola"]
musicIntent = ["play song","play music","start song","start a song","play a song"]

timeIntent = ["time please","tell me time","what's the time","time"]
dateIntent = ["date please","tell me date","what's the date today","date"]

while True:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello",name)
    elif msg in musicIntent:
        path = easygui.fileopenbox()
        os.startfile(path)
    elif msg in timeIntent:
        t = datetime.now().time()
        print("Current time is",t.strftime('%H:%M:%S,%p'))
    elif msg in dateIntent:
        d = datetime.now().date()
        print("Current date is",d.strftime('%d/%m/%y,%a'))
    elif msg.startswith('open'):
        web = msg.split()[-1]
        wb.open(web+'.com')
    elif msg == "bye":
        print("Bye...See you",name)
        break
    else:
        print("I don't understand")
