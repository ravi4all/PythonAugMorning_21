Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	return "Hello"

>>> sayHello()
'Hello'
>>> x = sayHello()
>>> type(x)
<class 'str'>
>>> def greet():
	def sayHello():
		return "Hello"
	def sayBye():
		return "Bye"
	return sayHello, sayBye

>>> greet()
(<function greet.<locals>.sayHello at 0x00000294959119D0>, <function greet.<locals>.sayBye at 0x0000029495911A60>)
>>> m1, m2 = greet()
>>> m1
<function greet.<locals>.sayHello at 0x0000029495911AF0>
>>> m2
<function greet.<locals>.sayBye at 0x0000029495911B80>
>>> m1()
'Hello'
>>> m2()
'Bye'
>>> 