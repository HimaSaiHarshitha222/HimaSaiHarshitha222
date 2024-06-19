start = 1
stop = 2
num = stop
for row in range(2, 6):#2,3,4,5
   for col in range(start, stop):
     num = num - 1
     print (num, end=' ')
   print("")
   start = stop
   stop +=row
   num = stop
