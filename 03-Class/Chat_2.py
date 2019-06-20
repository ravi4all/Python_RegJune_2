name = input("Enter your name : ")
print("Welcome",name)

# Comparison Operator - ==, >,<, >=, <=, !=
# Logical Operator/Keyword - and, or, not

while True:
    msg = input("Enter your message : ")
    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hi there":
        print("Hello",name)
    elif msg == "bye":
        print("Bye...See you",name)
        break
    else:
        print("I don't understand")
