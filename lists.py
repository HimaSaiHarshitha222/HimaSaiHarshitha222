Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> a = a+3
>>> a
13
>>> b
10
>>> a = [1,2,3,4,5]
>>> b = a
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> a.append(88)
>>> a
[1, 2, 3, 4, 5, 88]
>>> b
[1, 2, 3, 4, 5, 88]
>>> b[1] = 222
>>> b
[1, 222, 3, 4, 5, 88]
>>> a
[1, 222, 3, 4, 5, 88]
>>> a=[1, 2, 3, 4, 5]
>>> b = a[:]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> a[0]=11
>>> a
[11, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> a = [1, 2, 3, 4, 5]
>>> b = a.copy()
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> a[0]=100
>>> a
[100, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> b[1]=99
>>> b
[1, 99, 3, 4, 5]
>>> a
[100, 2, 3, 4, 5]
>>> #length
>>> a = [1, 2, 3, 4, 5]
>>> len(a)
5
>>> #concatenation
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> #Repetition
>>> [1, 2, 3, 4, 5, 6]*4
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> a = [1, 2, 3, 4, 5, 6]
>>> 44 in a
False
>>> 33 not in a
True
>>> a = []
>>> a.append(5)
>>> a
[5]
>>> a.append(78)
>>> a
[5, 78]
>>> a.append(99.12)
>>> a
[5, 78, 99.12]
>>> a.append(7,8)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.append(7,8)
TypeError: append() takes exactly one argument (2 given)
>>> a.extend([8,9,11])
>>> a
[5, 78, 99.12, 8, 9, 11]
>>> a.insert(3,"Python")
>>> a
[5, 78, 99.12, 'Python', 8, 9, 11]
>>> a.append(78)
>>> a
[5, 78, 99.12, 'Python', 8, 9, 11, 78]
>>> a.index(8)
4
>>> a.index(78)
1
>>> a.index(786)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.index(786)
ValueError: 786 is not in list
>>> a
[5, 78, 99.12, 'Python', 8, 9, 11, 78]
>>> a.count(99.12)
1
>>> a.count(78)
2
>>> a.count(786)
0
>>> a
[5, 78, 99.12, 'Python', 8, 9, 11, 78]
>>> a.remove('Python')
>>> a.remove(78)
>>> a
[5, 99.12, 8, 9, 11, 78]
>>> a.remove(88)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove(88)
ValueError: list.remove(x): x not in list
>>> a
[5, 99.12, 8, 9, 11, 78]
>>> a.pop(2)
8
>>> a
[5, 99.12, 9, 11, 78]
>>> print(a.remove(99.12))
None
>>> a
[5, 9, 11, 78]
>>> print(a.pop(1))
9
>>> a.appen(58)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.appen(58)
AttributeError: 'list' object has no attribute 'appen'
>>> a.append(58)
>>> a.extend([5,56,78])
>>> a
[5, 11, 78, 58, 5, 56, 78]
>>> a.pop()
78
>>> a
[5, 11, 78, 58, 5, 56]
>>> a.pop()
56
>>> a.pop()
5
>>> a
[5, 11, 78, 58]
>>> a.reverse()
>>> a
[58, 78, 11, 5]
>>> a.sort()
>>> a
[5, 11, 58, 78]
>>> a.sort(reverse = True)
>>> a
[78, 58, 11, 5]
>>> a
[78, 58, 11, 5]
>>> b= a.copy()
>>> a
[78, 58, 11, 5]
>>> b
[78, 58, 11, 5]
>>> b.clear()
>>> b
[]
>>> 