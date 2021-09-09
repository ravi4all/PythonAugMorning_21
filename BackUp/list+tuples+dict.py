Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [4,5,3,[41,34,66]]
>>> y = x[:]
>>> y = x.copy()
>>> x is y
False
>>> x[0] = 12
>>> x
[12, 5, 3, [41, 34, 66]]
>>> y
[4, 5, 3, [41, 34, 66]]
>>> x[-1][0] = 100
>>> x
[12, 5, 3, [100, 34, 66]]
>>> y
[4, 5, 3, [100, 34, 66]]
>>> import copy
>>> y = copy.deepcopy(x)
>>> x = []
>>> for i in range(10):
	x.append(i)

	
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in range(10):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8]
>>> x = []
>>> for i in range(10):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[0, 2, 4, 6, 8]
>>> x = [i for i in range(10)]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = [i for i in range(10) if i % 2 == 0]
>>> x
[0, 2, 4, 6, 8]
>>> x = [(i,j) for i in range(5) for j in range(5)]
>>> x
[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
>>> x = [(i,j) for i in range(5) for j in range(5) if i == j]
>>> x
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
>>> x = ()
>>> x = tuple()
>>> x = 10,21
>>> x = 12,
>>> x = (10,3,35,12)
>>> x
(10, 3, 35, 12)
>>> x[0]
10
>>> x[0:3]
(10, 3, 35)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name, age, salary = "Ram", 23, 56000
>>> data
('Ram', 23, 56000)
>>> name
'Ram'
>>> age
23
s
>>> a
>>> salary
56000
>>> data = {"name" : "Ram", "age" : 50, "salary" : 45000}
>>> data
{'name': 'Ram', 'age': 50, 'salary': 45000}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["name"]
'Ram'
>>> data["age"]
50
>>> data["salary"]
45000
>>> data["dept"] = "IT"
>>> data
{'name': 'Ram', 'age': 50, 'salary': 45000, 'dept': 'IT'}
>>> del data["age"]
>>> data
{'name': 'Ram', 'salary': 45000, 'dept': 'IT'}
>>> info = {"address" : "Delhi", "ph" : 67676767}
>>> data + info
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    data + info
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> data.update(info)
>>> data
{'name': 'Ram', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi', 'ph': 67676767}
>>> data.keys()
dict_keys(['name', 'salary', 'dept', 'address', 'ph'])
>>> data.values()
dict_values(['Ram', 45000, 'IT', 'Delhi', 67676767])
>>> data.items()
dict_items([('name', 'Ram'), ('salary', 45000), ('dept', 'IT'), ('address', 'Delhi'), ('ph', 67676767)])
>>> data.get("name")
'Ram'
>>> data["name"]
'Ram'
>>> data["email"]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    data["email"]
KeyError: 'email'
>>> data.get("email")
>>> data.get("email", "Not Available")
'Not Available'
>>> data.get("name", "Not Available")
'Ram'
>>> data.pop("age")
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    data.pop("age")
KeyError: 'age'
>>> data.pop("ph")
67676767
>>> data
{'name': 'Ram', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> data.popitem()
('address', 'Delhi')
>>> data.popitem()
('dept', 'IT')
>>> data
{'name': 'Ram', 'salary': 45000}
>>> data = [{"name":"John","sal":45000}, {"name":"Mac","sal":56000}]
>>> data[0]
{'name': 'John', 'sal': 45000}
>>> data[1]
{'name': 'Mac', 'sal': 56000}
>>> data = {"names":["John","Mac"], "sal" : [45000, 56000]}
>>> data
{'names': ['John', 'Mac'], 'sal': [45000, 56000]}
>>> data["names"]
['John', 'Mac']
>>> data["sal"]
[45000, 56000]
>>> data["names"][0]
'John'
>>> data["sal"][0]
45000
>>> data = {1 : 10, 2 : 40}
>>> data
{1: 10, 2: 40}
>>> data[1]
10
>>> data[2]
40
>>> data = {i : i ** 2 for i in range(10)}
>>> data
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> data = {"name" : "Ram", "age" : 50, "salary" : 45000}
>>> for item in data:
	print(item)

	
name
age
salary
>>> for item in data:
	print(data[item])

	
Ram
50
45000
>>> for item in data:
	print(item, ":", data[item])

	
name : Ram
age : 50
salary : 45000
>>> for item in data.values():
	print(item)

	
Ram
50
45000
>>> 