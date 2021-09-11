Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: F:\Batches\AugPython\BackUp_2\dict_exercise.py ==========
Total Marks : 304
Average Marks : 76.0
>>> data = {3,4,6,7,8,4,5,7,8,23,6,8,9,4,12,4,6,8,9,0,5}
>>> data
{0, 3, 4, 5, 6, 7, 8, 9, 12, 23}
>>> x1 = {3,4,6,6,3,}
>>> x2 = {1,4,6,89,0,5,3,4,7}
>>> x1 & x2
{3, 4, 6}
>>> x1 | x2
{0, 1, 3, 4, 5, 6, 7, 89}
>>> x1 - x2
set()
>>> x2 - x1
{0, 1, 5, 7, 89}
>>> x1.intersection(x2)
{3, 4, 6}
>>> x1.union(x2)
{0, 1, 3, 4, 5, 6, 7, 89}
>>> x1.difference(x2)
set()
>>> 
========= RESTART: F:/Batches/AugPython/BackUp_2/movie_rec_system.py =========
{'action': 0.3076923076923077, 'comedy': 0.18181818181818182, 'sci-fi': 0.1111111111111111, 'thriller': 0.2727272727272727, 'horror': 0.1111111111111111}
>>> 
========= RESTART: F:/Batches/AugPython/BackUp_2/movie_rec_system.py =========
{'action': 0.31, 'comedy': 0.18, 'sci-fi': 0.11, 'thriller': 0.27, 'horror': 0.11}
>>> 