Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def temp_conv(c):
	return 9/5 * c + 32

>>> temp_conv(34.44)
93.99199999999999
>>> temp = [33.4,32.67,29.7,36.5,33.1]
>>> temp_conv(temp)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    temp_conv(temp)
  File "<pyshell#2>", line 2, in temp_conv
    return 9/5 * c + 32
TypeError: can't multiply sequence by non-int of type 'float'
>>> for t in temp:
	print(temp_conv(t))

	
92.12
90.80600000000001
85.46000000000001
97.7
91.58000000000001
>>> f = []
>>> for t in temp:
	f.append(temp_conv(t))

	
>>> f
[92.12, 90.80600000000001, 85.46000000000001, 97.7, 91.58000000000001]
>>> def m_to_km(m):
	return m/1000

>>> def km_to_m(km):
	return km * 1000

>>> kms = [4.5,50,43,12]
>>> def myMap(func, iter):
	data = []
	for i in range(len(iter)):
		data.append(func(iter[i]))
	return data

>>> myMap(temp_conv, temp)
[92.12, 90.80600000000001, 85.46000000000001, 97.7, 91.58000000000001]
>>> myMap(km_to_m, kms)
[4500.0, 50000, 43000, 12000]
>>> map(temp_conv, temp)
<map object at 0x000001A166D2DDF0>
>>> list(map(temp_conv, temp))
[92.12, 90.80600000000001, 85.46000000000001, 97.7, 91.58000000000001]
>>> list(map(km_to_m, kms))
[4500.0, 50000, 43000, 12000]
>>> lambda x,y : x + y
<function <lambda> at 0x000001A168E71940>
>>> def add(x,y):
	return x + y

>>> add(3,4)
7
>>> lambda x,y : x + y
<function <lambda> at 0x000001A168E71940>
>>> (lambda x,y : x + y)(4,5)
9
>>> list(map(lambda km : km / 1000, kms))
[0.0045, 0.05, 0.043, 0.012]
>>> list(map(lambda km : km * 1000, kms))
[4500.0, 50000, 43000, 12000]
>>> list(map(lambda c : 9/5 * c + 32, temp))
[92.12, 90.80600000000001, 85.46000000000001, 97.7, 91.58000000000001]
>>> list(map(lambda km : km / 1000, [324,546,25,6,6]))
[0.324, 0.546, 0.025, 0.006, 0.006]
>>> 