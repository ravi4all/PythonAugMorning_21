Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = ["John","Mac","Sam","Tom","Harry"]
>>> dept = ["IT","HR","IT","IT","Sales"]
>>> sal = [45000,43000,27000,35000,58000]
>>> data = [names, sal,dept]
>>> data
[['John', 'Mac', 'Sam', 'Tom', 'Harry'], [45000, 43000, 27000, 35000, 58000], ['IT', 'HR', 'IT', 'IT', 'Sales']]
>>> for i in range(len(data[0])):
	print(data[0][i], data[1][i], data[2][i])

	
John 45000 IT
Mac 43000 HR
Sam 27000 IT
Tom 35000 IT
Harry 58000 Sales
>>> x = [3,5,7,8,3,12]
>>> y = x
>>> x
[3, 5, 7, 8, 3, 12]
>>> y
[3, 5, 7, 8, 3, 12]
>>> x[0] = 100
>>> x
[100, 5, 7, 8, 3, 12]
>>> y
[100, 5, 7, 8, 3, 12]
>>> z = x[:]
>>> z
[100, 5, 7, 8, 3, 12]
>>> y
[100, 5, 7, 8, 3, 12]
>>> z
[100, 5, 7, 8, 3, 12]
>>> x
[100, 5, 7, 8, 3, 12]
>>> x[0] = 10
>>> x
[10, 5, 7, 8, 3, 12]
>>> y
[10, 5, 7, 8, 3, 12]
>>> z
[100, 5, 7, 8, 3, 12]
>>> x is y
True
>>> x is z
False
>>> x == y
True
>>> x is y
True
>>> z = x[:]
>>> x == z
True
>>> x
[10, 5, 7, 8, 3, 12]
>>> z
[10, 5, 7, 8, 3, 12]
>>> x is z
False
>>> x = [4,5,7,4,12,[56,23,7,9]]
>>> y = x
>>> z = x[:]
>>> x[0] = 100
>>> y
[100, 5, 7, 4, 12, [56, 23, 7, 9]]
>>> x
[100, 5, 7, 4, 12, [56, 23, 7, 9]]
>>> z
[4, 5, 7, 4, 12, [56, 23, 7, 9]]
>>> x[-1]
[56, 23, 7, 9]
>>> x[-1][0]
56
>>> x[-1][0] = 150
>>> x
[100, 5, 7, 4, 12, [150, 23, 7, 9]]
>>> y
[100, 5, 7, 4, 12, [150, 23, 7, 9]]
>>> z
[4, 5, 7, 4, 12, [150, 23, 7, 9]]
>>> # shallow copy and deep copy
>>> import copy
>>> z = copy.deepcopy(x)
>>> x
[100, 5, 7, 4, 12, [150, 23, 7, 9]]
>>> z
[100, 5, 7, 4, 12, [150, 23, 7, 9]]
>>> x[-1][0] = 100
>>> x
[100, 5, 7, 4, 12, [100, 23, 7, 9]]
>>> z
[100, 5, 7, 4, 12, [150, 23, 7, 9]]
>>> # list comprehension
>>> 