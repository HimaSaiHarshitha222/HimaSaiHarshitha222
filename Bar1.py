import matplotlib.pyplot as plt 

x = [1001, 1003, 1006, 1007, 1009, 1011] 
y = [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99] 

x1 = [1002, 1004, 1010, 1008, 1014, 1015] 
y1 = [5000, 6000, 4500.00, 12000, 9000, 10000] 

plt.bar(x,y, label='Sales dept', color='red') 
plt.bar(x1, y1, label='Production dept', color='green') 

plt.xlabel('Emp Id')
plt.ylabel('Salaries') 
plt.title('Digi Brains Academy') 
plt.legend() 

plt.show()

