Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(30):
	t.forward(5 * i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(40):
	t.forward(5 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(30):
	t.circle(5 * i)
	t.left(45)

	

>>> t.reset()
>>> t.speed(0)
>>> for i in range(30):
	t.circle(5 * i)
	t.left(45)

	
>>> t.reset()
>>> t.speed(2)
>>> for i in range(30):
	t.circle(5 * i)
	t.left(45)

	
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    t.circle(5 * i)
  File "C:\Python38\lib\turtle.py", line 1992, in circle
    self._go(l)
  File "C:\Python38\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python38\lib\turtle.py", line 3196, in _goto
    self._update() #count=True)
  File "C:\Python38\lib\turtle.py", line 2663, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python38\lib\turtle.py", line 563, in _update
    self.cv.update()
  File "C:\Python38\lib\tkinter\__init__.py", line 1314, in update
    self.tk.call('update')
KeyboardInterrupt
>>> t.reset()
>>> t.right(75)
>>> t.forward(100)
>>> for i in range(4):
	t.right(144)
	t.forward(100)

	
>>> t.reset()
>>> t.right(90)
>>> t.forward(100)
>>> for i in range(4):
	t.right(144)
	t.forward(100)

	
>>> t.reset()
>>> colors = ['red','green','purple','orange']
>>> t.speed(0)
>>> for i in range(30):
	t.pencolor(colors[i % 4])
	t.circle(5 * i)
	t.left(75)

	
>>> t.reset()
>>> t.speed(0)
>>> for i in range(360):
	t.pencolor(colors[i % 4])
	t.width(i/100 + 1)
	t.circle(i)
	t.left(60)

	
>>> t.reset()
>>> t.speed(0)
>>> for i in range(360):
	t.pencolor(colors[i % 4])
	t.width(i/100 + 1)
	t.circle(i)
	t.left(59)

	
>>> t.reset()
>>> for i in range(30):
	t.pencolor(colors[i % 4])
	t.width(i/100 + 1)
	t.circle(5 * i)
	t.left(59)

	
>>> t.reset()
>>> t.speed(0)
>>> for i in range(30):
	t.pencolor(colors[i % 4])
	t.circle(5 * i)
	t.circle(-5 * i)
	t.left(i)

	
>>> t.reset()
>>> 