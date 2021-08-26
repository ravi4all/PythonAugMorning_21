Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text = "Hello world, this is Python Programming"
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.swapcase()
'hELLO WORLD, THIS IS pYTHON pROGRAMMING'
>>> "hello" == "Hello"
False
>>> "hello".casefold() == "Hello".casefold()
True
>>> text.count('o')
4
>>> text.count('p')
0
>>> text.count('i')
3
>>> text.count('o',6)
3
>>> text.count('o',16)
2
>>> text.count('o',6, 16)
1
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text
'Hello world, this is Python Programming'
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rindex('o')
30
>>> text.rfind('o')
30
>>> text.isalpha()
False
>>> text.isalnum()
False
>>> text.islower()
False
>>> text.isupper()
False
>>> text = "      hello......"
>>> text.strip()
'hello......'
>>> text.strip('.')
'      hello'
>>> text = text.lstrip()
>>> text
'hello......'
>>> text = text.rstrip()
>>> text
'hello......'
>>> text = text.rstrip('.')
>>> text
'hello'
>>> text = "Hello world, this is Python Programming"
>>> text.split()
['Hello', 'world,', 'this', 'is', 'Python', 'Programming']
>>> text.split()
['Hello', 'world,', 'this', 'is', 'Python', 'Programming']
>>> text.split(',')
['Hello world', ' this is Python Programming']
>>> text = "Hello world, this, is Python Programming, let's code"
>>> text.split(',')
['Hello world', ' this', ' is Python Programming', " let's code"]
>>> text.partition()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    text.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> text.partition(',')
('Hello world', ',', " this, is Python Programming, let's code")
>>> text.partition('is')
('Hello world, th', 'is', ", is Python Programming, let's code")
>>> text.partition('is ')
('Hello world, this, ', 'is ', "Python Programming, let's code")
>>> text.rsplit()
['Hello', 'world,', 'this,', 'is', 'Python', 'Programming,', "let's", 'code']
>>> text.rsplit(',')
['Hello world', ' this', ' is Python Programming', " let's code"]
>>> text
"Hello world, this, is Python Programming, let's code"
>>> text.split()
['Hello', 'world,', 'this,', 'is', 'Python', 'Programming,', "let's", 'code']
>>> text.split(",")
['Hello world', ' this', ' is Python Programming', " let's code"]
>>> data = ["hell","world","this","is","python"]
>>> data = ["hello","world","this","is","python"]
>>> ' '.join(data)
'hello world this is python'
>>> '-'.join(data)
'hello-world-this-is-python'
>>> ','.join(data)
'hello,world,this,is,python'
>>> text
"Hello world, this, is Python Programming, let's code"
>>> text.replace("code","not code")
"Hello world, this, is Python Programming, let's not code"
>>> text
"Hello world, this, is Python Programming, let's code"
>>> text.replace('i','x')
"Hello world, thxs, xs Python Programmxng, let's code"
>>> text.startswith('How')
False
>>> text.startswith('H')
True
>>> text.endswith('?')
False
>>> text.endswith('.')
False
>>> text.endswith('e')
True
>>> text.startswith('w',3)
False
>>> text.startswith('w',4)
False
>>> text.startswith('w',5)
False
>>> text.startswith('w',6)
True
>>> len(text)
52
>>> text.center(45)
"Hello world, this, is Python Programming, let's code"
>>> text.center(53)
" Hello world, this, is Python Programming, let's code"
>>> text.center(54)
" Hello world, this, is Python Programming, let's code "
>>> text.center(64)
"      Hello world, this, is Python Programming, let's code      "
>>> text.center(64, '*')
"******Hello world, this, is Python Programming, let's code******"
>>> text.zfill(10)
"Hello world, this, is Python Programming, let's code"
>>> text.zfill(53)
"0Hello world, this, is Python Programming, let's code"
>>> text.zfill(60)
"00000000Hello world, this, is Python Programming, let's code"
>>> 