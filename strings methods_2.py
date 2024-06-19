Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "This is a Sample String"
>>> s.replace('is','*')
'Th* * a Sample String'
>>> s.replace('i','*')
'Th*s *s a Sample Str*ng'
>>> s.replace('i','*',1)
'Th*s is a Sample String'
>>> 'anushka'.replace('a','')
'nushk'
>>> 'anushka'.replace('a','',1)
'nushka'
>>> s
'This is a Sample String'
>>> s.replace(' ','')
'ThisisaSampleString'
>>> '1034'.replace('0','5')
'1534'
>>> s
'This is a Sample String'
>>> s.split()
['This', 'is', 'a', 'Sample', 'String']
>>> len(s.split())
5
>>> s
'This is a Sample String'
>>> len(s)
23
>>> '23,56,7,8,9,0,2.34,98.12,9,11'.split(',')
['23', '56', '7', '8', '9', '0', '2.34', '98.12', '9', '11']
>>> a = ['23', '56', '7', '8', '9', '0', '2.34', '98.12', '9', '11']
>>> ''.join(a)
'235678902.3498.12911'
>>> ','.join(a)
'23,56,7,8,9,0,2.34,98.12,9,11'
>>> '-'.join(a)
'23-56-7-8-9-0-2.34-98.12-9-11'
>>> b = [11,45,7]
>>> ''.join(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ''.join(b)
TypeError: sequence item 0: expected str instance, int found
>>> b = ['11','45','7']
>>> ''.join(b)
'11457'
>>> 'navEEn kUMAr'.lower()
'naveen kumar'
>>> 'navEEn kUMAr'.upper()
'NAVEEN KUMAR'
>>> 'navEEn kUMAr'.title()
'Naveen Kumar'
>>> 'navEEn kUMAr'.capitalize()
'Naveen kumar'
>>> 'navEEn kUMAr'.swapcase()
'NAVeeN KumaR'
>>> 'Abdul Kalam'.startswith('A')
True
>>> 'Abdul Kalam'.endswith('m')
True
>>> 'Abdul Kalam'.endswith('am')
True
>>> 'Abdul Kalam'.endswith('lam')
True
>>> "James Bond@007".isalnum()
False
>>> "JamesBond007".isalnum()
True
>>> "JamesBond".isalnum()
True
>>> '45346'.isalnum()
True
>>> "JamesBond".isalpha()
True
>>> "JamesBond007".isalpha()
False
>>> "JamesBond".islower()
False
>>> "jamesbond".islower()
True
>>> "jamesbond".upper()
'JAMESBOND'
>>> 'JAMESBOND'.isupper()
True
>>> "james bond".title()
'James Bond'
>>> 'James Bond'.istitle()
True
>>> '4545'.isdigit()
True
>>> '45.45'.isdigit()
False
>>> ' '.isspace()
True
>>> s = "It is Summer"
>>> s.index('Summer')
6
>>> s[0:6]
'It is '
>>> s[6:]
'Summer'
>>> s[0:6]+'Hot'+s[6:]
'It is HotSummer'
>>> s[0:6]+'Hot'+s[5:]
'It is Hot Summer'
>>> 