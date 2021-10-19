Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> counter()
1
>>> x = 0
>>> def counter():
	while True:
		x += 1
		return x

	
>>> counter()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    counter()
  File "<pyshell#11>", line 3, in counter
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> def greet():
	print("Hello")
	return "Bye"
	print("Say Bye Again")

	
>>> greet()
Hello
'Bye'
>>> def greet():
	print("Hello")
	yield "Bye"
	print("Say Bye Again")

	
>>> greet()
<generator object greet at 0x000001AA2D963890>
>>> obj = greet()
>>> next(obj)
Hello
'Bye'
>>> next(obj)
Say Bye Again
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    next(obj)
StopIteration
>>> obj = greet()
>>> for i in obj:
	print(i)

	
Hello
Bye
Say Bye Again
>>> obj
<generator object greet at 0x000001AA2D963890>
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter()
<generator object counter at 0x000001AA2DA49900>
>>> views = counter()
>>> next(views)
1
>>> next(views)
2
>>> next(views)
3
>>> next(views)
4
>>> for i in range(5):
	print(next(views))

	
5
6
7
8
9
>>> 