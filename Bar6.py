import matplotlib.pyplot as plt
from pandas import *

df = read_excel("D:\Python\PANDAS\Gold Prices.xlsx","Sheet1")
x = df['Year']
y = df['Price']

plt.plot(x, y, label='Gold Prices in India',color='green') 


plt.title('Gold Prices since 1964') 
plt.xlabel('Years') 
plt.ylabel('Price in Rs') 

plt.legend()
plt.show()
