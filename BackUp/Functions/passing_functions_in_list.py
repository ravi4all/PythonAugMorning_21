Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	print("Hello User")

	
>>> def sayBye():
	print("Bye User")

	
>>> sayHello()
Hello User
>>> sayBye()
Bye User
>>> greet = [sayHello(), sayBye()]
Hello User
Bye User
>>> greet
[None, None]
>>> h = sayBye()
Bye User
>>> h
>>> greet = [sayHello, sayBye]
>>> greet
[<function sayHello at 0x00000176D3B09040>, <function sayBye at 0x00000176D3B6DE50>]
>>> sayHello()
Hello User
>>> sayHello
<function sayHello at 0x00000176D3B09040>
>>> greet[0]
<function sayHello at 0x00000176D3B09040>
>>> greet[1]
<function sayBye at 0x00000176D3B6DE50>
>>> greet[0]()
Hello User
>>> greet[1]()
Bye User
>>> 