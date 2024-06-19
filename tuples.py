Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ''
>>> type(a)
<class 'str'>
>>> a = str()
>>> type(a)
<class 'str'>
>>> a = []
>>> type(a)
<class 'list'>
>>> a = list()
>>> a = []
>>> a = list()
>>> type(a)
<class 'list'>
>>> a = ()
>>> type(a)
<class 'tuple'>
>>> a = tuple()
>>> type(a)
<class 'tuple'>
>>> 
>>> a = (34,56.78,78,12,True,12,"Python")
>>> a
(34, 56.78, 78, 12, True, 12, 'Python')
>>> len(a)
7
>>> 34 in a
True
>>> (1,2,34) + (5,8,1)
(1, 2, 34, 5, 8, 1)
>>> (1, 2, 34, 5, 8, 1)*3
(1, 2, 34, 5, 8, 1, 1, 2, 34, 5, 8, 1, 1, 2, 34, 5, 8, 1)
>>> a
(34, 56.78, 78, 12, True, 12, 'Python')
>>> a[-3]
True
>>> a[0]=44
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[0]=44
TypeError: 'tuple' object does not support item assignment
>>> s = "Naveen"
>>> s[0]='Pr'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s[0]='Pr'
TypeError: 'str' object does not support item assignment
>>> a = 3,4,6,7
>>> a
(3, 4, 6, 7)
>>> a = (3)
>>> type(a)
<class 'int'>
>>> a
3
>>> a = (3,4)
>>> a
(3, 4)
>>> a = (3)
>>> a
3
>>> a = (3,)
>>> a
(3,)
>>> type(a)
<class 'tuple'>
>>> (25000.00,)*4
(25000.0, 25000.0, 25000.0, 25000.0)
>>> (25000.00)*4
100000.0
>>> a
(3,)
>>> a = (34,56.78,78,12,True,12,"Python")
>>> a.index(56.78)
1
>>> a.index(56.78)
1
>>> a.index(12)
3
>>> a.index(22)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.index(22)
ValueError: tuple.index(x): x not in tuple
>>> a.count(12)
2
>>> a.count(122)
0
>>> 