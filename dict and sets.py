Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> colors = {10: "Red", 35: "Green", 15: "Blue", 25: "White"}

>>> sorted(colors.items())
[(10, 'Red'), (15, 'Blue'), (25, 'White'), (35, 'Green')]
>>> sorted(colors.items(),key = lambda x: x[1])
[(15, 'Blue'), (35, 'Green'), (10, 'Red'), (25, 'White')]
>>> sorted(colors.items(),key = lambda x: x[1],reverse = True)
[(25, 'White'), (10, 'Red'), (35, 'Green'), (15, 'Blue')]
>>> s = ['Gujarat', 'Uttarakand', 'Madhya Pradesh', 'Telangana', 'Goa', 'Andhra Pradesh']
>>> c = ['Ahmedabad', 'Dehradun', 'Bhopal', 'Hyderabad', 'Panaji', 'Anantapur']
>>> dict(zip(s,c))
{'Gujarat': 'Ahmedabad', 'Uttarakand': 'Dehradun', 'Madhya Pradesh': 'Bhopal', 'Telangana': 'Hyderabad', 'Goa': 'Panaji', 'Andhra Pradesh': 'Anantapur'}
>>> str = "Sujay=23, Rajesh=20, Lahari=19,Nithin=22"

>>> str.split(',')
['Sujay=23', ' Rajesh=20', ' Lahari=19', 'Nithin=22']
>>> for ele in ['Sujay=23', ' Rajesh=20', ' Lahari=19', 'Nithin=22']:
	print(ele.split('='))

	
['Sujay', '23']
[' Rajesh', '20']
[' Lahari', '19']
['Nithin', '22']
>>> #sets
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s = set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> s = {34,1, 56.7,8-9j,"Python", 23, 34, 0, 3, True, 77, "python", False, 12}
>>> s
{0, 1, 34, 3, 12, (8-9j), 77, 'python', 23, 56.7, 'Python'}
>>> s = {34,1, 56.7,8-9j,"Python", 23, 34, 0, 3, True, 77, "python", False, 12}
>>> 
>>> 
>>> 
>>> 
>>> s = {34, 56.7,8-9j,"Python", 23, 34, 0, 3, True, 77, "python", 1, False, 12}
>>> s
{0, True, 34, 3, 12, (8-9j), 77, 'python', 23, 56.7, 'Python'}
>>> len(s)
11
>>> 34 in s
True
>>> 7 in s
False
>>> frozenset(s)
frozenset({0, True, 34, 3, 12, (8-9j), 77, 'python', 23, 56.7, 'Python'})
>>> A = {1,2,3,4}
>>> B = {3,1}
>>> B.issubset(A)
True
>>> B<=A
True
>>> A.issuperset(B)
True
>>> A>=B
True
>>> A = {3, 6, 1}
>>> B = {2, 8, 3, 1}
>>> A.isdisjoint(B)
False
>>> A = {3, 1, 4}
>>> B = {8, 9, 0}
>>> A.isdisjoint(B)
True
>>> a = {3, 1, 7, 4} 

>>> b = {2, 8, 3, 1} 

>>> a.union(b)
{1, 2, 3, 4, 7, 8}
>>> a|b
{1, 2, 3, 4, 7, 8}
>>> x = {"apple", "banana", "cherry"}

>>> y = {"google", "microsoft", "apple"}

>>> x.union(y)
{'apple', 'microsoft', 'google', 'banana', 'cherry'}
>>> x|y
{'apple', 'microsoft', 'google', 'banana', 'cherry'}
>>> a = {3, 1, 7, 4}

>>> b = {2, 8, 3, 1}

>>> c = {1, 0, 4, 6}

>>> d = {8, 2, 6, 3} 

>>> a|b|c|d
{0, 1, 2, 3, 4, 6, 7, 8}
>>> a.union(b,c,d)
{0, 1, 2, 3, 4, 6, 7, 8}
>>> a = {3, 6, 1} 

>>> b = {2, 8, 3, 1}

>>> a&b
{1, 3}
>>> a.intersection(b)
{1, 3}
>>> a = {3, 1, 7, 4, 5} 

>>> b = {2, 8, 3, 1, 5} 

>>> c = {1, 0, 4, 6, 5} 

>>> d = {8, 2, 6, 3, 5}

>>> a&b&c&d
{5}
>>> a.intersection(b)
{1, 3, 5}
>>> a.intersection(b,c,d)
{5}
>>> a = {3, 6, 1} 

>>> b = {2, 8, 3, 1} 

>>> a-b
{6}
>>> b-a
{8, 2}
>>> a.difference(b)
{6}
>>> a = {3, 1, 7, 4, 5} 

>>> b = {2, 8, 3, 1, 5} 

>>> c = {1, 0, 4, 6, 5} 

>>> a-b-c
{7}
>>> a.difference(b,c)
{7}
>>> a = {3, 6, 1}

>>> b = {2, 8, 3, 1}

>>> 
>>> a^b
{2, 6, 8}
>>> a = {3, 1, 7, 4, 5} 		

>>> b = {2, 8, 3, 1, 5} 		

>>> c = {1, 0, 4, 6, 5} 		

>>> d = {8, 2, 6, 3, 5}
>>> 
>>> a^b^c^d
{0, 1, 3, 7}
>>> s = {34,1, 56.7,8-9j,"Python", 23, 34, 0, 3, True, 77, "python", False, 12}
>>> s
{0, 1, 34, 3, 12, (8-9j), 77, 'python', 23, 56.7, 'Python'}
>>> s.add(100)
>>> s
{0, 1, 34, 3, 100, 12, (8-9j), 77, 'python', 23, 56.7, 'Python'}
>>> s.update([7,14,21,28])
>>> s
{0, 1, 34, 3, 100, 7, 12, (8-9j), 77, 14, 'python', 21, 23, 56.7, 28, 'Python'}
>>> s.remove(8-9j)
>>> s
{0, 1, 34, 3, 100, 7, 12, 77, 14, 'python', 21, 23, 56.7, 28, 'Python'}
>>> s.discard('python')
>>> s
{0, 1, 34, 3, 100, 7, 12, 77, 14, 21, 23, 56.7, 28, 'Python'}
>>> s.remove(999)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    s.remove(999)
KeyError: 999
>>> s.discard(999)
>>> s
{0, 1, 34, 3, 100, 7, 12, 77, 14, 21, 23, 56.7, 28, 'Python'}
>>> s.pop()
0
>>> s.pop()
1
>>> s
{34, 3, 100, 7, 12, 77, 14, 21, 23, 56.7, 28, 'Python'}
>>> b = s.copy()
>>> b
{34, 3, 100, 7, 12, 77, 14, 21, 23, 56.7, 28, 'Python'}
>>> b.clear()
>>> b
set()
>>> 