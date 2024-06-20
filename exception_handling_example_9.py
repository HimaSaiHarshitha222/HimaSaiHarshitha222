def avg(list): 
   tot=0 
   for x in list: 
      tot+=x 
   avg = tot/len(list) 
   return tot, avg 

try: 
   t,a = avg([]) 
   print('Total= {}, Average= {}'.format(t,a)) 
except TypeError: 
   print('Type Error, please provide numbers.') 
except ZeroDivisionError: 
   print('ZeroDivisionError, please do not give empty list.')
