Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = (10,20,30,40,50,60,70)
>>> pos = 3
>>> left = a[:pos-1]
>>> left
(10, 20)
>>> right = a[pos-1:]
>>> right
(30, 40, 50, 60, 70)
>>> left + (34,) + right
(10, 20, 34, 30, 40, 50, 60, 70)
>>> a = (10,20,30,40,50,60,70)
>>> pos=3
>>> a[:pos-1]
(10, 20)
>>> a[pos-1:]
(30, 40, 50, 60, 70)
>>> a[pos:]
(40, 50, 60, 70)
>>> a
(10, 20, 30, 40, 50, 60, 70)
>>> pos = 3
>>> a[:pos-1]
(10, 20)
>>> a[pos:]
(40, 50, 60, 70)
>>> #Dictionary
>>> a = {}
>>> type(a)
<class 'dict'>
>>> a = dict()
>>> marks = {'Telugu':78, 'Hindi':76, 'English':65}
>>> marks['Hindi']
76
>>> marks = {'Telugu':78, 'Hindi':76, 'English':65,'Hindi':64}
>>> len(marks)
3
>>> marks
{'Telugu': 78, 'Hindi': 64, 'English': 65}
>>> 'Telugu' in marks
True
>>> emp = {'Nag':10, 'Vishnu':20, 'Nag':30}

>>> emp
{'Nag': 30, 'Vishnu': 20}
>>> emp = {['Nag']:10, 'Vishnu':20, 'Raj':30} 

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    emp = {['Nag']:10, 'Vishnu':20, 'Raj':30}
TypeError: unhashable type: 'list'
>>> d = {1001:'Aadhya', 1002:'Balaram', 1003:'Cummins', 1004:'Dhoni'}
>>> d.keys()
dict_keys([1001, 1002, 1003, 1004])
>>> d.values()
dict_values(['Aadhya', 'Balaram', 'Cummins', 'Dhoni'])
>>> d.items()
dict_items([(1001, 'Aadhya'), (1002, 'Balaram'), (1003, 'Cummins'), (1004, 'Dhoni')])
>>> d[1005] = 'Eeswar'
>>> d
{1001: 'Aadhya', 1002: 'Balaram', 1003: 'Cummins', 1004: 'Dhoni', 1005: 'Eeswar'}
>>> d.update({1006:'Farooq', 1007:'Gambir', 1008:'Harsha'})
>>> d
{1001: 'Aadhya', 1002: 'Balaram', 1003: 'Cummins', 1004: 'Dhoni', 1005: 'Eeswar', 1006: 'Farooq', 1007: 'Gambir', 1008: 'Harsha'}
>>> d.get(1004)
'Dhoni'
>>> d.get(1088)
>>> d.get(1088,"Key Not Found")
'Key Not Found'
>>> d.pop(1005)
'Eeswar'
>>> d
{1001: 'Aadhya', 1002: 'Balaram', 1003: 'Cummins', 1004: 'Dhoni', 1006: 'Farooq', 1007: 'Gambir', 1008: 'Harsha'}
>>> abcd = d.copy()
>>> abcd
{1001: 'Aadhya', 1002: 'Balaram', 1003: 'Cummins', 1004: 'Dhoni', 1006: 'Farooq', 1007: 'Gambir', 1008: 'Harsha'}
>>> abcd.clear()
>>> abcd
{}
>>> 