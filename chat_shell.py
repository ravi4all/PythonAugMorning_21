Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: F:/Batches/AugPython/palindrome_num.py ==============
Enter a number : 123
Number is not palindrome...
>>> 
=============== RESTART: F:/Batches/AugPython/palindrome_num.py ==============
Enter a number : 1221
Number is palindrome...
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : hi
Hello User
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : hello
I don't understand
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : Hi
I don't understand
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : HI
Hello User
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : Hi
Hello User
>>> msg
'hi'
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : hi
Hello User
>>> 
=================== RESTART: F:/Batches/AugPython/chat_1.py ==================
Enter your message : hi
Hello User
Enter your message : hello
I don't understand
Enter your message : hey
I don't understand
Enter your message : bye
Bye User
>>> 
=================== RESTART: F:/Batches/AugPython/chat_2.py ==================
Enter your message : hi
Hello User
Enter your message : hello
I don't understand
Enter your message : hey
I don't understand
Enter your message : bye
Bye User
>>> 
=================== RESTART: F:/Batches/AugPython/chat_2.py ==================
Enter your message : hi
Hello User
Enter your message : hello
Hello User
Enter your message : hey
Hello User
Enter your message : bye
Bye User
>>> 
=================== RESTART: F:/Batches/AugPython/chat_3.py ==================
Enter your message : hi
Hello User
Enter your message : hey
Hello User
Enter your message : hello
Hello User
Enter your message : bye
Bye User
>>> import datetime
>>> datetime.date
<class 'datetime.date'>
>>> datetime.date.day
<attribute 'day' of 'datetime.date' objects>
>>> datetime.datetime.now()
datetime.datetime(2021, 8, 24, 9, 58, 27, 669876)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 8, 24, 9, 59, 5, 511944)
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2021, 8, 24, 9, 59, 16, 758028)
>>> dt.now().date
<built-in method date of datetime.datetime object at 0x000001F24768A270>
>>> print(dt.now().date())
2021-08-24
>>> print(dt.now().time())
09:59:35.849120
>>> d = dt.now().date()
>>> t = dt.now().time()
>>> d.strftime("%d/%m/%y")
'24/08/21'
>>> d.strftime("%d/%m/%y,%p")
'24/08/21,AM'
>>> d.strftime("%d/%m/%y,%a")
'24/08/21,Tue'
>>> t.strftime("%H:%M:%S,%p")
'09:59:52,AM'
>>> 
= RESTART: F:/Batches/AugPython/chat_3.py
Enter your message : hi
Hello User
Enter your message : hello
Hello User
Enter your message : hey
Hello User
Enter your message : date
24/08/21,Tue
Enter your message : time
10:12:56,AM
Enter your message : tell me date
24/08/21,Tue
Enter your message : tell me time
10:13:01,AM
Enter your message : bye
Bye User
>>> import os
>>> os.listdir()
['01-code.py', '02-code.py', '03-code.py', 'armstrong_num.py', 'BackUp', 'chat_1.py', 'chat_2.py', 'chat_3.py', 'chat_4.py', 'guess_the_num.py', 'hollow_patterns.py', 'if_else_2.py', 'if_else_introduction.py', 'if_else_patterns.py', 'loop_1.py', 'loop_introduction.py', 'nested_loop.py', 'palindrome_num.py', 'patterns.py', 'rock_paper_scissor.py', 'turtle_code.py', 'while_intro.py']
>>> os.chdir("F:\\Batches\Songs")
>>> os.getcwd()
'F:\\Batches\\Songs'
>>> os.listdir()
['bang-bang.mp3', 'exception_hierarchy.png', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'file_handling_1.png', 'file_handling_2.png', 'song.mp3', 'songCopy.mp3']
>>> import random
>>> songs = os.listdir()
>>> random.choice(songs)
'fifa world cup.mp3'
>>> os.startfile(random.choice(songs))
>>> os.startfile(random.choice(songs))
>>> os.startfile(random.choice(songs))
>>> os.startfile(random.choice(songs))
>>> os.startfile(random.choice(songs))
>>> os.startfile(random.choice(songs))
>>> import glob
>>> mp3 = glob.glob("*.mp3")
>>> os.startfile(random.choice(mp3))
>>> 
= RESTART: F:/Batches/AugPython/chat_4.py
Enter your message : hi
Hello User
Enter your message : hello
Hello User
Enter your message : date
24/08/21,Tue
Enter your message : play music
Enter your message : bye
Bye User
>>> x = [2,4,6,8,2,12]
>>> for i in range(len(x)):
	print(x[i])

	
2
4
6
8
2
12
>>> for i in range(len(x)):
	print(i+1,":",x[i])

	
1 : 2
2 : 4
3 : 6
4 : 8
5 : 2
6 : 12
>>> 