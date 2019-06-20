name = input("Enter your name : ")
print("Welcome",name)

helloIntent = ["hi","hello","hey","hi there","hey there","hello there","howdy",
               "hola"]

# Membership Operator - in, not in
# Identity Operator - is, not is

while True:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello",name)
    elif msg == "bye":
        print("Bye...See you",name)
        break
    else:
        print("I don't understand")
