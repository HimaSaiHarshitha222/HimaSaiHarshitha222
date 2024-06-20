Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pandas import *
>>> df = read_excel("D:\Python\PANDAS\Data.xlsx","Sheet1")
>>> df
   EmpId     Ename    Sal         DoJ
0   1001      Balu  25000   30-6-2014
1   1002   Gautham  36500  25-12-2016
2   1003      Gani  45200   24-5-2015
3   1004  Siddarth  32000   16-5-2013
4   1005     Subbu  18500  22-11-2018
5   1006       Jai  26000   19-8-2012
6   1007     Nanda  15500  30-10-2019
>>> df['Ename']
0        Balu
1     Gautham
2        Gani
3    Siddarth
4       Subbu
5         Jai
6       Nanda
Name: Ename, dtype: object
>>> df['Sal']
0    25000
1    36500
2    45200
3    32000
4    18500
5    26000
6    15500
Name: Sal, dtype: int64
>>> df[['Ename','Sal']]
      Ename    Sal
0      Balu  25000
1   Gautham  36500
2      Gani  45200
3  Siddarth  32000
4     Subbu  18500
5       Jai  26000
6     Nanda  15500
>>> df1 = read_csv("D:\Python\PANDAS\Data.csv")
>>> df1
   EmpId     Ename    Sal         DoJ
0   1001      Balu  25000  30-06-2014
1   1002   Gautham  36500  31-12-2016
2   1003      Gani  45200  22-11-2018
3   1004  Siddarth  32000  16-05-2013
4   1005     Subbu  18500  22-11-2018
5   1006       Jai  26000  19-08-2012
6   1007   Bharath  23000  25-07-2019
7   1008   Sanjana  15500  30-06-2017
8   1009      Ravi  18000  30-06-2018
>>> empdata={"EmpId":[1001,1002,1003,1004,1005,1006],"Ename":["Balu","Gautham","Gani","Siddarth","Subbu","Jai"],"Sal":[25000,36500,45200,32000,18500,26000],"DoJ":["30-6-2014","25-12-2016","24-5-2015","16-5-2013","22-11-2018","19-8-2012"]}
