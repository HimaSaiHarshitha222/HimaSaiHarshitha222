Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Naveen"
>>> s = s+'Kumar'
>>> s
'NaveenKumar'
>>> s = "Naveen"
>>> s
'Naveen'
>>> id(s)
2105218918448
>>> s = s+'Kumar'
>>> s
'NaveenKumar'
>>> id(s)
2105218918704
>>> a = [1,2,3]
>>> id(a)
2105188005696
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> id(a)
2105188005696
>>> a[0] = 4
>>> a
[4, 2, 3, 4]
>>> id(a)
2105188005696
>>> 