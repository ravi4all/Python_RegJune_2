import os, random

name = input("Enter your name : ")
print("Welcome",name)
helloIntent = ["hi","hello","hey","hi there","hey there","hello there","howdy",
               "hola"]
musicIntent = ["play song","play music","start song","start a song","play a song"]
while True:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello",name)
    elif msg in musicIntent:
        path = 'C:\\Users\\asus\\Music'
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye...See you",name)
        break
    else:
        print("I don't understand")
