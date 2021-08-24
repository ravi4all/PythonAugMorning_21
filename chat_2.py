#Chat Application using If Else

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg == "hi" or msg == "hey" or msg == "hello" or msg == "hi there":
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
