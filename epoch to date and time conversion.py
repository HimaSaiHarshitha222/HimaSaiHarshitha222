import time 

t = time.localtime(time.time()) 

d = t.tm_mday 
m = t.tm_mon 
y = t.tm_year 
print('Current date is: %d - %d - %d' %(d, m, y)) 

h = t.tm_hour 
m = t.tm_min 
s = t.tm_sec 
print('Current time is: %d: %d: %d' %(h,m,s))
