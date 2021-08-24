#Chat Application using If Else

from datetime import datetime as dt

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there","hola"]
dateIntent = ["date","tell me date","what's the date","today's date"]
timeIntent = ["time","tell me time","what's the time","current time"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = dt.now().date()
        print(d.strftime("%d/%m/%y,%a"))
    elif msg in timeIntent:
        t = dt.now().time()
        print(t.strftime("%H:%M:%S,%p"))
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
