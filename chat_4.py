#Chat Application using If Else

from datetime import datetime as dt
import os, random, glob

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there","hola"]
dateIntent = ["date","tell me date","what's the date","today's date"]
timeIntent = ["time","tell me time","what's the time","current time"]
musicIntent = ["play music", "play song","song"]

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
    elif msg in musicIntent:
        os.chdir("F:\\Batches\Songs")
        mp3 = glob.glob("*.mp3")
        random_song = random.choice(mp3)
        os.startfile(random_song)
    elif msg == "show songs":
        pass
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
