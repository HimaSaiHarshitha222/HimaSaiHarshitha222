Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Welcome to Python Programming"
>>> 'c' in s
True
>>> 'java' in s
False
>>> 'python' in s
False
>>> 
>>> 'Python' in s
True
>>> 'java' not in s
True
>>> 'NTR' > 'Mahesh Babu'
True
>>> 'Box' > 'Boy'
False
>>> 'Naveen' == 'naveen'
False
>>> 'Naveen' != 'naveen'
True
>>> 'Naveen' < 'naveen'
True
>>> ord('N')
78
>>> ord('n')
110
>>> "         This is a Sample Text Message        ".lstrip()
'This is a Sample Text Message        '
>>> "         This is a Sample Text Message        ".rstrip()
'         This is a Sample Text Message'
>>> "         This is a Sample Text Message        ".strip()
'This is a Sample Text Message'
>>> s
'Welcome to Python Programming'
>>> s.find('l')
2
>>> s.find('e')
1
>>> s.index('l')
2
>>> s.index('le')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.index('le')
ValueError: substring not found
>>> s.index('e')
1
>>> s
'Welcome to Python Programming'
>>> s.find('Python')
11
>>> s.index('Python')
11
>>> s.find('Java')
-1
>>> s.index('Java')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.index('Java')
ValueError: substring not found
>>> s
'Welcome to Python Programming'
>>> s.rfind('e')
6
>>> s.rindex('e')
6
>>> s.rfind('DJ')
-1
>>> s.rindex('DJ')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.rindex('DJ')
ValueError: substring not found
>>> s
'Welcome to Python Programming'
>>> s.count('e')
2
>>> s.count('o')
4
>>> s.count('Python')
1
>>> s.count('Java')
0
>>> "That's a Beautiful Bird".replace('Bird','Flower')
"That's a Beautiful Flower"
>>> "That's a Beautiful Bird".replace('a','*')
"Th*t's * Be*utiful Bird"
>>> s
'Welcome to Python Programming'
>>> s.replace('o','#')
'Welc#me t# Pyth#n Pr#gramming'
>>> s.replace('o','#',1)
'Welc#me to Python Programming'
>>> s.replace('o','#',2)
'Welc#me t# Python Programming'
>>> s
'Welcome to Python Programming'
>>> s.replace(' ','')
'WelcometoPythonProgramming'
>>> 