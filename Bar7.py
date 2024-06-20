import matplotlib.pyplot as plt
from pandas import *

df = read_excel("D:\Python\PANDAS\GDP.xlsx","Sheet1")
x = df['Year']
y = df['GDP Growth']

plt.plot(x, y, label='Indian GDP',color='green') 


plt.title('Indian GDP since 1960') 
plt.xlabel('Years') 
plt.ylabel('GDP Growth') 

plt.legend()
plt.show()
